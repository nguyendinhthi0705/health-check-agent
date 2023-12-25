import schedule
import time
import health_check as glib
import os


def run_manual():
  frequency = int(os.environ.get('CHECK_FREQUENCY'))
  while True:
    glib.print_with_time("Trigger Health Check")
    result, msg =  glib.check_readness()
    if not result:
      glib.print_with_time("Check fail: " + msg)
      glib.print_with_time("Trigger fail actions")
      glib.print_with_time("Stop the check")
      break
    else:
      glib.print_with_time("Check pass")
    time.sleep(frequency*59)

run_manual()
		
