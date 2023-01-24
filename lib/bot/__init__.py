import discord
import asyncio
from glob import glob
from discord.ext.commands import Bot as BotBase
import os
from dotenv import load_dotenv

OWNER_IDS = [268862253326008322, 166790627856613376]
COGS = [path.split("/")[-1][:-3] for path in glob("./lib/cogs/*.py")]
load_dotenv()


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

    
class Bot(BotBase):
    def __init__(self):
        self.command_prefix = "!"
        
        self.ready = False
        self.cogs_read = Ready()

        super().__init__(command_fix=self.command_prefix,
                         owner_ids=OWNER_IDS,
                         intents=discord.Intents().all())

    def setup(self):
        for cogs in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog loaded")
        print("setup complete")

    def run(self):
        print("running setup...")
        self.setup()

        self.TOKEN = os.getenv("DISCORD_TOKEN")
        
        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_ready(self):
        if not self.ready:
            while not self.cogs_ready.all_ready():
                print("not ready")
                await asyncio.sleep(0.5)

            self.ready = True
            print("bot logged in as {0.user}".format(self))

        else:
            print("bot reconnected")


bot = Bot()
