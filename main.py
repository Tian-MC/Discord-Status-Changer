"""
Discord Status Changer - Direct HTTP Version
WARNING: This script changes the status of YOUR Discord account.
Use at your own risk!
"""

import requests
import time
import json
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DiscordStatusChanger:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.phrases = []
        self.current_index = 0
        self.load_phrases()
    
    def load_phrases(self):
        """Load phrases from phrases.txt file"""
        try:
            with open('phrases.txt', 'r', encoding='utf-8') as file:
                self.phrases = [line.strip() for line in file.readlines() if line.strip()]
            
            if not self.phrases:
                raise ValueError("phrases.txt file is empty!")
                
            logger.info(f"Loaded {len(self.phrases)} phrases from file")
            
        except FileNotFoundError:
            logger.error("phrases.txt file not found! Creating a sample file...")
            self.create_sample_file()
            
        except Exception as e:
            logger.error(f"Error loading phrases: {e}")
            self.phrases = ["Default status"]
    
    def create_sample_file(self):
        """Create a sample file if it does not exist"""
        sample_phrases = [
            "Gaming time",
            "Studying hard", 
            "Vibing to music",
            "Coffee and relax",
            "Coding session",
            "Night owl mode",
            "Exploring new worlds",
            "Being creative"
        ]
        
        with open('phrases.txt', 'w', encoding='utf-8') as file:
            for phrase in sample_phrases:
                file.write(phrase + '\n')
        
        self.phrases = sample_phrases
        logger.info("Sample phrases.txt file created")
    
    def test_connection(self):
        """Test if the token works"""
        try:
            response = requests.get(
                'https://discord.com/api/v9/users/@me',
                headers=self.headers
            )
            
            if response.status_code == 200:
                data = response.json()
                username = data.get('username', 'Unknown')
                logger.info(f"Connection successful! User: {username}")
                print(f"Connected as: {username}")
                return True
            else:
                logger.error(f"Connection error: {response.status_code}")
                print(f"Error: {response.status_code} - Invalid token?")
                return False
                
        except Exception as e:
            logger.error(f"Network error: {e}")
            print(f"Connection error: {e}")
            return False
    
    def change_status(self):
        """Change the custom status"""
        if not self.phrases:
            logger.warning("No phrases available!")
            return False
            
        current_phrase = self.phrases[self.current_index]
        
        # Payload to change the custom status
        payload = {
            "custom_status": {
                "text": current_phrase,
                "expires_at": None,
                "emoji_id": None,
                "emoji_name": None
            }
        }
        
        try:
            response = requests.patch(
                'https://discord.com/api/v9/users/@me/settings',
                headers=self.headers,
                data=json.dumps(payload)
            )
            
            if response.status_code == 200:
                logger.info(f"Status changed: '{current_phrase}' ({self.current_index + 1}/{len(self.phrases)})")
                print(f"New status: {current_phrase}")
                
                # Move to the next phrase
                self.current_index = (self.current_index + 1) % len(self.phrases)
                return True
            else:
                logger.error(f"Status change error: {response.status_code}")
                print(f"Error: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"Error changing status: {e}")
            print(f"Error: {e}")
            return False
    
    def status_change_loop(self, interval_hours=24):
        """Main loop to change status"""
        print(f"Starting status change loop every {interval_hours} hours...")
        
        # First change immediately
        self.change_status()
        
        while True:
            try:
                interval_seconds = interval_hours * 3600
                print(f"Next status change: {datetime.now().strftime('%H:%M:%S')} + {interval_hours}h")
                
                # Wait for the specified interval
                time.sleep(interval_seconds)
                
                # Reload phrases (for live file changes)
                self.load_phrases()
                
                # Change status
                self.change_status()
                
            except KeyboardInterrupt:
                print("\nStopped by user")
                break
            except Exception as e:
                logger.error(f"Error in loop: {e}")
                print("Error in loop, retrying in 1 minute...")
                time.sleep(60)

def get_token():
    """Get the token from the .env file"""
    
    # Try to load from .env
    token = os.getenv('DISCORD_USER_TOKEN')
    
    if token and token != 'YOUR_USER_TOKEN':
        logger.info("Token loaded from .env file")
        return token
    
    # If not found, check if .env file exists
    if not os.path.exists('.env'):
        print("\n" + "="*60)
        print("ERROR: .env FILE NOT FOUND!")
        print("="*60)
        print("\nCreate a file named '.env' in the same folder as the script")
        print("and add this line:")
        print("\nDISCORD_USER_TOKEN=your_token_here")
        print("\n" + "="*60)
        print("How to get the token:")
        print("1. Open Discord in your BROWSER (not the app)")
        print("2. Press F12 → go to 'Network'")
        print("3. Reload the page (F5)")
        print("4. Look for 'api/v9' requests → Headers → 'authorization'")
        print("5. Copy the value into the .env file")
        print("\nWARNING: The token is PRIVATE - do not share it!")
        print("="*60)
        
        # Offer to create a sample .env file
        answer = input("\nDo you want to create a sample .env file? (y/n): ").lower()
        if answer in ['y', 'yes']:
            create_sample_env()
        
        return None
    
    print("Token not found in .env file!")
    print("Make sure the .env file contains:")
    print("DISCORD_USER_TOKEN=your_token")
    return None

def create_sample_env():
    """Create a sample .env file"""
    env_content = """# Discord Status Changer configuration file
# Replace 'your_token_here' with your real Discord token

DISCORD_USER_TOKEN=your_token_here

# The token often starts with 'mfa.' followed by random characters
# DO NOT share this file with anyone!
"""
    
    try:
        with open('.env', 'w', encoding='utf-8') as file:
            file.write(env_content)
        print("Sample .env file created!")
        print("Edit the .env file and enter your token")
    except Exception as e:
        print(f"Error creating .env file: {e}")

def main():
    """Main function"""
    print("Discord Status Auto-Changer")
    print("WARNING: This script may violate Discord's ToS!")
    print("="*50)
    
    # Get the token
    token = get_token()
    if not token:
        return
    
    # Create the changer instance
    changer = DiscordStatusChanger(token)
    
    # Test the connection
    if not changer.test_connection():
        print("Unable to connect. Check your token!")
        return
    
    # Ask for the interval
    print("\nChoose interval:")
    print("1. Normal (every 24 hours)")
    print("2. Test (every 30 seconds)")
    print("3. Custom")
    
    choice = input("\nEnter 1, 2 or 3: ").strip()
    
    if choice == "2":
        interval = 30/3600  # 30 seconds converted to hours
        print("\nTest mode enabled (30 seconds)")
    elif choice == "3":
        try:
            hours = float(input("Enter interval in hours (e.g. 0.5 for 30 min): "))
            interval = max(hours, 0.008)  # Minimum 30 seconds
            print(f"\nCustom mode ({hours} hours)")
        except:
            print("Invalid value, using 24 hours")
            interval = 24
    else:
        interval = 24
        print("\nNormal mode enabled (24 hours)")
    
    # Start the loop
    try:
        changer.status_change_loop(interval)
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()