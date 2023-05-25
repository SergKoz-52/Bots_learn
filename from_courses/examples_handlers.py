from aiogram.types import ContentType
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

ContentType.AUDIO == 'audio'                                # True
ContentType.TEXT == 'text'                                  # True
ContentType.PHOTO == 'photo'                                # True
ContentType.STICKER == 'sticker'                            # True
ContentType.CONTACT == 'contact'                            # True
ContentType.LOCATION == 'location'                          # True
ContentType.POLL == 'poll'                                  # True
ContentType.SUCCESSFUL_PAYMENT == 'successful_payment'      # True
ContentType.VOICE == 'voice'                                # True
ContentType.WEB_APP_DATA == 'web_app_data'                  # True

dp = Dispatcher()


# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.content_type == ContentType.PHOTO)
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')


# Этот хэндлер будет срабатывать на тип контента "photo"
@dp.message(F.content_type == 'photo')
async def process_send_photo(message: Message):
    await message.answer(text='Вы прислали фото')


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({'voice', 'video', 'text'}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')


# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({ContentType.VOICE,
                                ContentType.VIDEO,
                                ContentType.TEXT}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')