import discord
import asyncio
import requests
import os


TOKEN = os.environ.get('TOKEN')
MINSWAP_URL = "https://api-mainnet-prod.minswap.org/coinmarketcap/v2/pairs"
MINSWAP_ID = os.environ.get('MINSWAP_ID')
bot = discord.Client()
        
@bot.event
async def dex_data(member):
    await bot.wait_until_ready() # ensures cache is loaded
    # while loop to continuously keep the price updating
    # every 5 minutes
    while not bot.is_closed():
        r = requests.get(MINSWAP_URL)
        output = r.json()
        await member.edit(nick=f"VNM: ${output[MINSWAP_ID]['last_price'][0:7]}")
        await asyncio.sleep(300) # or 300 if you wish for it to be 5 minutes

@bot.event
async def on_ready():
    try:
        print("Logged in as: ")
        print(str(bot.user.id))
        print(str(bot.user.name))
        print(bot.guilds)
        mem_obj = ""
        for guild in bot.guilds:
            for member in guild.members:
                mem_obj = member
                # This loop is a built in function
                # that allows us to use asycnio coroutines
                # very easily #magic
        await bot.loop.create_task(await dex_data(mem_obj))
        print('------')
    except Exception as e:
        print("Error Crawling Stats for Today: "+f"Exception:{e}")
    finally:
        await bot.close()

bot.run(TOKEN)