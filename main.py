import discord, asyncio, os
TOKEN = os.environ["DISCORD_TOKEN"]
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("凪、起きた。Same Game, Different Tomorrow.で待機中")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "凪" in message.content:
        await message.channel.send("……何？呼んだ？新しい部屋、なかなか良いじゃん")

client.run(TOKEN)
