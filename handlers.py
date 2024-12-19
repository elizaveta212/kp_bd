from aiogram import F, Router
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup

import keyboard as kb

import asyncpg
from database import get_perfumes, create_database, create_tables

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()
    
class Form(StatesGroup):
    gender = State()
    occasion = State()
    season = State()
    price_range = State()
    fragrance_group = State()
    notes = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! Этот сервис поможет подобрать парфюм на основе Ваших предпочтений.')
    await message.reply('Для кого Вы хотите подобрать аромат?', reply_markup=kb.gender)

@router.callback_query(F.data.in_(['женский', 'мужской', 'унисекс']))
async def process_gender(callback: CallbackQuery, state: FSMContext):
    selected_gender = callback.data
    await callback.message.answer(f'Вы выбрали {selected_gender} парфюмерию.')
    await state.update_data(gender=selected_gender)
    await callback.message.answer('Какую группу ароматов Вы предпочитаете?', reply_markup=kb.fragrance_group)
    await state.set_state(Form.fragrance_group)
    

@router.callback_query(F.data.in_(['цветочные', 'цитрусовые', 'фруктовые','восточные', 'древесные', 'фужерные', 'гурманские', 'зелёные', 'акватические']))
async def process_fragrance_group(callback: CallbackQuery, state: FSMContext):
    selected_fragrance_group = callback.data
    await callback.message.answer(f'Вы выбрали группу ароматов {selected_fragrance_group}.')
    await state.update_data(fragrance_group=selected_fragrance_group)
    notes_keyboard = None
    if selected_fragrance_group == 'цветочные':
        notes_keyboard = kb.notes_keyboard_flower 
    elif selected_fragrance_group == 'цитрусовые':
        notes_keyboard = kb.notes_keyboard_citrus  
    elif selected_fragrance_group == 'фруктовые':
        notes_keyboard = kb.notes_keyboard_fruits
    elif selected_fragrance_group == 'восточные':
        notes_keyboard = kb.notes_keyboard_vostok
    elif selected_fragrance_group == 'древесные':
        notes_keyboard = kb.notes_keyboard_wood
    elif selected_fragrance_group == 'гурманские':
        notes_keyboard = kb.notes_keyboard_sweet 
    elif selected_fragrance_group == 'фужерные':
        notes_keyboard = kb.notes_keyboard_fugers
    elif selected_fragrance_group == 'зелёные':
        notes_keyboard = kb.notes_keyboard_green
    elif selected_fragrance_group == 'акватические':
        notes_keyboard = kb.notes_keyboard_aqua
    if notes_keyboard:
        await callback.message.answer('Выберите ноты:', reply_markup=notes_keyboard)
        await state.set_state(Form.notes)

@router.callback_query(F.data.in_(['роза', 'мимоза', 'ирис', 'лаванда', 'жасмин', 'тубероза', 'бергамот', 'лимон', 'апельсин', 'мандарин', 'юдзу', 'нероли', 
                                   'уд', 'ладан', 'сандал', 'шафран', 'иланг-иланг', 'пачули', 'кедр', 'ель', 'эвкалипт', 'берёза', 'сосна', 'ветивер', 
                                    'вишня', 'дыня', 'клубника', 'яблоко', 'кокос', 'персик','герань', 'дубовый мох', 'бобы тонка', 'можжевельник', 'камфора',
                                    'папоротник', 'мёд', 'ваниль', 'шоколад', 'карамель', 'конфеты ирис', 'тирамису', 'морская вода', 'водоросли', 'лотос', 
                                    'огурец', 'арбуз', 'водная лилия', 'мята', 'полынь', 'розмарин', 'зелёный чай', 'базилик', 'свежескошенная трава']))
async def process_note_selection(callback: CallbackQuery, state: FSMContext):
    selected_note = callback.data
    await callback.message.answer(f'Вы выбрали ноту: {selected_note}.')
    await state.update_data(notes=selected_note)
    await callback.message.answer('Какой тип парфюма Вам нужен?', reply_markup=kb.occasion)
    await state.set_state(Form.occasion)

