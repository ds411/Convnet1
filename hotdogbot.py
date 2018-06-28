import discord
from discord.ext.commands import Bot
from discord.ext import commands
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import asyncio
import requests
from io import BytesIO

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

TOKEN = 'NDYyMDE4NTY2NTA2NDE0MDgw.Dhb5Gg.UImNIOirm9SRtNfi-YltSN_4BFo'

model = load_model('hotdogmodel.h5')

@Client.event
async def on_ready():
    print('running...')
    
@Client.event
async def on_message(message):
    if(message.content.startswith('!hotdog')):
        await Client.send_message(message.channel, 'received')
        attachments = message.attachments
        print(attachments)
        i = 0
        for a in attachments:
            i += 1
            url = a['url']
            try:
                response = requests.get(url)
                im = Image.open(BytesIO(response.content))
                im = im.resize((100, 100), Image.NEAREST)
                im.save("checkdog.jpg")
                x = load_img('checkdog.jpg',False,target_size=(100, 100))
                x = np.expand_dims(x, axis=0)
                preds = model.predict_classes(x)
                probs = model.predict_proba(x)
                if(preds[0] == 0):
                    await Client.send_message(message.channel, "I believe that attachment " + str(i) + " is not a hot dog.")
                elif(preds[0] == 1):
                    await Client.send_message(message.channel, "I believe that attachment " + str(i) + " is a hot dog.")
            except IOError:
                await Client.send_message(message.channel, "Attachment " + str(i) + " is not a valid image.")
                
Client.run(TOKEN)