import logging
import os
from datetime import datetime

# Create logs directory at project root
LOG_DIR = "logs"
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Get project root (current working directory)
logs_path = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO,
    filemode='a'
)

if __name__ == "__main__":
    logging.info("Logger has been configured.")