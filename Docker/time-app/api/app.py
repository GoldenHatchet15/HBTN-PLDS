from flask import Flask, jsonify, request
from datetime import datetime
import pytz
import os

app = Flask(__name__)

@app.route("/api/time")
def get_time():
    # Get the default timezone (container's timezone)
    container_tz = os.environ.get('TZ', 'UTC')
    
    # Get the current time in the container's timezone
    now = datetime.now(pytz.timezone(container_tz))
    
    # Get client timezone if specified in query parameters
    client_tz = request.args.get('tz')
    client_time = None
    
    if client_tz:
        try:
            # Convert time to requested timezone
            client_time = now.astimezone(pytz.timezone(client_tz)).strftime("%H:%M:%S")
        except:
            client_time = "Invalid timezone"
    
    return jsonify({
        "time": now.strftime("%H:%M:%S"),
        "timezone": container_tz,
        "client_time": client_time,
        "client_timezone": client_tz,
        "available_timezones": sorted(pytz.common_timezones)[:10] + ["..."] + sorted(pytz.common_timezones)[-10:]  # Just sending a sample
    })

@app.route("/time")
def time_without_prefix():
    # Forward to the main endpoint
    return get_time()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)