import logging 
import os
from datetime import datetime

# 1. Log file ka naam (Time ke saath)
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Logs folder ka path (Fix: Added os.getcwd() here)
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# 3. Folder banana (Agar nahi bana hai toh)
os.makedirs(logs_path,exist_ok=True)

# 4. Final File Path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
