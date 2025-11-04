import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()  # lädt die .env-Datei

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(123456789012345678)
    await channel.send(
        content=f"👋 Willkommen {member.mention}!\nHab viel Spaß auf **Sunrise RP (;**",
        file=discord.File("sunriserp.png")
    )

# Hier wird dein Token sicher geladen:
bot.run(os.getenv("BOT_TOKEN"))
