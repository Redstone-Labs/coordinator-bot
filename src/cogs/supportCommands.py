from nextcord.ext import commands
from dotenv import load_dotenv
from utils.embedBuilder import makeEmbed
import nextcord
import os


class SupportCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        load_dotenv()
    @nextcord.slash_command(name='projects', description='Discover our projects & repositories on Github.', guild_ids=[int(os.getenv('GUILD_ID'))])
    async def projects(self, interaction, user: nextcord.Member = nextcord.SlashOption(description='(Optional) Mention a user', required=False)): # /projects command
        print(interaction.message)
        await interaction.send(embed=makeEmbed("Our Github", 
                                               "All of our code is public and listed on **Github**. Find out more by checking out the links below:\n\
                                               - [Redstone Labs Organization](https://github.com/Redstone-Labs)\n\
                                                    - [React](https://github.com/Redstone-Labs/react) - Fun, quick-paced, chat minigames designed to keep players engaged in the server.\
                                                \n\n\
                                                **Note:** To download plugins for your server, please go to the respective repository and head to the *releases* category on the right hand side menu."),\
                                                content=f'<@{user.id}>' if user else None)    

    @nextcord.slash_command(name='when', description='When will x feature/project be released?', guild_ids=[int(os.getenv('GUILD_ID'))])
    async def when(self, interaction, user: nextcord.Member = nextcord.SlashOption(description='(Optional) Mention a user.', required=False)): # /when command
        await interaction.send(embed=makeEmbed("When is x feature coming?",
                                               "Our development team is consisted of volunteers who do not get paid for the time and effort put into this project. \
                                                That being said, we do not enforce deadlines on any of our work. We try to get thigns done as fast as possible for your own convenience, but please take into \
                                                consideration that we are all busy with life things outside of this. Rest assured that we dilligently working to deliver quality \
                                                products for you to use."), content=f'<@{user.id}>' if user else None) 

async def setup(bot):
    load_dotenv()
    bot.add_cog(SupportCommands(bot))