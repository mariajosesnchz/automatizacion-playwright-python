import os

BASE_URL = os.getenv("BASE_URL", "https://www.xtrim.com.ec/")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "10000"))