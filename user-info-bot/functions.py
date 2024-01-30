from aiogram import Bot
from aiogram.types import Message
from states import sign_up
from aiogram.fsm.context import FSMContext

async def get_user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    matn = (f"{message.from_user.mention_html('USER')} INFO:\n\n"
            f"Ism-familya: {message.from_user.full_name}\n\n"
            f"ID: {message.from_user.id}\n\n"
            )

    if user.bio: matn += f"Tarjimai holi: {user.bio}\n\n"
    if message.from_user.username: matn += f"Username: @{message.from_user.username}"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption=matn, parse_mode="HTML")
    else:
        await message.answer(matn, parse_mode="HTML")

async def start_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Salom, ismingizni kiriting." )
    await state.set_state(sign_up.name)

async def help_answer(message: Message, bot: Bot):
    matn = f"""
        <b>Bot Buyruqlari</b>

/start - Botni ishga tushurish
/help Yordam!    
"""
    await bot.send_message(message.from_user.id, matn, parse_mode="HTML")


async def sign_up_name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Ismingiz qabul qilindi: {message.text}")
    await message.answer(f"Yoshingizni kiriting.")
    await state.set_state(sign_up.age)

async def sign_up_age(message: Message, bot: Bot, state: FSMContext):
    # await message.answer(f"Yoshingiz qabul qilindi: {message.text}")
    data = await state.get_data()
    await message.answer(f"""Ma'lumotlaringiz:
Ismingiz: {data.get("name")}
Yoshingiz: {message.text}
""")
    await state.clear()