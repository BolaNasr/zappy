import os
import time
import re
import slack
from get_tweets import get_tweets
# instantiate Slack client

slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = slack.RTMClient(token=slack_token)

# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "go"
webclient = slack.WebClient(slack_token)

def handle_command(**kwargs):
    """
        Executes bot command if the command is known
    """

    channel_id = kwargs['data']['channel']
    thread_ts = kwargs['data']['ts']
    if "user" in kwargs['data']:
        user = kwargs['data']['user']
    else:
        return
    if EXAMPLE_COMMAND in kwargs['data']['text']:

        get_tweets("elementsdevelo1")

        webclient.api_call('chat.postMessage',
            data = {
            "channel":channel_id,
            "text": "http://127.0.0.1:8000/tweets/" ,
            "thread_ts":thread_ts })
    else:
        # Default response is help text for the user
        default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

        # Sends the response back to the channel
        webclient.api_call('chat.postMessage',
            data = {
            "channel":channel_id,
            "text":default_response,
            "thread_ts":thread_ts })
            

if __name__ == "__main__":

    if webclient.rtm_connect():
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = webclient.api_call("auth.test")["user_id"]
        while True:
            slack_client.on(event='message', callback=handle_command)

            slack_client.start()

            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")

