# Phrase detector bot for telegram

## Objective

We will build a bot that can be added to a telegram channel that will detect prohibited phrases/words
and delete those from the channel.

## Tech

How we do the small things is how we do the big things. I will lay the groundwork and estabilish the practises for how to go about things. One smal thing. I work on linux primarily, so we'll need a team member to update our docs for Windows and other environments.

### Stack
Here we just list all the concepts that team member need to know to get started. If we need a seperate page explaining all terms we can add that.

#### virtualenv
virtualenv is a tool used to isolate Python environments. Say you're build to similar projects and both use a lot of different libraries. The thing is when you install those libraries into the global cache you might override version dependencies. Also when you deploy your application you'll end up having to make a list of all your dependencies. Virtualenv has some neat functonality allowing you to take a snapshot of your environment and recreate it on another machine.

### pip
this tool is used to install required depedencies

### python-telegram-bot
we'll use this library because it's well thought-out and has good documentation and has an active community.

## Installation instructions

- Get the latest code
- In root folder create a file called `producton.env` and update as per settings in `settings-sample.env`
- Install `pip` and `virtualenv`
- Create a virtual environment with `virtualenv -p python3 .venv` (as an example)
- Install depedencies with `pip install -r requirements.txt`
- Finally test everything with `python run.py` 
- If you get stuck the project board is an additional place to look at for information.
