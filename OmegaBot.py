import discord
from discord.ext.commands import Bot
from discord.ext import commands

adminid = "421722865369612288"

client = discord.Client()
bot_prefix= ""
client = commands.Bot (commands_prefix=bot_prefix)

@clien.event
async def on_reay() :
    print("Bot Online")
	print("Name: ()".format(clien.user.name))
	print("ID: ()".format(client.user.id))

@client.event
async def on_member_join(member):
	serverchannel = member.server.default_channel
	msg =  "Wilkommen, [0] auf dem Server [1]!".format(member.mention, member.derver.name)
    await client.send_message(serverchannel, msg)
	
@client.event
async def on_member_remove(member)
serverchannel = member.server.default_channel
	leave_msg =  "Tschüss, [0] war eine tolle Zeit, mit dir!".format(member.mention)
    await client.send_message(serverchannel, leave_msg)

@clien.command(pass_context=True)
async def -help(ctx):
    await client.say("Meine Commands sind
	-help      Zeigt dir alle Commands ich ich habe
	-ping      Ich sage Pong (XD)
	-dev       Zeigt Namen meines DevelopersNamen meines Developers!")
	
	async def -ping(ctx):
    await client.say("Pong")
	
		async def -dev(ctx):
    await client.say("Der Name meines Developers lautet... OmegaholzYT!")
	
    if message.content.startwith("-game") and message.author.id == adminid:
	    game = message.content[6:]
		await client.change.preasence(game=discord.Game(name=mit Developern))
		await client.send_message(message.channel, "Ich habe meinen Status zu " + game +" geändert")
	
client.run("NDE0NTMwNTc5OTQ2Nzk5MTE0.DYRTkg.Dwr5z1EgHNqd-CLq-wXlaPavrPs")
