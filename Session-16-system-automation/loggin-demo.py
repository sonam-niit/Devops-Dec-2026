import logging

logging.basicConfig( 
    filename="app.log",
    level=logging.DEBUG,
    filemode="a", # default mode is append only
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

logging.debug('Water Temp check')
logging.info('Brewing Started')
logging.warning('Water level is low')
logging.error('No Water Found')
logging.critical('Machine Shutting Down')

print("Log Written Successfully")
# By default the Log level is Warning
# Means when you run code you can't see Info and Debug Messaged

# Debug < Info < Warning < Error < Critical
# Default formart: LogLevel:username:message

# a is append mode means add new logs at the end of the file
# w mode will delete old data and add latest logs only

