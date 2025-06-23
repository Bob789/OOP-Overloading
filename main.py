from notification import Notification
from advanced_logger import Logger
msg = Notification()
msg.notify("user1")
msg.notify("user1", "user2", "user3")

logger = Logger()
logger.log("Hello world!")  # Text
logger.log(404)             # Number
logger.log(["item1", "item2"])  # List

