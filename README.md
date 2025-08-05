
# Sergio's Discord TTS Bot

This is a simple Discord bot that listens for messages in a specific text channel and speaks them out loud in a voice channel using Google Text-to-Speech (gTTS).

## How it works

- The bot connects to your Discord server.
- It watches for new messages in a text channel named `sergio`.
- When someone sends a message in that channel, the bot uses gTTS to convert the message to speech.
- It joins a voice channel called `general` and plays the audio.

## Setup

1. **Install requirements**  
   Make sure you have Python installed, then run:
   ```bash
   pip install discord.py gTTS
   ```

2. **Install FFmpeg**  
   This bot uses FFmpeg to play audio. Download it here: https://ffmpeg.org/download.html  
   Make sure it's added to your system's PATH.

3. **Edit the bot token**  
   Open the Python script and replace `'YOUR_BOT_TOKEN'` with your actual bot token.

4. **Run the bot**
   ```bash
   python your_script_name.py
   ```

## Notes

- The bot only listens to messages in a channel called `sergio`. You can change the `TARGET_TEXT_CHANNEL_NAME` in the script if needed.
- Likewise, it only joins a voice channel named `general`.
- The bot does not disconnect from the voice channel by default — you can uncomment the `disconnect` line if you want it to leave after each message.
