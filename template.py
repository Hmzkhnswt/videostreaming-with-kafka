import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "videoStreaming_with_kafka"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"__init__.py",
    f"controller/__init__.py",
    f"controller/producer_controller.py",
    f"controller/consumer_controller.py",
    f"model/__init__.py",
    f"model/kafka_producer.py",
    f"model/kafka_consumer.py",
    f"view/__init__.py",
    f"view/videostream.py",
    f"view/videodisplay.py",
    f"main_producer.py",
    f"main_consumer.py",
    f"requirements.txt",
    f"config.py",
    f"Dockerfile",
    f"docker-compose.yml",
    f".gitignore",
    f"README.md",
    f"LICENSE",
    f".env",    
    "logs/.gitkeep",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")