# Reddit Bot

A Reddit Bot that replies with Streamable mirror links on `r/Gunners`

## Getting Started

### 1. Install the python packages
```bash
pip install -r requirements.txt
```

### 2. Create an app on Reddit
Go to [Reddit Apps](https://old.reddit.com/prefs/apps/) and create an app of type **"script"**.

![](https://raw.githubusercontent.com/adityathebe/redditBot/master/img/dev-apps.png)

### 3. Create an account on Streamable
Sign up on [streamable](https://streamable.com/). You'll need the *username* and *password* for the script.

### 4. Run the bot
First, fill up the necessary details in `config.py` file. See `config-sample.py` file for guidance.

```
python bot.py
```

* * *

> Created with PRAW *(Python Reddit API Wrapper)*