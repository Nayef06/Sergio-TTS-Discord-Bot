from gtts import gTTS
import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


# Set the voice channel name and the target text channel
TARGET_VC_NAME = "general"
TARGET_TEXT_CHANNEL_NAME = "sergio"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    for guild in bot.guilds:
        print(f'Connected to server: {guild.name}')

@bot.event
async def on_message(message):
    if message.channel.name == TARGET_TEXT_CHANNEL_NAME:
        # Find the voice channel named "general"
        for channel in message.guild.channels:
            if channel.name == TARGET_VC_NAME and channel.type == discord.ChannelType.voice:
                # Connect to the voice channel if not already connected
                voice_client = discord.utils.get(bot.voice_clients, guild=message.guild)
                if not voice_client or not voice_client.channel:
                    voice_client = await channel.connect()

                # Use gTTS to convert text to speech
                tts = gTTS(text=message.content, lang='en', slow=False)
                tts.save("tts_message.mp3")

                # Play the saved audio file in the voice channel
                audio_source = discord.FFmpegPCMAudio("tts_message.mp3")
                voice_client.play(audio_source)

                # Wait for the bot to finish speaking before processing the next message
                while voice_client.is_playing():
                    await asyncio.sleep(1)

                # await voice_client.disconnect()

bot.run('YOUR_BOT_TOKEN')  # Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
