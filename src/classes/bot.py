import discord
from discord.ext import commands
import datetime

class Bot(commands.AutoShardedBot):
    def __init__(self, **kwargs: object) -> object:
        super().__init__(**kwargs)
        self.starttime = datetime.datetime.now()
        self.version = "0.0.1"

    @property
    def uptime(self):
        return datetime.datetime.now() - self.starttime