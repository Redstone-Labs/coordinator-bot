import nextcord

def makeEmbed(title, desc, r=None, g=None, b=None):
    return nextcord.Embed(
        title='Redstone Labs | ' + title,
        description=desc,
        color= nextcord.Color.from_rgb(r, g, b) if r and g and b else nextcord.Color.from_rgb(238, 61, 61)
    )