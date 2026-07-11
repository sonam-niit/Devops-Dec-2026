import logging

logging.basicConfig(
    level= logging.DEBUG,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("DB connected")
logging.info("User Logged In")
logging.warning("Disk Usage 85%")
logging.error("Lost DB Connect")
logging.critical("App crashed")

# Debug < Info < Warning < Error < Critical