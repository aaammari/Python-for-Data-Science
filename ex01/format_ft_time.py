import time
from datetime import datetime

seconds_since_epoch = time.time()
print(
    "Seconds since January 1, 1970:"
    f" {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation"
)
print(datetime.fromtimestamp(seconds_since_epoch).strftime("%b %d %Y"))
