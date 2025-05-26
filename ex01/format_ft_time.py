import time
from datetime import datetime

curr = time.time()

scientific = f"{curr:.2e}"

formatted_date = datetime.fromtimestamp(curr).strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {curr:,.4f} or {scientific} in scientific notation\n{formatted_date}")