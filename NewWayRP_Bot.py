#NewWayRP Bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import embeds
import random
import os
import asyncio

intents = discord.Intents.all()

#client = discord.Bot(intents = intents)
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="NewWayRP FiveM", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready")



@bot.event
async def on_member_join(member):
    #channel = bot.get_channel(856867016346828820)
    #await channel.edit(name = 'Member count: {}'.format(channel.guild.member_count))
    role = discord.utils.get(member.guild.roles, name = '�������')
    await member.add_roles(role)
    wellcome_table = discord.Embed (title="", url="https://realdrewdata.medium.com/", description="", color=0x2ecc71) 
    wellcome_table.set_author(name="�������������", url="", icon_url="")
    wellcome_table.set_thumbnail(url='https://blog.aci.aero/wp-content/uploads/2019/03/shutterstock_745544935-952x635.jpg')
    wellcome_table.add_field(name="� ���� ������ ���� �", value = "{}".format(random.randint(10000, 99990)), inline=False)
    wellcome_table.add_field(name="������� ���������� ��������� ������ ������ ", value = "{}".format(member), inline=False)
    wellcome_table.set_footer(text="NewWayRP AirLines")
    channel = bot.get_channel(856432895752404998)
    await channel.send(embed = wellcome_table)
    #await channel.send("{} joined to server! Role: {}".format(member, role.name))
    await  member.send("�� joined to server {}!  Role: {}".format(member.guild.name, role.name))
    print("{} joined to server! Role: {}".format(member, role.id))


      
      
@bot.event
#async def on_member_leave(member):
async def on_member_remove(member):
    print("leave to channel! ")
    #channel = bot.get_channel(856867016346828820)
    #print ('chan', channel)
    #await channel.edit(name = 'Member count: {}'.format(channel.guild.member_count))
    channel = bot.get_channel(856432895752404998)
    await channel.send("{} leave from server!".format(member.name))
    By_table = discord.Embed (title="", url="https://realdrewdata.medium.com/", description="", color=0xFF5733) 
    By_table.set_author(name="�������������", url="", icon_url="")
    By_table.set_thumbnail(url='https://img3.goodfon.ru/wallpaper/nbig/5/d8/art-samolet-polet-solnce-nebo.jpg')
    By_table.add_field(name="���� ���������� �������� ���� �", value = "{}".format(random.randint(10000, 99990)), inline=False)
    By_table.add_field(name="������� �������� ����� ��������� ", value = "{}".format(member), inline=False)
    By_table.set_footer(text="NewWayRP AirLines")
    await channel.send(embed = By_table)
    print("{} leave from server!".format(member))



# ���� �� ������� �������
@bot.event
#async def on_reaction_add(reaction, user):
async def on_raw_reaction_add(payload):
    message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
    #var_emoji = discord.utils.get(message.guild.emojis, name=':ballot_box_whith_check:')
    #reaction = discord.utils.get(message.reactions, emoji=var_emoji)
    #print (reaction, var_emoji, payload.emoji.name, payload.emoji.id, payload.emoji)
    user = payload.member
    ChID = 856820333473824770
    if message.id != ChID:
        return;
    else:
    #if payload.emoji == '??':
      print("done")
      role = discord.utils.get(user.guild.roles, name = '���� �����')
    #rol = discord.utils.get(guild.roles, name="���� �����")
      await user.add_roles(role)

#������� ��� ������ ������ �� ����� ���� � ��������� ����� �������       
@bot.command()
async def text (ctx, *, text):
    await ctx.send(f'{text}')
    await ctx.message.delete()


#bot.run('') 
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))

