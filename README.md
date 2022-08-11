<div align="center">

# ![Pringles Bot Logo](https://i.imgur.com/9o0hyRz.png)

## A bot that will give you free pringles, poorly coded in Python using Selenium and AntiCaptcha. If Steve Cahillane sees this, expect this repository to go down. If this bot surprisingly worked for you, it would be cool if you [donated](https://en.liberapay.com/bestadam/) to me. It would convince me to code better and actually be more commited to these projects (cause who doesn't like money???).
<img alt="GitHub" src="https://img.shields.io/github/license/bestadamdagoat/pringles-bot"> ![Website](https://img.shields.io/website?label=pringles%20site&url=https%3A%2F%2Fpringlessweepstakes.com) ![Liberapay receiving](https://img.shields.io/liberapay/receives/bestadam) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/selenium) ![GitHub issues](https://img.shields.io/github/issues/bestadamdagoat/pringles-bot)
</div>

Basically what this bot does is it:
- Opens up the [Pringles promo site](https://pringlessweepstakes.com).
- Generates random info using your catchall.
- Auto solves the captcha (the system is a little slow and you will need to get credits on the [AntiCaptcha site](http://getcaptchasolution.com/wfgri4goqd)).
- Instantly goes to the reward screen and repeats the whole process.

## NOTES: 
This bot is very bad and will eventually fail due to either unknown reasons or AntiCaptcha being too slow, make sure to check up on it at least once an hour.

When initially starting the bot, make sure to close out the tab that asks for you to accept cookies. If you don't the bot will fail.

You will **NOT** win every time when using this bot, be patient.

The Pringle links will go to your email/catchall.

You are free to modify the code in any way you want, but if you do PLEASE make a PR.

## UPCOMING FEATURES:
NOTE: I probably won't implement these unless this promotion gets extended or revived (after the end of it). If you want to see the latest planned features/progress on them, go to the Issues tab and sort by the tag [enhancement](https://github.com/bestadamdagoat/pringles-bot/labels/enhancement). 

- Auto Accept Cookies https://github.com/bestadamdagoat/pringles-bot/issues/1
- Re-enter using the same generated account https://github.com/bestadamdagoat/pringles-bot/issues/2
- Make the script into an Executable and configure it using a config file https://github.com/bestadamdagoat/pringles-bot/issues/3
- Use different captcha system https://github.com/bestadamdagoat/pringles-bot/issues/4
- Track the Wins/Losses https://github.com/bestadamdagoat/pringles-bot/issues/5
- Send info to a Discord Webhook https://github.com/bestadamdagoat/pringles-bot/issues/6

## HOW TO USE THE BOT:
NOTE: Make sure you have any version of Chrome 104 installed (unless you manually upgraded chromedriver.exe). You can do this by going to chrome://version.
1. Clone the repository
     - You can do this by going to Code (the green button) and either downloading this repo as a zip (make sure to unzip it) or doing it the cool way and cloning with Git
2. Open up the file in your favorite IDE (like PyCharm or VScode)
     - If you can open up this file in CMD/Terminal, you do not need an explanation on how to get this thing fully setup.
3. Go into the terminal and type `pip install -r requirements.txt`.
4. Unzip `anticaptcha-blank.zip` and put your [AntiCaptcha API Key](http://getcaptchasolution.com/wfgri4goqd) in the `config_ac_api_key.js` file located at `\anticaptcha-blank.zip\js`.
     - Make sure to put the API key into the `var antiCapthaPredefinedApiKey = '';` line.
5. Rezip the `anticaptcha-blank.zip` file and replace the old one.
     - You can rezip files using 7zip or Winrar.
6. Edit the `catchall = "YOURCATCHALLHERE"` line in `pbot.py` so that `YOURCATCHALLHERE` is replaced with your catchall.
     - Your catchall is your domain (ex. github.com) not a full email (like adam@github.com).
7. You are now ready to run the bot!
     - Make sure to agree to cookies when running the bot.
