from aiogram import types, Router, F
from aiogram.filters import command
from aiogram.fsm.context import FSMContext
from utils import db
from keyboards import main_menu_keyboard
from utils.constans import *



common_router = Router()

common_router.message(Command(commands=[START_COMMAND]))
asyns def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    
    user = message.from_user
    db.add_user(user.id, user.username, user.first_name, user.last_name)
    
    welcome_text = (
        f" Привіт, {user.first_name}!\n\n"
        f" Вітаю в нашому боті ремомендаторі для перегляду фільмів та серіалів\n\n"
        f" Ось що я можу для тебе зробити\n\n"
        f" Пошук фільмів та серіалів за жанрами\n\n "
        f" Перегляд трендових фільмів і так далі\n\n "
        f" Додавання власних фільмів та серіалів для перегляду\n\n "
        f" Використовуйте кнопки меню для навігації "
        
    )
    await message.answer(welcome_text, reply_markup=main_menu_keyboard)
    @common_rouler.message(Command(commands=[HELP_COMMAND]))
    @common_rouler.message(F.text == 'Допомога')
    async def cmd_help(message: types.Message):
        help_text = (
            '<b>Як користуватись ботом:<\b>\n\n'
            '<b>Категорії<\b> -перегляд фільмів та серіалів за жанрами\n'
            '<b>Пошук<\b>-пошук за назвою\n'
            '<b>Популярне<\b>-отримати список популярного\n\n'

            
        )
        await message.answer(help_text, parse_mode='HTML')
        
        @common_router.message(F.text == "Назад до меню")
        async def back to main