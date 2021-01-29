# A Discord Bot Using Python

## Table of contents
* [General Info](#gen-info)
* [Libraries used](#libs-used)
* [Setup](#setup)
* [Resources](#resources)
* [Notes](#notes)

## General Info
* A Discord bot used to generate memes, play songs etc.
* The language used is Python -v 3.8.7

## Libraries used:
* discord.py -v 1.6.0 
* opencv-python -v 4.5.1.48
* requests -v 2.25.1
* python-dotenv -v 0.15.0

## Setup
* You must have python -v 3 and pip -v 3 installed in your system
* Link to install python: https://www.python.org/downloads/

* To install discord.py, opencv-python, python-dotenv and requests use: ``` $ pip install discord.py opencv-python python-dotenv requests ```

* To run this project:
```
$ cd ../discord_bot
$ python bot.py
```

## Resources
* Create basic discord bot: https://discordpy.readthedocs.io/en/latest/discord.html , https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ , https://realpython.com/how-to-make-a-discord-bot-python/

* discord.py docs : https://discordpy.readthedocs.io/en/latest/index.html


## Notes
* In last line of bot.py file in:
``` client.run(TOKEN) ```
  Replace TOKEN with your bot's Token
