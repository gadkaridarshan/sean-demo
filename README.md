# Sean the Rasa Bot by Darshan

## :surfer: Introduction
The purpose of this repo is to showcase a contextual AI assistant (simple version) built with the open source Rasa framework.

Sean is an demo version and lives in our docs, 
helping regular folks talk about their Physical and Mental Health issues. It supports the following user goals:

- Talk about their Physical Issues
- Talk about their Mental Issues
- Connect them to an advisor, if they want
- Collect your information and provide it to the advisor for them to contact you

## 👷‍ Installation

To install Sean, please clone the repo and run:

```
cd sean-demo
pip install -r requirements.txt
pip install -e .
```
This will install the bot and all of its requirements.
Note that this bot should be used with python 3.6 or 3.7.

## 🤖 To run Sean:

Use `rasa train` to train a model (this will take a significant amount of memory to train,
if you want to train it faster, try the training command with
`--augmentation 0`).

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions --actions actions.actions
```

In another window, run the bot:
```bash
docker run -p 8000:8000 rasa/duckling
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working 
under the hood. To simply talk to the bot, you can remove this flag.

## To test Sean:

After doing a `rasa train`, run the command:

```bash
rasa test --stories test/test_conversation.md
rasa test --stories test/test_nlu.md
rasa test --stories test/test_stories.md
```

## 👩‍💻 Overview of the files

`data/core/` - contains stories 

`data/nlu` - contains NLU training data

`actions` - contains custom action code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

## ⚫️ Code Style

To ensure a standardized code style we use the formatter [black](https://github.com/ambv/black).

If you want to automatically format your code on every commit, you can use [pre-commit](https://pre-commit.com/).
Just install it via `pip install pre-commit` and execute `pre-commit install` in the root folder.
This will add a hook to the repository, which reformats files on every commit.

If you want to set it up manually, install black via `pip install black`.
To reformat files execute
```
black .
```

## :gift: License
Licensed under the GNU General Public License v3. Copyright 2018 Rasa Technologies
GmbH. Licensees may convey the work under this license. There is no warranty for the work.

{{authors}} 
Darshan Gadkari
