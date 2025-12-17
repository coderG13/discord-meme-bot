# Discord Meme Bot 🤖

A Python Discord bot that responds to the `$meme` command with random memes from Reddit.

![Discord Meme Bot Demo](assets/demo-working.png)

## Features

- 🎭 Fetches random memes from Reddit using the [Meme API](https://github.com/D3vd/Meme_Api)
- 💬 Responds to `$meme` command in Discord channels
- 🔄 Built with discord.py and asynchronous event handling
- 🚀 Easy to set up and deploy

## Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- pip (Python package installer)
- A Discord account
- A Discord server with "Manage Server" permissions

## Setup Instructions

### 1. Clone or Download This Project

```bash
git clone <your-repo-url>
cd discord-meme-bot
```

### 2. Install Dependencies

**On macOS/Linux:**
```bash
python3 -m pip install -r requirements.txt
```

**On Windows:**
```bash
py -3 -m pip install -r requirements.txt
```

### 3. Create Your Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "MemeBot")
3. Navigate to the "Bot" tab in the left panel
4. Click "Add Bot"
5. Under the bot settings, click "Reset Token" and copy your bot token
6. **Important:** Scroll down to "Privileged Gateway Intents" and enable "Message Content Intent"

### 4. Configure Your Bot Token

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in a text editor and replace `your_bot_token_here` with your actual bot token:
   ```
   DISCORD_TOKEN=your_actual_token_here
   ```

**Security Note:** The `.env` file is already in `.gitignore` and will NOT be uploaded to GitHub. Never share your bot token publicly!

### 5. Invite Bot to Your Server

1. In the Developer Portal, go to "OAuth2" → "URL Generator"
2. Select scopes: `bot`
3. Select bot permissions: `Send Messages`, `Read Messages/View Channels`
4. Copy the generated URL and paste it in your browser
5. Select your server and authorize the bot

### 6. Run the Bot

**On macOS/Linux:**
```bash
python3 bot.py
```

**On Windows:**
```bash
py -3 bot.py
```

You should see: `Logged on as MemeBot#XXXX!`

## Usage

Once the bot is running and in your server:

1. Go to any channel where the bot has access
2. Type `$meme`
3. The bot will respond with a random meme from Reddit!

## How It Works

The bot uses:
- **discord.py**: A Python wrapper for the Discord API that handles events and messaging
- **Meme API**: A free REST API that returns random memes from Reddit in JSON format
- **Asynchronous Programming**: Event-driven architecture to respond to Discord messages

### Code Structure

- `get_meme()`: Fetches a random meme URL from the Meme API
- `on_ready()`: Event handler called when the bot successfully logs in
- `on_message()`: Event handler called when any message is sent in channels the bot can see
- `MyClient`: Custom Discord client class that extends `discord.Client`

## Customization Ideas

- Add more commands (e.g., `$joke`, `$quote`)
- Filter memes by subreddit: `https://meme-api.com/gimme/{subreddit}`
- Add error handling for API failures
- Implement cooldowns to prevent spam
- Add reactions to messages

## Troubleshooting

**Bot doesn't respond to messages:**
- Make sure "Message Content Intent" is enabled in the Developer Portal
- Verify the bot has permission to read and send messages in the channel
- Check that `intents.message_content = True` is set in the code

**Import errors:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check your Python version: `python3 --version`

**Bot goes offline:**
- The bot only runs while the script is running
- Keep the terminal window open, or deploy to a cloud service for 24/7 uptime

## License

This project is open source and available for educational purposes.

## Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Meme API Documentation](https://github.com/D3vd/Meme_Api)

---

**Note:** Keep your bot token secure and never share it publicly!
