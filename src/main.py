import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.bot import when_mentioned_or
import random

api_key = 'API key replaced :3'
bot_prefixes = ['dora ', 'Dora ', 'dora', 'Dora']
greet_strings = ['Hello {0}!', 'Hey {0}!',
                 'o/ {0}', 'oi {0}', 'Yo {0}!', "Hi {0}!"]

gaali_strings_hindi = ['string1', 'string2', 'string3']

roast_strings = ['{0} is what the result of a broken rubber balloon looks like',
                 'Kids, study well if you dont want to end up like {0}!',
                 'Too bad, you can\'t photoshop an ugly personality (like yours), {0}']

use_help_string = 'Type \'dora help\' to get a list of stuff I can do!'

help_string = 'Say hi and I\'ll reply to you!\n' + \
              '\"dora gaali de\" to see some Hindi gaalis\n' + \
              '\"dora roast <@user>\" to roast someone'

reply_greet_strings = [greeting.replace('{0}', '').replace('!', '').strip().lower()
                       for greeting in greet_strings]

muted = []

owner_id = 'OWNER_ID_PLACEHOLDER'

print("Starting Doracake...")

bot = discord.ext.commands.Bot(command_prefix=(when_mentioned_or(*bot_prefixes)),
                               description=use_help_string,
                               help_command=None,
                               case_insensitive=True)


@bot.event
async def on_ready():
    print('Logged in as user {0}'.format(bot.user))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("dora help"))


@bot.event
async def on_message(message):

    # Check if the message was not sent by a bot
    # if(True):

    if(muted.__contains__(message.author.id)):
        await message.delete()

    if (not message.author.bot):

        message_first_word = message.content.split(' ')[0].lower()

        # Check if the first word of the input is a string from reply_greet_strings
        if (message_first_word.startswith(tuple(reply_greet_strings)) and
                len(message.content) > 1):

            # Check if there's a space, and hence more than one word
            if (message.content.count(' ') > 0):

                # Reply to the author of the message, only if the second word (the one immediately after hi
                # is the bot prefix)
                if (message.content.split(' ')[1].lower().startswith(tuple(bot_prefixes))):
                    await message.channel.send(random.choice(greet_strings)
                                               .format('<@'+str(message.author.id)+'>'))
            else:
                await message.channel.send(random.choice(greet_strings)
                                           .format('<@'+str(message.author.id)+'>'))

        elif(message_first_word == 'f'):
            await message.channel.send('F')

        elif(message_first_word == 'oof'):
            await message.channel.send('big oof')

        elif(message_first_word == 'xd'):
            await message.channel.send('lmao')

        elif(message_first_word == 'lol'):
            await message.channel.send('LOL xD')

        elif(message_first_word == 'lmao'):
            await message.channel.send('looooooooool')

    await bot.process_commands(message)


@bot.command(case_insensitive=True)  # dora gaali de
async def gaali(ctx, *args):
    if(len(args) > 0 and args[0].lower() == 'de'):
        await ctx.message.channel.send(random.choice(gaali_strings_hindi))
    else:
        await ctx.message.channel.send('AHEM, gaali khayega tu <@{0}>'.
                                       format(ctx.message.author.id))


@ bot.command(case_insensitve=True)  # dora roast <@person>
async def roast(ctx, *args):
    if (not len(args) > 0):
        await ctx.message.channel.send(random.choice(roast_strings).
                                       format('<@'+str(ctx.message.author.id)+'>'))
        return

    if (args[0] == "@here" or args[0] == "@everyone"):
        await ctx.message.channel.send('Nope. you cannot tag everyone/here. Not happening today.')
        return

    try:
        await ctx.message.channel.send(random.choice(roast_strings).
                                       format('<@'+str(args[0].id)+'>'))
    except:
        await ctx.message.channel.send('Tag someone next time, bruh')


@ bot.command(aliases=reply_greet_strings)
async def greet(ctx, *args):
    if(len(args) > 0):
        if(args[0] != "@everyone" and args[0] != "@here"):
            try:
                await ctx.message.channel.send(random.choice(greet_strings)
                                               .format(args[0]))
            except:
                await ctx.message.channel.send(random.choice(greet_strings)
                                               .format('<@'+str(ctx.message.author.id)+'>'))

    else:
        await ctx.message.channel.send(random.choice(greet_strings)
                                       .format('<@'+str(ctx.message.author.id)+'>'))


@ bot.command()
async def command_not_found(ctx):
    await ctx.message.channel.send('Unknown command! Try \'dora help\'')


@ bot.command()
async def mute(ctx, user: discord.User):
    print(muted)

    try:
        if (user.id == owner_id):
            return
        muted.append(user.id)
    except:
        await ctx.message.channel.send('Tag someone properly next time.')

    await ctx.message.delete()
    print(muted)


@ bot.command()
async def fork(ctx, user: discord.User):
    try:
        if (user.id == owner_id):
            return
        muted.remove(user.id)
    except:
        await ctx.message.channel.send('Tag someone properly next time.')

    await ctx.message.delete()
    print(muted)

bot.run(api_key)