@router.callback_query(F.data.in_(['повседневный', 'вечерний', 'спортивный']))
async def process_season(callback: CallbackQuery, state: FSMContext):
    selected_occasion = callback.data
    await callback.message.answer(f'Вы выбрали {selected_occasion} аромат.')
    await state.update_data(occasion = selected_occasion)
    await callback.message.answer('На какое время года нужен аромат?', reply_markup=kb.season)
    await state.set_state(Form.season)

@router.callback_query(F.data.in_(['зима', 'весна', 'лето', 'осень']))
async def process_season(callback: CallbackQuery, state: FSMContext):
    selected_season = callback.data
    await callback.message.answer(f'Вы выбрали время года {selected_season}.')
    await state.update_data(occasion = selected_season)
    await callback.message.answer('В каком ценовом диапазоне ищем парфюм?', reply_markup=kb.price_range)
    await state.set_state(Form.price_range)

@router.callback_query(F.data.in_(['до 5000', 'от 5000 до 10000', 'от 10 000 до 15000', 'от 15 000 и более']))
async def process_price_range(callback: CallbackQuery, state: FSMContext):
    selected_price_range = callback.data
    await callback.message.answer(f'Вы выбрали ценовой диапазон {selected_price_range}.')
    await state.update_data(price_range=selected_price_range)
    await callback.message.answer('Подбираем парфюм для Вас...')  
    user_data = await state.get_data() 
    gender = user_data.get('gender')
    fragrance_groups = user_data.get('group')
    occasion = user_data.get('occasion')
    season = user_data.get('season')
    price_range = user_data.get('price_range')
    note = user_data.get('note')
    
    conn = await asyncpg.connect(database='perfum_database', user='postgres', password='0212er', host='localhost', port='5432')
    
    async def get_gender_id(conn, gender):
      query = "SELECT gender_id FROM genders WHERE gender_name = $1"
      result = await conn.fetchrow(query, gender)
      return result['gender_id'] if result else None
        
    async def get_fragrance_group_id(conn, group):
      query = "SELECT group_id FROM fragrance_groups WHERE group_name = $1"
      result = await conn.fetchrow(query, group)
      return result['group_id'] if result else None
        
    async def get_occasion_id(conn, occasion):
      query = "SELECT occasion_id FROM occasions WHERE occasion_name = $1"
      result = await conn.fetchrow(query, occasion)
      return result['occasion_id'] if result else None
        
    async def get_season_id(conn, season):
      query = "SELECT season_id FROM seasons WHERE season_name = $1"
      result = await conn.fetchrow(query, season)
      return result['season_id'] if result else None
        
    async def get_price_range_id(conn, price_range):
      query = "SELECT price_range_id FROM price_ranges WHERE price_range_name = $1"
      result = await conn.fetchrow(query, price_range)
      return result['price_range_id'] if result else None
        
    async def get_note_id(conn, note):
      query = "SELECT note_id FROM notes WHERE note_name = $1"
      result = await conn.fetchrow(query, note)
      return result['note_id'] if result else None
        
    try:
        gender_id = await get_gender_id(conn, gender) 
        fragrance_group_id = await get_fragrance_group_id(conn, fragrance_groups) 
        occasion_id = await get_occasion_id(conn, occasion) 
        season_id = await get_season_id(conn, season) 
        price_range_id = await get_price_range_id(conn, price_range)
        note_id = await get_note_id(conn, note)
        gender_id = await get_gender_id(conn, gender)
        
        perfumes = await get_perfumes(conn, gender_id, fragrance_group_id, occasion_id, season_id, price_range_id, note)
        
        if perfumes:
            await callback.message.answer("Подобранные ароматы:\n" + "\n".join(perfumes))
        else:
            await callback.message.answer("К сожалению, ароматы с такими характеристиками не найдены.")
    except Exception as _ex:
        await callback.message.answer("[INFO] Ошибка при извлечении ароматов: " + str(_ex))
    finally:
        await conn.close()
        print("[INFO] Завершение соединения с PostgreSQL")

