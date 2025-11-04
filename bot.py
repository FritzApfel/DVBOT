import os
import discord
from discord.ext import commands

# Intents aktivieren, damit der Bot Join-Events sehen darf
intents = discord.Intents.default()
intents.members = True  # wichtig!
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

# Event: Wenn ein neuer User dem Server joint
@bot.event
async def on_member_join(member):
    # ID des Channels, in den die Nachricht gesendet werden soll
    # 👉 diese musst du anpassen (Rechtsklick auf Channel → "ID kopieren")
    WELCOME_CHANNEL_ID = 123456789012345678  

    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        print("❌ Channel nicht gefunden. Bitte Channel-ID prüfen.")
        return

    # Nachricht + Bild senden
    await channel.send(
        content=f"👋 Willkommen {member.mention}!\nHab viel Spaß auf **Sunrise RP (;**",
        file=discord.File("sunriserp.png")
    )

bot.run(os.getenv("BOT_TOKEN"))
