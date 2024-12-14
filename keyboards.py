from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

gender = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Для женщин', callback_data='женский')],
    [InlineKeyboardButton(text='Для мужчин', callback_data='мужской')],
    [InlineKeyboardButton(text='Унисекс', callback_data='унисекс')]])

fragrance_group = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Цветочные', callback_data='цветочные')],
    [InlineKeyboardButton(text='Цитрусовые', callback_data='цитрусовые')],
    [InlineKeyboardButton(text='Восточные', callback_data='восточные')],
    [InlineKeyboardButton(text='Древесные', callback_data='древесные')],
    [InlineKeyboardButton(text='Фруктовые', callback_data='фруктовые')],
    [InlineKeyboardButton(text='Фужерные', callback_data='фужерные')],
    [InlineKeyboardButton(text='Гурманские', callback_data='гурманские')],
    [InlineKeyboardButton(text='Зелёные', callback_data='зелёные')],
    [InlineKeyboardButton(text='Акватические', callback_data='акватические')]])

notes_keyboard_flower = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Роза', callback_data='роза')],
    [InlineKeyboardButton(text='Мимоза', callback_data='мимоза')],
    [InlineKeyboardButton(text='Ирис', callback_data='ирис')],
    [InlineKeyboardButton(text='Лаванда', callback_data='лаванда')],
    [InlineKeyboardButton(text='Жасмин', callback_data='жасмин')],
    [InlineKeyboardButton(text='Тубероза', callback_data='тубероза')]])

notes_keyboard_citrus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Бергамот', callback_data='бергамот')],
    [InlineKeyboardButton(text='Лимон', callback_data='лимон')],
    [InlineKeyboardButton(text='Апельсин', callback_data='апельсин')],
    [InlineKeyboardButton(text='Мандарин', callback_data='мандарин')],
    [InlineKeyboardButton(text='Юдзу', callback_data='юдзу')],
    [InlineKeyboardButton(text='Нероли', callback_data='нероли')]])

notes_keyboard_vostok = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Уд', callback_data='уд')],
    [InlineKeyboardButton(text='Ладан', callback_data='ладан')],
    [InlineKeyboardButton(text='Сандал', callback_data='сандал')],
    [InlineKeyboardButton(text='Шафран', callback_data='шафран')],
    [InlineKeyboardButton(text='Иланг-иланг', callback_data='иланг-иланг')],
    [InlineKeyboardButton(text='Пачули', callback_data='пачули')]])

notes_keyboard_wood = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кедр', callback_data='кедр')],
    [InlineKeyboardButton(text='Ель', callback_data='ель')],
    [InlineKeyboardButton(text='Эвкалипт', callback_data='эвкалипт')],
    [InlineKeyboardButton(text='Берёза', callback_data='берёза')],
    [InlineKeyboardButton(text='Ветивер', callback_data='ветивер')],
    [InlineKeyboardButton(text='Сосна', callback_data='сосна')]])

notes_keyboard_fruits = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вишня', callback_data='вишня')],
    [InlineKeyboardButton(text='Дыня', callback_data='дыня')],
    [InlineKeyboardButton(text='Клубника', callback_data='клубника')],
    [InlineKeyboardButton(text='Яблоко', callback_data='яблоко')],
    [InlineKeyboardButton(text='Кокос', callback_data='кокос')],
    [InlineKeyboardButton(text='Персик', callback_data='персик')]])

notes_keyboard_fugers = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Герань', callback_data='герань')],
    [InlineKeyboardButton(text='Дубовый мох', callback_data='дубовый мох')],
    [InlineKeyboardButton(text='Бобы тонка', callback_data='бобы тонка')],
    [InlineKeyboardButton(text='Можжевельник', callback_data='можжевельник')],
    [InlineKeyboardButton(text='Камфора', callback_data='камфора')],
    [InlineKeyboardButton(text='Папоротник', callback_data='папоротник')]])

notes_keyboard_sweet = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ваниль', callback_data='ваниль')],
    [InlineKeyboardButton(text='Шоколад', callback_data='шоколад')],
    [InlineKeyboardButton(text='Карамель', callback_data='карамель')],
    [InlineKeyboardButton(text='Конфеты ирис', callback_data='конфеты ирис')],
    [InlineKeyboardButton(text='Мёд', callback_data='мёд')],
    [InlineKeyboardButton(text='Тирамису', callback_data='тирамису')]])

notes_keyboard_aqua = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Морская вода', callback_data='морская вода')],
    [InlineKeyboardButton(text='Водоросли', callback_data='водоросли')],
    [InlineKeyboardButton(text='Водная лилия', callback_data='водная лилия')],
    [InlineKeyboardButton(text='Огурец', callback_data='огурец')],
    [InlineKeyboardButton(text='Лотос', callback_data='лотос')],
    [InlineKeyboardButton(text='Арбуз', callback_data='арбуз')]])

notes_keyboard_green = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мята', callback_data='мята')],
    [InlineKeyboardButton(text='Полынь', callback_data='полынь')],
    [InlineKeyboardButton(text='Розмарин', callback_data='розмарин')],
    [InlineKeyboardButton(text='Зелёный чай', callback_data='зелёный чай')],
    [InlineKeyboardButton(text='Базилик', callback_data='базилик')],
    [InlineKeyboardButton(text='Свежескошенная трава', callback_data='свежескошенная трава')]])

season = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зима', callback_data='зима')],
    [InlineKeyboardButton(text='Весна', callback_data='весна')],
    [InlineKeyboardButton(text='Лето', callback_data='лето')],
    [InlineKeyboardButton(text='Осень', callback_data='осень')]])

occasion = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Повседневный', callback_data='повседневный')],
    [InlineKeyboardButton(text='Вечерний', callback_data='вечерний')],
    [InlineKeyboardButton(text='Спортивный', callback_data='спортивный')]])

price_range = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='До 5000', callback_data='до 5000')],
    [InlineKeyboardButton(text='От 5000 до 10000', callback_data='от 5000 до 10000')],
    [InlineKeyboardButton(text='От 10000 до 15000', callback_data='от 10 000 до 15000')],
    [InlineKeyboardButton(text='От 15000 до 20000', callback_data='от 15 000 и более')]])
