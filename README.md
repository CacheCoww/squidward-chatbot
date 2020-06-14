# Squidward Chatbot

## Project Overview
This is a chatbot created with deep learning modeled off of the TV character Squidward from Spongebob. The model was created using Python and PyTorch and the model was deployed using a Flask application.

<img src="https://github.com/hmsmith5/squidward-chatbot/blob/master/screenshot1.PNG?raw=true" alt="screenshot with sample chat">

## Results
The first model was not very coherent so I added in the lines from the other characters. I am looking into using AWS EC2 for more power to train just the Squidward lines.

## Progress
 - Created a script to extract the transcript for every episode from website into a .txt file [generateTranscripts.py]
 - Created functions to extract sentence-response pairs for a specified character [
 - Defined model classes and ran data through models
 - Integrated model into Flask application
