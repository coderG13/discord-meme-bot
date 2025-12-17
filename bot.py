import discord
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_meme():
    """Fetches a random meme from Reddit using the Meme API."""
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        """Called when the bot successfully logs in."""
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        """Called when a message is sent in a channel the bot can see."""
        # Don't respond to ourselves
        if message.author == self.user:
            return
        
        # Respond to $meme command
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# Set up intents to allow the bot to read message content
intents = discord.Intents.default()
intents.message_content = True

# Create and run the client
client = MyClient(intents=intents)

# Get token from environment variable
token = os.getenv('DISCORD_TOKEN')
if not token:
    raise ValueError("DISCORD_TOKEN not found in environment variables. Please create a .env file with your token.")

client.run(token)
