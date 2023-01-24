import discord
from discord.commands import slash_command, Option
from discord.ext.commands import Cog

from random import choice
import requests
import json


with open("./data/guild_ids.txt", "r") as r:
    guild_ids = [int(guild_id) for guild_id in f.read().strip().split(',')]


class Jokes(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=guild_ids, description="Get a random dad joke", name="joke")
    async def post_joke(self, ctx, keyword: Option(str, "Search for a joke by keyword.", required=False, default=None)):
        if keyword:
            request_string = f"https://icanhazdadjoke.com/search?term={keyword}"
        else:
            request_string = f"https://icanhazdadjoke.com/"

        result = json.loads(requests.get(request_string,
                                         headers={'User-Agent': 'https://github.com/hthrfong/royboy-a-discord-bot', 'Accept': 'application/json'}).text)

        try:
            joke = result['joke']
        except KeyError:
            joke = choice(result['results'])['joke']

        await ctx.respond(joke)
