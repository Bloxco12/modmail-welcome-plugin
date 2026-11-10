import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

WELCOME_CHANNEL_ID = 1559332120550178836

class WelcomePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel is None:
            return

        member_count = member.guild.member_count

        message_content = (
            f"Thank you for joining **<:tail:1531370296714461307> Air Canada Virtual**, {member.mention} ! "
            f"You're a part of our {member_count} members.\n\n"
            f"> We are dedicated to deliver an incredible flight experience for all our passengers and proudly *Fly the Flag* as **<:Staralliance:1547838369520820224> A Star Alliance Member**.\n\n"
            f"Struggling with anything? Simply DM <@1493358854044516493> and our Support Team will assist you!"
        )

        try:
            await channel.send(message_content)
        except discord.HTTPException:
            pass

async def setup(bot):
    await bot.add_cog(WelcomePlugin(bot))
