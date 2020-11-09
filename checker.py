from bs4 import BeautifulSoup
import re
import os

import discord
from dotenv import load_dotenv
import requests
import time

from selenium import webdriver


def check_button():
    driver = webdriver.Chrome()
    urls = ['https://www.walmart.ca/en/ip/samsung-32-curved-monitor-1920x10804ms60hz-lc32f391fwnxza/PRD27A2X308ONR2']
    driver.get(urls[0])
    time.sleep(5)
    page_source = driver.page_source

    v = driver.find_element_by_css_selector(
        "button.css-1i45fk4")
    v.click()
    print(v)
    print(v.is_enabled())

    return [v.is_enabled()]


def parse_file():
    f = open("urls.txt")
    lines = f.readlines()
    print(lines)
    for line in lines:
        split = line.split(",")
        print(split)
    print(f)


GUILD = os.getenv('DISCORD_GUILD')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
client = discord.Client()


@client.event
async def on_ready():
    channel = client.guilds[0].text_channels[0]
    print(check_button())
    if(check_button()):

        await channel.send("https://www.walmart.ca/en/ip/samsung-32-curved-monitor-1920x10804ms60hz-lc32f391fwnxza/PRD27A2X308ONR2")
    print(client.guilds[0].channels)
    print(f'{client.user} has connected to Discord!')

# client.run(TOKEN)
parse_file()
