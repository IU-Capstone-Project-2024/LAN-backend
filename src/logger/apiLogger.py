import logging
from pathlib import Path

apiLogger = logging.getLogger(__name__)
apiLogger.setLevel(logging.DEBUG)

logFile = Path(__file__).parent.parent / "logs/api.log"
fileHandler = logging.FileHandler(logFile)

dateformat = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('%(name)s - %(asctime)s - %(processName)s - %(levelname)s - %(pathname)s:%(funcName)s:%(lineno)d > %(message)s', datefmt=dateformat)

fileHandler.setFormatter(formatter)
apiLogger.addHandler(fileHandler)