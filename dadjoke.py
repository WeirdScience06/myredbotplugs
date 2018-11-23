import discord
from discord.ext import commands
import aiohttp
import json
import random
from random import randint
from random import choice


class Yourdadjoke:
    """It's time to get a random dadjoke"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def getdadjoke(self, ctx):
        """Here is your random DadJoke ..."""
        
        user = ctx.message.author
        page = randint(1,6)
        link = "http://api.scorpstuff.com/dadjokes.php".format(page)
        async with aiohttp.get(link) as m:
            result = await m.json()
            message = choice(result)
            dadjoke = discord.Embed(colour=user.colour)
            dadjoke.add_field(name="{}'s dadjoke!".format(user.display_name),value="{}".format(message["message"]))
            await self.bot.say(embed=dadjoke)

def setup(bot):
    bot.add_cog(DadJoke(bot))