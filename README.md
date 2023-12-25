# Health Check
This is simple app to health check local server via Cron job or API.
To setup:
> cd health-check-agent
> python3 -m venv .venv
> . .venv/bin/activate
> pip install -r requirements.txt

# To Start
## Start Web API
> flask run

## Start Cron Job
> python run_schedule.py

## Start Cron Job Check and Trigger Action Then Stop the App
> python run_manual.py