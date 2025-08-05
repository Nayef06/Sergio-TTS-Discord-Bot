from gtts import gTTS
import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


TARGET_VC_NAME = "general" # Edit to own VC name
TARGET_TEXT_CHANNEL_NAME = "sergio" # Edit to own text channel name

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    for guild in bot.guilds:
        print(f'Connected to server: {guild.name}')

@bot.event
async def on_message(message):
    if message.channel.name == TARGET_TEXT_CHANNEL_NAME:
        for channel in message.guild.channels:
            if channel.name == TARGET_VC_NAME and channel.type == discord.ChannelType.voice:
                voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
                if not voice_client or not voice_client.channel:
                    voice_client = await channel.connect()

                tts = gTTS(text=message.content, lang='en', slow=False)
                tts.save("tts_message.mp3")

                audio_source = discord.FFmpegPCMAudio("tts_message.mp3")
                voice_client.play(audio_source)

                while voice_client.is_playing():
                    await asyncio.sleep(1)

                # await voice_client.disconnect()

bot.run('YOUR_BOT_TOKEN')  # Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token

