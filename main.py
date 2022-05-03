import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "حزين"]

sya7 = ["sya7", "صياح", "tired", "ارهاق"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person/bot!"]

if "responding" not in db.keys():
  db["responding"] = True

banned_words = ["kosomak", "Kosomak", "كسمك", "كسم", "kosom", "Kosom"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_video(video_search):
    tmp = video_search.split()
    name = tmp[0]
    for i in tmp[1:]:
        name += ("+" + i)
    response = requests.get("https://www.youtube.com/results?search_query=" + name)
    first_vid_location = str(response.content).split("watch?", 1)[1]
    first_vid_path_url = first_vid_location.split("\"", 1)[0]

    return "https://www.youtube.com/watch?" + first_vid_path_url
  

def update_encouragements(encouraging_msg):
  if "encouragements" in db.keys():
    encouragements = list(db["encouragements"])
    encouragements.append(encouraging_msg)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_msg]

def update_banned(banned_msg):
  if "banned" in db.keys():
    encouragements = db["banned"]
    encouragements.append(banned_msg)
    db["banned"] = encouragements
  else:
    db["banned"] = [banned_msg]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    await message.channel.send(get_quote())

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])
  
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if any(word in msg for word in sya7):
    await message.channel.send("كوكو كوكو كوكو")

  if msg.startswith('$new'):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith('$del'):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del ",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
      await message.channel.send(encouragements)
    else:
      await message.channel.send("There's no encouragements that exitst")

  if any(word in msg for word in banned_words):
    await message.author.kick()

  if msg.startswith('$list'):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = list(db["encouragements"])
      await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off")

  if msg.startswith("$yt"):
    value = msg.split("$yt ", 1)[1]
    await message.channel.send(get_video(value.lower()))
    
keep_alive()
client.run(os.environ['TOKEN'])