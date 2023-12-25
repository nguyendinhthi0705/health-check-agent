import schedule
import time
import health_check as glib
import os



def check():
  result, msg =  glib.check_readness()
  if not result:
    glib.print_with_time("Check fail: " + msg)
  else:
    glib.print_with_time("Check pass")

def run_schedule():
    frequency = int(os.environ.get('CHECK_FREQUENCY'))
    schedule.every(frequency).minutes.do(check)
    while True:
        schedule.run_pending()
        time.sleep(frequency)

run_schedule()
		
