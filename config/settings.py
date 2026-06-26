from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))