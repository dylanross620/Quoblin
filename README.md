# Quoblin

A Discord chat bot for quote tracking.

## Setup

### Python Setup

This project uses python 3 and requires the datetime module. This can be installed using pip by using ```pip install -r requirements.txt ```.

### Google Sheets Setup

1. Go to https://developers.google.com/sheets/api/quickstart/python#enable_the_api and follow the instructions for the sections labelled "Enable the API" and "Configure the OAuth consent screen"
2. Under `Data Access`, click "Add or Remove Scopes" and add the "https://www.googleapis.com/auth/spreadsheets" scope
3. Under `Audience`, add yourself as a test user to avoid needing verification
resulting `credentials.json` file to the project directory.
4. Return to the Google instructions mentioned in step 1. and follow the next section, which should be labelled "Authorize credentials for a desktop application". Download the credentials file, rename it to `credentials.json`, and place it in this folder

Next, create a spreadsheet for the quotes to be placed in and generate a shared link where people with the link can view the spreadsheet.

If you don't run the bot for a while, you may run into an authorization error. To fix it, delete the `token.json` file and run the bot again.

## Discord Setup

1. Go to [https://discord.com/developers/applications](https://discord.com/developers/applications)
2. Click `New Application` and name the application Quoblin (or whatever you want the bot to be named)
3. Under `OAuth2`, make the following changes:
    - Add `http://localhost:8888` as a Redirect
    - Add the `applications.commands`, `messages.read`, and `bot` scopes, selecting your localhost redirect URL
    - Under Bot Permissions, select `Send Messages` and `Use Slash Commands`
4. Go to the auto-generated link on the bottom of the `OAuth2` page. This will add the bot to your server. After adding the bot you'll be redirected to an invalid webpage, that is fine and you can safely close the tab
5. Under `Bot`, click on `Regenerate token`. Save this token, you will be asked for it when you run the bot for the first time
6. Still under `Bot`, scroll down to `Privileged Gateway Intents` and enable `Message Content Intent`

## Running

To run the bot, perform setup if you have not already. Once setup is completed run ```python bot.py```

The first time you run the bot, you will be prompted for several variables:
- First you will be prompted for the id of the Google Sheet to be used for the quotes. This can be obtained from the URL of the sheet, in the format `docs.google.com/spreadsheets/d/<your_id_here>/edit`.
- Second you will be prompted for the range of the spreadsheet that is to be used for quotes in the format `<sheet_name>!<range>`. For example, if the primary sheet within the spreadsheet file is name `Quotes` and you would like quotes to fill the first column, the range should be `Quotes!A:B` (the 2nd column is needed).
- Third you will be prompted for the shared link generated in the Google Sheets setup.
- Fourth you will be prompted for the Discord bot token you received in step 5 of the Discord setup
- Finally, you will be asked to provide a comma-separated list of user roles that are considered moderators for the sake of the bot. This list is case-sensitive

To change any of these settings, you can modify the `settings.json` file manually or delete it in order to redo the prompts

