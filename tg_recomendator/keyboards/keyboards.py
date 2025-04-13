from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

from utiles.constans import *

def main_menu_keyboard():
    buttons = [
        [KeyboardButton(text="Категорії"), KeyboardButton(text="Пошук")]
        [KeyboardButton(text="Популярне"), KeyboardButton(text="Допомога")] 
    ]
    
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard

def admin_keyboard():
    buttons = [
        [KeyboardButton(text='Додати категорії'),
         KeyboardButton(text='Додати жанр')]
        [KeyboardButton(text='Додати фільм\серіал'),
         KeyboardButton(text='Назад до меню')]
    ]
    
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard

def categories_inline_keyboard(categories):
    buttons = []

    for category in categories:
        buttons.append(
            InlineKeyboardButton(text=category['name'],
                callback_data=f"category_{category['id']}")
        )
        buttons.append([InlineKeyboardButton(text='Назад', callback_data='back_to_main')])
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard
    
def genras_inline_keyboard(genres, category_id):
    buttons = []
    for genre in genres:
        buttons.append(
            InlineKeyboardButton(text_genre["name"])
                        callback_data=f'genre_{genre['id']}_{category_id}'
        )   
        buttons.append([InlineKeyboardButton(text='Назад', callback_data='back_to_main')])
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard
    
def media_list_keyboard(page = 1, max_page=1, media_type=None, genre_id=None):
    buttons = []
    navigation = []
    if page > 1:
        prev_page = f'page_{page - 1}'
        if media_type:
            prev_page += f'_(media_type)'
        if genre_id:
            prev_page += f'_(genre_id)'
        navigation.append(InlineKeyboardButton(text='назад', callback_data=prev_page))
        navigation.append(InlineKeyboardButton(text=f'[page]\[max_page]',
                                               callback_data='current_page'))
    if page > max_page:
        next_page = f'page_{page + 1}'
        if media_type:
            prev_page += f'_(media_type)'
        if genre_id:
            prev_page += f'_(genre_id)'
        navigation.append(InlineKeyboardButton(text='назад', callback_data=next_page))
        databuttons.append(navigation)
        if genre_id:
            buttons.append(InlineKeyboardButton(text='Назад до жанрів'
                                                callback_data=f'back to genres(media_type)'))
        else:
            buttons.append(InlineKeyboardButton(text='Назад до категорій'
                                                callback_data=f'back to genres(media_type)'))
            
        keyboard = InlineKeyboardButton(inline-keyboard=buttons)
        return keyboard
    def media_details_keyboard(media_id, media_type):
        buttons.append(
        (InlineKeyboardButton(text='Переглянути'
        InlineKeyboardButton(text='Назад', callback_data='back to main list')
        
        
                                         
        )
         
         buttons.append(
        (InlineKeyboardButton(text='Дивитися трейлер'
                                        callback_data=f'watch trailer'_[media_type]_[media_id]))
        InlineKeyboardButton(text='Назад', callback_data='back to  list'_{media_type})
        keyboard = InlineKeyboardButton(inline-keyboard=buttons)
        return keyboard
         )
def media_type_keyboard();
buttons = {
    [InlineKeyboardButton(text='Фільм', callback_data=f'add_media_movie')]
    [InlineKeyboardButton(text='серіал', callback_data=f'add_media_tv')]
    [InlineKeyboardButton(text='мультик', callback_data=f'add_media_animation')]
    [InlineKeyboardButton(text='назад', callback_data=f'cancel_add_media')]
}
    keyboard = InlineKeyboardButton(inline_keyboard=buttons)
    return = keyboard
def cancel_keyboard(callback_data='cancel'):
    buttons = [
    [InlineKeyboardButton(text = 'Скасувати', callback_data=callback_data)]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard



         