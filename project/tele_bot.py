#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from io import BytesIO
from PIL import Image
import telebot
from fastapi import FastAPI, HTTPException
from test_score import test_score_with_wrong

# Initialize the Telegram Bot
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Initialize the FastAPI app
app = FastAPI()

# Directory to store student answers
base_dir = 'student_answers'
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Scores and wrongs
scores = {}
wrongs = [0] * 10

# Handler for /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Automatic Test Checking Bot! Send me an image of your test to get started.")

# Handler for photo messages
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    chat_id = message.chat.id
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    img = Image.open(BytesIO(downloaded_file))
    student_name = f'student_{message.from_user.id}'
    img_path = os.path.join(base_dir, f'{student_name}.png')
    img.save(img_path)

    score, wrong = test_score_with_wrong(img_path)  # You need to implement this function
    scores[student_name] = score
    update_wrongs(wrong)

    bot.reply_to(message, f"Test received! Your score is: {score}")

# Handler for /list command
@bot.message_handler(commands=['list'])
def list_students(message):
    response = "Student List:\n" + "\n".join(scores.keys())
    bot.reply_to(message, response)

# Handler for /scores command
@bot.message_handler(commands=['scores'])
def show_scores(message):
    response = "Scores:\n" + "\n".join(f"{student}: {score}" for student, score in scores.items())
    bot.reply_to(message, response)

# Handler for /analysis command
@bot.message_handler(commands=['analysis'])
def test_analysis(message):
    average_score = round(sum(scores.values()) / len(scores), 1) if scores else 0
    response = f"Average Score: {average_score}\nError Statistics: {wrongs}"
    bot.reply_to(message, response)

# Function to update the global wrongs list
def update_wrongs(new_wrongs):
    global wrongs
    wrongs = [i + j for i, j in zip(wrongs, new_wrongs)]

# Start the bot polling
def start_bot_polling():
    bot.polling()

# Start the bot polling in a separate thread
import threading
threading.Thread(target=start_bot_polling).start()

# Run the FastAPI web server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

