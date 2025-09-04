import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# File handler for DEBUG messages
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)

# Logging examples
logger.info("This shows up in console and app.log")
logger.debug("This shows up only in app.log")
