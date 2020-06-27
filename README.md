# Squidward Chatbot

## Project Overview
This is a chatbot created with deep learning modeled off of the TV character Squidward from Spongebob. The model was created using Python and PyTorch and the model was deployed using a Flask application on Heroku.

<img src="https://github.com/hmsmith5/squidward-chatbot/blob/master/screenshot1.PNG?raw=true" alt="screenshot with sample chat">

## Results
The first model was not very coherent so I added in the lines from the other characters. The first model was trained on my computer using CPU only. I also trained a couple more with slightly different parameters using an AWS EC2 instance.

## Progress
 - Created a script to extract the transcript for every episode from website into a .txt file [generateTranscripts.py]
 - Created functions to extract sentence-response pairs for a specified character [parse_transcript.py]
 - Defined classes for holding and proccesing vocab and sentences [load_data.py]
 - Defined model classes and ran data through models [model.py]
 - Integrated model into Flask application [app.py]

## To Do
 - Optimize models for better performance
 - Fix inconsistent punctuation
 - Improve Frontend design
 - The model is too large to upload to GitHub so figure out workaround
