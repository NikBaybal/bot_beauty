from aiogram.types import InputMediaPhoto
from aiogram.types import FSInputFile

def img_answer(path:str):
    file_in=FSInputFile(path, "rb")
    return file_in

def img(path:str,text:str)->InputMediaPhoto:
    file_in=FSInputFile(path, "rb")
    return InputMediaPhoto(media=file_in, caption=text, parse_mode = 'HTML')


