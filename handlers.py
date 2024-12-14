from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext 
import keyboard as kb
from database import get_perfumes

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
    await Form.fragrance_group.set()
    

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
        await Form.notes.set()

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
    await Form.occasion.set()

@router.callback_query(F.data.in_(['повседневный', 'вечерний', 'спортивный']))
async def process_season(callback: CallbackQuery, state: FSMContext):
    selected_occasion = callback.data
    await callback.message.answer(f'Вы выбрали {selected_occasion} аромат.')
    await state.update_data(occasion = selected_occasion)
    await callback.message.answer('На какое время года нужен аромат?', reply_markup=kb.season)
    await Form.season.set()

@router.callback_query(F.data.in_(['зима', 'весна', 'лето', 'осень']))
async def process_season(callback: CallbackQuery, state: FSMContext):
    selected_season = callback.data
    await callback.message.answer(f'Вы выбрали время года {selected_season}.')
    await state.update_data(occasion = selected_season)
    await callback.message.answer('В каком ценовом диапазоне ищем парфюм?', reply_markup=kb.price_range)
    await Form.price_range.set()

@router.callback_query(F.data.in_(['до 5000', 'от 5000 до 10000', 'от 10 000 до 15000', 'от 15 000 и более']))
async def process_price_range(callback: CallbackQuery, state: FSMContext):
    selected_price_range= callback.data
    await callback.message.answer(f'Вы выбрали ценовой диапазон {selected_price_range}.')
    await state.update_data(price_range = selected_price_range)
    await callback.message.answer('Подбираем парфюм для Вас...')
    user_data = await state.get_data() 
    gender = user_data.get('gender')
    fragrance_group = user_data.get('fragrance_group')
    occasion = user_data.get('occasion')
    price_range = user_data.get('price_range')
    season = user_data.get('season')
    notes = user_data.get('notes')
    perfumes = get_perfumes(gender, fragrance_group, occasion, season, price_range, notes)
    if perfumes:
        await callback.message.answer("Подобранные ароматы:\n" + "\n".join(perfumes))
    else:
        await callback.message.answer("К сожалению, ароматы с такими характеристиками не найдены.")
