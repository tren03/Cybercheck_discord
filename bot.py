import discord
import requests
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

VIRUSTOTAL_API_KEY = '55edafdf1a535b5e81f348cb6c27a3c43bc37f38b091ae6cb72229a401ff6aeb'
MALICIOUS_THRESHOLD = 2
REACTION_EMOJI = '⚠️'

def check_maliciousness(url):
    params = {
        'apikey': VIRUSTOTAL_API_KEY,
        'resource': url
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params, headers=headers)
    result = response.json()

    if result['response_code'] == 1:
        positive_engines = result['positives']
        if positive_engines >= MALICIOUS_THRESHOLD:
            return True

    return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
    for url in urls:
        is_malicious = check_maliciousness(url)
        if is_malicious:
            
            await message.channel.send(f'⚠️ @{message.author.name}, your message contained a malicious link. We advise you not to open it')
            await message.add_reaction(REACTION_EMOJI)
            break

client.run('MTEyNDczODk4MzA4NDE4MzYxMw.GaoBQ6.pZ_E6qTpFjflPvhbAaoC4dTyETNHy7I8S-UkUg')

