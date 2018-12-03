#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import sys,os

#Set the import directory

sys.path.append(os.path.join(sys.path[0],'ChatBot_Completed'))#Set the csv file directory
path = "./ChatBot_Completed"
os.chdir( path )
#Import the app_main from ChatBot_Billy_v2
import ChatBot_new_v4 as cb

app = Flask(__name__)

#Test Locally in ngrok
ACCESS_TOKEN = 'EAADFF6ZAbMocBABEjfJCNaHufY2InFQvyZBqgL0NctZBZC5ZBplcHmVRZB435VtV7ivHkXwjvIHbL1vvbL6XEH0p2pjhWTyPb1K28KItZBHrjrrV6FpxL4QmBwn3C8wwoI4Gh0Jy4DweGCTi4bkZBTdtmtEovQuhIZAArkZBL1ZAWu5p1aRVvqZAuryL'
VERIFY_TOKEN = 'TESTINGTOKEN'


#Run in heroku web server
#ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#VERIFY_TOKEN = os.environ['VERIFY_TOKEN']

bot = Bot (ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
#                    response_sent_text = get_message()

                    chatter_input = message['message'].get('text')
                    print(chatter_input)
                    
                    
                    response_sent_text_raw = cb.Chatbot_1(chatter_input)
                    response_sent_text = str(response_sent_text_raw)
                    print(response_sent_text)
                    
                    
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["No photo!", "No image", "Recognize image is not my work", "I should build a CNN application to recognize this image, not now, in the future, maybe :)", "Good one (Y)",u'\U0001f604' + "No photo for now"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
