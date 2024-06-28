import logging
from pathlib import Path

botLogger = logging.getLogger(__name__)
botLogger.setLevel(logging.DEBUG)

logFile = Path(__file__).parent.parent.parent / "logs/bot.log"
fileHandler = logging.FileHandler(logFile)

dateformat = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('%(name)s - %(asctime)s - %(processName)s - %(levelname)s - %(pathname)s:%(funcName)s:%(lineno)d > %(message)s', datefmt=dateformat)

fileHandler.setFormatter(formatter)
botLogger.addHandler(fileHandler)

