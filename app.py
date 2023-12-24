from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
import health_check as glib

app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()


health.add_check(glib.check_liveness)
envdump.add_section("application", glib.check_readness)

# Add a flask route to expose information
app.add_url_rule("/live", "Live Check", view_func=lambda: health.run())
app.add_url_rule("/read", "Read Check", view_func=lambda: envdump.run())

