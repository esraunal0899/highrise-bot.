import asyncio
from highrise.__main__ import main as highrise_main
from highrise import BaseBot

class MyBot(BaseBot):
    async def on_start(self):
        print("Bot is running!")

async def start_bot():
    await highrise_main([
        {
            "bot": MyBot(),
            "token": "68a6ef1d04a0d92e1d5ae7689517a78aa5d87b347849656717695f06f68912ee",
            "room_id": "68cfa210982de1fbfa59feea"
        }
    ])

if __name__ == "__main__":
    asyncio.run(start_bot())
