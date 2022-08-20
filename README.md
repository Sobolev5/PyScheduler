## PyScheduler
Simple python snippets scheduler with cron like syntax and metamask web3 auth.

### First
Create virtualenv and fill database
> python -m venv env && source env/bin/activate && pip install -r requirements.txt
> python run.py fill_database "fill_database()"

### Second
Rename .env.example to .env and change necessary values

### Third
Add to cron
> */1 * * * * /var/www/YOUR_PATH/env/bin/python /var/www/YOUR_PATH/run.py snippet.scheduler "run_snippets()" &>/dev/null

# Coffee
**0x6817b29f6a25B7BaE42158FAFad7b782415e4209** ERC20 Thank you



