from os.path import dirname, abspath
import logging
import sys

ROOT_DIR = dirname(abspath(__file__))

logger = logging.getLogger("package")  # Create logger with name 'package'
handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
