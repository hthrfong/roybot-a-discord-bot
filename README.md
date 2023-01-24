# RoyBot, a Discord bot
Malin's Discord bot

## To add RoyBot

### From Discord side
- Go to https://discord.com/developers/applications
- Click "New Application"
- Name the application (e.g. call it "RoyBot")
- On the left side menu, click "Bot"
- Click "Add Bot" and confirm
- On left side menu, click "OAuth2"
- Tick "bot"
- Copy the URL that appears below and paste into browser. A prompt will show up that allows you to add  RoyBot to your server. Select your server and click "Authorize".

### From command line side
- Make sure `python3` and `git` are installed
- Copy the RoyBot files to your directory of choice: 
```
git clone https://github.com/hthrfong/roybot-a-discord-bot.git
```
- On the left side menu of the Discord application page (https://discord.com/developers/applications), click "Bot" and click "Copy" to copy the token
- In `lib/bot/.env`, replace "TOKENGOESHERE" with the token you copied in the previous step. When you open `lib/bot/.env` in a text editor, it should look something like this (but with different numbers/letters):
```
DISCORD_TOKEN="NzA0OTcwNzUyNzQyNjUzOTYz.Xqk5ww.1U_-WdW4aeGWCNF7bOJkLAu_2TM"
```
- To activate the bot, run:
```
python3 launch.py
```
If everything works, RoyBot will appear as online on the server!
