from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from utils.constants import *

from states import SearchStates
from utils import search_movie, search_tv
from keyboards import media_list_keyboard, main_menu_keyboard
from keyboards import cancel_keyboard

search_router = Router()
@search_router.message(Command(commands=[SEARCH_COMMAND]))
async def cmd_search(message: types.Message, state: FSMContext):
    """Обробник команди /search"""
    await state.set_state(SearchStates.waiting_for_query)
    await message.answer(
        "Введіть назву фільму або серіалу для пошуку:",
        reply_markup=cancel_keyboard("cancel_search")
    )
    
@search_router.message(F.text == 'Пошук')
async def text_search(message: types.message, state: FSMContext):
    await cmd_search(message,state)
    
@search_router.message(StateFilter(SearchStates.waiting_for_query))
async def text_search(message: types.message, state: FSMContext):
    query = message.text.strip()
    if not query:
        await message.answer('Будь ласка введіть назву фільму або серіалу')
        return
    search_message = await message.answer('Пошук...')
    movies_result = await search_movie(query)
    tv_result = await search_tv(query)
    
    await state.clear()
    
    
    movies_count = len(movies_result.get('results', [])) if movies_result else 0
    
    if movies_count == 0 and tv_count == 0:
        await search_message.edit_text('Не знайдено')
        return
    text = f'Результати пошуку за запитом'<h>(query)</h>:/n/n
    
    if movies_count > 0 :
        text = f <b>(movie_count)'фільмів не знайдено'
        for i, movie in enumerate(movies_result['results'][:5], 1)
            title = movie.get('title', 'невідома назва')
            release_date = movie_get('release_date', '')
            release_year = ([release_date[:4]]) if release_date else ''
            rating = movie.get('vote_average', 0)
            rating_stars = int(rating / 2) if rating else ''
            text = [i] <b>[title]</b> [release_year] [rating_stars]/n
            
    if tv_count >5:
        text += f"...і ще"  <b>{tv_count}</b>
        for i, tv in enumarate(tv_result['results'][:5], 1)
            title = tv.get('name', 'невідома назва') 
            first_air_date = tv.get("first_air_date", '')
            rating = tv.get("vote_average", 0)
            rating_stars = int(rating / 2)   if rating else ''
            text += '/n'         
        if tv_count >5 :
            text += f '...і ще'{ tv_count    5}
    await search_message.edit_text(text, parse_mode = 'HTML')
search_router.callback_query(lambda c: c.data == 'cancel_search')
async def cancel_search(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.clear()
    await callback_query.message.edit_text('Пошук скасовано')
    
    
def register_search_handlers(dp):
    dp.include_router(search_router)
