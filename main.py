from os import getenv
from dotenv import load_dotenv
from uvloop import install
from pyrogram import Client, filters
#from pyrogram.types import ReplyKeyboardMarkup
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
install()

app = Client(
    'pedrohilan_bot',
    api_id=getenv("TELEGRAM_API_ID"),
    api_hash=getenv("TELEGRAM_API_HASH"),
    bot_token=getenv("TELEGRAM_BOT_TOKEN")
)

scopes = ['https://spreadsheets.google.com/feeds']
json_creds = getenv("GOOGLE_SHEETS_CREDS_JSON")

creds_dict = json.loads(json_creds)
creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
client = gspread.authorize(creds)

# Find a workbook by url
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1TmPohMBPI2bsxYsWs7p9mv19FOiUH6NnzRNJbXSc3Q4/edit#gid=16028244")
sheet = spreadsheet.sheet1

@app.on_message(filters.command('iniciar'))
async def start(client, message):
    await message.reply("Digite o comando '/últimos' para os 5 últimos registros da ficha de encaminhamento Google")

@app.on_message(filters.command('últimos'))
async def last(client, message):
    
    # Extract and print all of the values
    rows = sheet.get_all_records()
    msg = ''
    for i in range(1,6):
        msg += "**Adolescente/Jovem** : "+rows[-i]['Nome do(a) Adolescente/Jovem']+"\n** Enviado em:** "+rows[-i]['Carimbo de data/hora']+"\n\n"
    
    await message.reply(msg)

app.run()