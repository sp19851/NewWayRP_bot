#NewWayRP Bot
##import keep_alive
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import embeds
from typing import Union
import random

import asyncio
import traceback

intents = discord.Intents.all()
#client = discord.Bot(intents = intents)
bot = commands.Bot(command_prefix='!', intents = intents)


@bot.event 
async def on_ready():
    activity = discord.Game(name="NewWayRP FiveM", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    #await bot.change_presence(status=discord.Status.online)
    print("LocalBot is ready")

      
@bot.event 
async def on_member_join(member):
    #channel = bot.get_channel(856867016346828820)
    #await channel.edit(name = 'Member count: {}'.format(channel.guild.member_count))
    #role = discord.utils.get(member.guild.roles, name = 'Блудный сын')
    role = discord.utils.get(member.guild.roles, name = 'Пилигрим')
    await member.add_roles(role)
    wellcome_table = discord.Embed (title="", url="https://realdrewdata.medium.com/", description="", color=0x2ecc71) 
    wellcome_table.set_author(name="Бортпроводник", url="", icon_url="")
    wellcome_table.set_thumbnail(url='https://blog.aci.aero/wp-content/uploads/2019/03/shutterstock_745544935-952x635.jpg')
    wellcome_table.add_field(name="В штат прибыл рейс №", value = "{}".format(random.randint(10000, 99990)), inline=False)
    wellcome_table.add_field(name="Просьба пропустить пассажира бизнес класса  ", value = "{}".format(member), inline=False)
    wellcome_table.add_field(name="Ему нашару досталась роль  ", value = "пилигрим. Какой с него теперь спрос", inline=False)
    wellcome_table.set_footer(text="NewWayRP AirLines")
    channel = bot.get_channel(743753916574859345) 
    await channel.send(embed = wellcome_table)
    #await channel.send("{} joined to server! Role: {}".format(member, role.name))
    await  member.send("Вы присоединились к серверу {}!  Роль по умолчанию: {}. Что бы получить возможность просматривать больше каналов прочтите правила и поставте галочку.".format(member.guild.name, role.name))
    print("{} joined to server! Role: {}".format(member, role.id))

     
      
@bot.event 
#async def on_member_leave(member):
async def on_member_remove(member):
    print("leave to channel! ")
    channel = bot.get_channel(743753916574859345)
    await channel.send("{} leave from server!".format(member.name))
    By_table = discord.Embed (title="", url="https://realdrewdata.medium.com/", description="", color=0xFF5733) 
    By_table.set_author(name="Бортпроводник", url="", icon_url="")
    By_table.set_thumbnail(url='https://img3.goodfon.ru/wallpaper/nbig/5/d8/art-samolet-polet-solnce-nebo.jpg')
    By_table.add_field(name="Штат покидает рейс №", value = "{}".format(random.randint(10000, 99990)), inline=False)
    By_table.add_field(name="Просьба уступить место пассажиру ", value = "{}".format(member), inline=False)
    
    By_table.set_footer(text="NewWayRP AirLines")
    await channel.send(embed = By_table)
    print("{} leave from server!".format(member))


# Получение роли после нажатия эмоции пользователем под прочтением правил
channels = [857320946330763275, 854074059587059722]
@bot.event
async def on_raw_reaction_add(payload):
    chan = bot.get_channel(payload.channel_id)
    mess = await chan.fetch_message(payload.message_id)
    user1 = payload.member
    user2 = mess.author
    print (mess)
    user2 = mess.author
    adm = payload.member
    perms = adm.guild_permissions
    is_admin = perms.administrator
    print ('**', mess.id,chan.id)
    if not mess.id in channels and chan.id not in channels:
       return
    elif mess.id == channels[0]:
        print("work1")
        role = user1.guild.get_role(854001171542310942)
        await user1.add_roles(role)
    elif chan.id == channels[1] and is_admin:
        role = discord.utils.get(user2.guild.roles, name = 'Пилигрим')
        await user2.add_roles(role)
    else:
        return


# Команда написания текста от имени бота      
@bot.command()
async def text (ctx, *, text):
    await ctx.send(f'{text}')
    await ctx.message.delete()

#Получение именя по id 
@bot.command()
async def getuserbyid(ctx, userid: int): 
  await ctx.message.delete()
  _member = await ctx.guild.fetch_member(userid)
  await ctx.send("```id {} использует член сообщества {}/{}```".format(userid, _member, _member.nick))
  
@getuserbyid.error
async def getuserbyid_error(ctx, error):
  await ctx.send(error)

#Удаление сообщений
@bot.command()
async def clearmes(ctx, number):
  adm = ctx.message.author
  perms = adm.guild_permissions
  is_admin = perms.administrator
  if is_admin:
    number = int(number) #Converting the amount of messages to delete to an integer
    ch = ctx.message.channel
    deleted = await ch.purge(limit = number, check =  clearmes)
    await ch.send("```{} удалил {} сообщения(й)```".format(adm,len(deleted)))
  else:
    return

@clearmes.error
async def getuserbyid_error(ctx, error):
  await ctx.send(error)
  
  

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
