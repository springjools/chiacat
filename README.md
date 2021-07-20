# chiacat
Python wrapper for madmax plotter and telegram notifier

# What you need

- A telegram bot: talk to botfather to create one/get the bot token

- the chat id/group id of the chat or group where you want to post messages, see this:
https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

- the madmax plotter. I'm using the windows branch and powershell, but I guess it would be easy to use linux as well with small modifications
https://github.com/madMAx43v3r/chia-plotter#install see the link under windows

# Usage instructions

Fill in your plotter info in madmax.ps1 and telegram info into telegramMsg.py

Install python requirements with pip3 install -r requirements.txt

Run like this:

python3 chiacat.py

It opens powershell with an argument named  madmax.ps1, currently it looks for this file in the same folder. An example script is provided, but it needs your pool contract and farmer key. 

Enter your telegram bot token and chat id in telegramMsg.py. The chat id is the group or person who should receive the notifications.



# Improvements

This can of course be improved a lot. Suggestions are welcome and I can also add some quality if life improvements if anyone actually is interested in using this :)
