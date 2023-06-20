# Generative chatbot

## Set up and installing

### Prerequisites

The following programs should already be installed:

- python3.7 (newer versions are not compatible with the dependencies used)
- pip (tested with v22.3.1, newer versions should work)

Once installed, set-up and activate a venv in python. 
Note that the specific steps may slightly differ with different system environments (OS, CLI).

`python3.7 -m venv venv`
`venv\Scripts\activate`

To install all dependencies run:

`pip install -r requirements.txt`

## Run the application

To run the application, use the following command:

`python3.7 bot.py`

This will load the chat-data from the chat.txt file and start training the chatbot.
The training data is stored in a sqlite3 database.

Once the application is running, open the botinterface.html file in a browser of choice.

Tested with:
- Chrome 114.0.5735.111
- Edge 114.0.1823.51
- Firefox 114.0.1

Now, you may start typing and should get a response from the chatbot upon pressing enter.
The bot will use your input and keep learning.