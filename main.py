import os
import asyncio
from highrise import BaseBot, Position, main as highrise_main

HIGHRISE_TOKEN = os.getenv("HIGHRISE_TOKEN")
HIGHRISE_ROOM_ID = os.getenv("HIGHRISE_ROOM_ID")


class MyBot(BaseBot):
    async def on_start(self):
        print("✅ Bot démarré avec succès !")

    async def on_chat(self, user, message):
        msg = message.lower()

        if msg == "bonjour":
            await self.highrise.chat(f"Bonjour {user.username} 👋")

        elif msg == "aurevoir":
            await self.highrise.chat(f"À bientôt {user.username} 👋")

        elif msg.startswith("tp"):
            await self.highrise.teleport(
                user.id, Position(x=0.0, y=0.0, z=0.0, facing="FrontLeft")
            )

        elif msg.startswith("kick "):
            parts = msg.split(" ", 1)
            if len(parts) > 1:
                target = parts[1]
                await self.highrise.chat(f"{target} a été expulsé 🚪")

        elif msg.startswith("prison "):
            parts = msg.split(" ", 1)
            if len(parts) > 1:
                target = parts[1]
                await self.highrise.chat(f"{target} a été envoyé en prison 🚔")

        elif msg.startswith("libere "):
            parts = msg.split(" ", 1)
            if len(parts) > 1:
                target = parts[1]
                await self.highrise.chat(f"{target} a été libéré 🕊️")

        elif msg.startswith("move "):
            await self.highrise.chat("Commande move exécutée 🟢")


        elif msg.startswith("where "):
            parts = msg.split(" ", 1)
            if len(parts) > 1:
                target = parts[1]
                await self.highrise.chat(f"{target} est à une position inconnue 📍")

        elif msg.startswith("join "):
            parts = msg.split(" ", 1)
            if len(parts) > 1:
                target = parts[1]
                await self.highrise.chat(f"Bienvenue {target} 🎉")


async def start_bot():
    await highrise_main(
        MyBot(),
        token=HIGHRISE_TOKEN,
        room_id=HIGHRISE_ROOM_ID
    )


if __name__ == "__main__":
    asyncio.run(start_bot())
