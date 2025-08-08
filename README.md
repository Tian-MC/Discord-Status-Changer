# Discord Status Auto-Changer 🤖

Automatically change your Discord custom status message every 24 hours (or custom interval) by reading phrases from a text file.

> ⚠️ **WARNING**: This script uses your personal Discord account token and may violate Discord's Terms of Service. Use at your own risk. Account suspension is possible.

## Features ✨

- 🔄 **Automatic Status Rotation**: Changes your custom status every 24 hours
- 📝 **Custom Phrases**: Reads phrases line-by-line from `phrases.txt`
- ⏰ **Flexible Intervals**: 24h normal mode, 30s test mode, or custom intervals
- 🔒 **Secure Token Storage**: Uses `.env` file for token management
- 📊 **Logging**: Full logging with timestamps and error handling
- 🔧 **Easy Setup**: Automatic file creation and user guidance
- 🔄 **Live Reload**: Automatically reloads phrases file every cycle

## Installation 🚀

1. **Clone the repository**
```bash
git clone https://github.com/tian-mc/discord-status-changer
cd discord-status-changer
```

2. **Install dependencies**
```bash
pip install python-dotenv requests
```

3. **Create your phrases file** (`phrases.txt`).
   e.g.
```
🎮 Gaming time
📚 Studying hard  
🎵 Vibing to music
☕ Coffee and coding
💻 Building something cool
🌙 Night owl mode
🚀 Exploring new worlds
🎨 Being creative
```

4. **Get your Discord token**
   - Open Discord in your **browser** (not desktop app)
   - Press `F12` → go to `Network` tab
   - Refresh the page (`F5`)
   - Write something in any chat do you have
   - Click on `typing` → find `authorization`
   - Copy the token value.

5. **Create `.env` file**
```env
DISCORD_USER_TOKEN=your_token_here
```

6. **Run the script**
```bash
python main.py
```

## Usage 💡

When you run the script, you'll see:

```
🤖 Discord Status Auto-Changer
⚠️  This script may violate Discord ToS!
==================================================

Choose interval:
1. Normal (every 24 hours)
2. Test (every 30 seconds) 
3. Custom

Enter 1, 2 or 3:
```

### Modes

- **Normal Mode** (24 hours): Perfect for daily status rotation
- **Test Mode** (30 seconds): Great for testing your phrases quickly
- **Custom Mode**: Set your own interval (minimum 30 seconds)

## File Structure 📁

```
discord-status-changer/
├── main.py          # Main script
└── README.md              # This file
```

## Security & Privacy 🔒

- ✅ Token stored in `.env` file (not in code)
- ✅ No data sent to external servers
- ✅ Uses Discord's official API endpoints
- ⚠️ Your token grants full account access - keep it secret!

## Troubleshooting 🔧

### Common Issues

**"Token not found in .env"**
- Make sure `.env` file exists in the same directory as the script
- Check that the file contains: `DISCORD_USER_TOKEN=your_token`
- Ensure no extra spaces around the `=` sign

**"Connection failed"**
- Verify your token is correct and not expired
- Make sure you copied the full token (they're quite long)
- Try getting a fresh token from Discord

**"Module not found"**
```bash
pip install python-dotenv requests
```

**"Status not changing"**
- Check the console for error messages
- Verify `phrases.txt` exists and contains phrases
- Make sure phrases aren't empty lines

### Getting a Fresh Token

If your token stops working:
1. Open Discord in browser
2. Log out and log back in
3. Repeat the token extraction process
4. Update your `.env` file

## Legal Disclaimer ⚖️

This tool is for educational purposes only. Using automation with your Discord account may violate Discord's Terms of Service and could result in account suspension or termination. 

**Use at your own risk.** The author is not responsible for any consequences of using this software.

## Changelog 📋

### v1.0.0
- Initial release
- Basic status changing functionality
- .env token support
- Multiple interval modes
- Automatic file creation
- Comprehensive logging

---

**⭐ Star this repo if you like it!**

Made with ❤️ for Discord users who want dynamic status messages.
