# coordinator-bot
A simple and functional Discord bot used In the Redstone Labs Discord server.

## How to fork the project
Please read [CONTRIBUTING.MD](https://github.com/Redstone-Labs/.github/blob/main/CONTRIBUTING.MD) before submitting changes.

1. Fork the repository.
2. Create a venv (virtual environment) in the root folder using ``python3 -m venv .venv``
3. Add a .env file inside the root folder of the project with the following format:
```env
DISCORD_TOKEN= ... /* The token of your Discord bot */
GUILD_ID= ... /* The guild ID the bot will be registering slash commands in */
```
3. Download all the requirements.txt dependancies using ``pip3 install -r requirements.txt``

## Linting
A linter is already provided with the source code.

------

Written using the nextcord python library.
