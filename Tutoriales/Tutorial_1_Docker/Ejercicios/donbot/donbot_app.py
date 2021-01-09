from slack import WebClient
from donbot import DonBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new DonBot
don_bot = DonBot("#bot")

# Get the onboarding message payload
message = don_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)