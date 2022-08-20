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

### Working example
https://pyscheduler.andrey-sobolev.ru/

## Buy me a coffee [thanks]
```no-highlight
TPbvvhqZsEuKCLEAWMAERgw7f82eGeU389 TRC (TRON)
```



