# Cybercheck_discord
## Discord Malicious Link Checker
This Discord bot monitors messages for potentially malicious URLs using the VirusTotal API. If a URL is detected as malicious, the bot reacts to the message and sends a warning to the user.

## Configuration
Discord Bot Token: Replace '#DISCORD_BOT_TOKEN' with your Discord bot token in the client.run line.

VirusTotal API Key: Replace 'VIRUS_TOTAL_API_KEY' with your VirusTotal API key in the VIRUSTOTAL_API_KEY variable.

Malicious Threshold: Adjust the MALICIOUS_THRESHOLD variable to set the minimum number of antivirus engines flagging a URL as malicious.

## Usage
### Running the Bot:

Ensure you have Python installed.
Install required packages: pip install discord.py requests.
Run the script: python bot.py.
Integration with Discord:

Invite the bot to your server using the Discord Developer Portal.
Ensure the bot has the necessary permissions to read messages, send messages, and add reactions.
Monitoring Messages:

The bot will automatically check messages for URLs.
If a URL is flagged as malicious, the bot will send a warning message and add a reaction to the original message.
## Important Note
This bot relies on the VirusTotal API for URL scanning. Ensure you comply with VirusTotal's terms of service when using their API.
