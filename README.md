# Health Check
This is simple app to health check local server via Cron job or API.
# To setup:
 Setup <a href='https://docs.python-guide.org/starting/install3/linux/' target='_blank'> Python <a><br />
 Setup <a href='https://docs.python-guide.org/starting/install3/linux/' target='_blank'> Python Env<br />

> git clone https://github.com/nguyendinhthi0705/health-check-agent.git <br />
> cd health-check-agent <br />
> python3 -m venv .venv <br />
> . .venv/bin/activate <br />
> pip install -r requirements.txt <br />

# To Start
## Update Configuration:
 Edit file .env for mysql connection, default CHECK_FREQUENCY is 1 or 1 minute
## Start Cron Job Check and Trigger Action Then Stop the App
To Add your own shell script action just update file actions.sh 
> python run_manual.py

## Start Web API
> flask run

## Start Cron Job
> python run_schedule.py