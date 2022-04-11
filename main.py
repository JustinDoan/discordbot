import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is now running! Logged in as: {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ping"):
        await message.channel.send("Pong!")


# Start Bot
with open("token.txt", "r") as f:
    token = f.read()

client.run(token)
