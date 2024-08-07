from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import src.bot.app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    user = msg.from_user
    
    # client = httpx.AsyncClient(base_url="http://localhost:8000")
    
    # await client.post(
    #     "/auth/signin",
    #     json=Signin(
    #         id=user.id,
    #         first_name=user.first_name,
    #         last_name=user.last_name,
    #         username=user.username,
    #         auth_date=datetime.now(),
    #     ),
    # )
    await msg.answer(
        "Hi",
        reply_markup=kb.start,
    )


@router.message(Command("help"))
async def cmd_help(msg: Message) -> None:
    await msg.answer("There is nothing u needs")


@router.message(F.data == "Room")
async def room(cb: CallbackQuery) -> None:
    await cb.answer("")
    await cb.message.answer("What", reply_markup=kb.room)


@router.callback_query(F.data == "Events")
async def events(cb: CallbackQuery) -> None:
    await cb.answer("")
    await cb.message.answer("there is no events")
