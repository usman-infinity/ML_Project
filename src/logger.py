import logging
import os
from datetime import datetime

# 1️⃣ Create logs folder (just folder)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 2️⃣ Create log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 3️⃣ Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

