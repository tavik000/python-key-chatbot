"""
对SequenceToSequence模型进行基本的参数组合测试
"""

import sys
import random
import pickle

import numpy as np
import tensorflow as tf
# import jieba
# from nltk.tokenize import word_tokenize
from hanziconv import HanziConv
import datetime
import json

#---------------English Model-------------
import os
import re
from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor
#---------------Server----------------------
from flask import Flask, request
from pymessenger.bot import Bot as PYBot

#--------------Chatterbot---------------------
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from difflib import SequenceMatcher
import os
import csv
import random

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
out_msg = ''

def get_response(userText):
    bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "response_selection_method": "chatterbot.response_selection.get_random_response"

        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.'
        }
        ],            
    preprocessors=['chatterbot.preprocessors.clean_whitespace',
                   'chatterbot.preprocessors.unescape_html', 'chatterbot.preprocessors.convert_to_ascii'],
        silence_performance_warning=True,
        filters=["chatterbot.filters.RepetitiveResponseFilter"]
    )

def booking():
    bookings = []
    bookingref = random.randint(0,100000)
    bookingref = str(bookingref)

    print("Your Booking number: ", bookingref)
    surname = input("Please enter your surname: ")
    forename = input("Please enter your other name: ")
    film = input("Please enter the name of film you want to see: ")
    day = input("Please enter the day of the week you want to see the film: ")
    while (day not in ['1', '2', '3', '4', '5', '6', '7']):
        day = input("You input weekday not correct, please try to input again: ")    
    noofseat = input("Please enter number of the seat you want to researved: ")
    while ((noofseat.isdigit() == False) or (noofseat.isdigit() == True and int(noofseat) > 50)):
        if (noofseat.isdigit() == False):
            noofseat = input("You have input incorrect integer number, please try to input again: ")
        else:
            noofseat = input("You have inputted the number exceeds the maxium 50 seats in the cinema, please try to input again: ")    
    print ("Dear ", forename, surname, ", your booking on the film **", film, "** on day ", day, "with ", noofseat, "people has been confirmed.")
    print ("Thank you for your booking!!!")

    bookings.append(bookingref)
    bookings.append(surname)
    bookings.append(forename)
    bookings.append(film)
    bookings.append(day)
    bookings.append(noofseat)

    with open("cinema.csv","a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(bookings) 

def booking_ch():
    bookings = []
    bookingref = random.randint(0,100000)
    bookingref = str(bookingref)

    print("你的預約編號: ", bookingref)
    surname = input("請問你的姓氏: ")
    forename = input("請問你的名字: ")
    film = input("你想看的電影名稱: ")
    day = input("你想看星期幾的電影: ")
    while (day not in ['1', '2', '3', '4', '5', '6', '一', '二', '三', '四', '五', '六', '日']):
        day = input("你輸入星期幾的日子不正確啊，麻煩你重新輸入啦: ")    
    noofseat = input("請問要預約多少個座位: ")
    while ((noofseat.isdigit() == False) or (noofseat.isdigit() == True and int(noofseat) > 50)):
        if (noofseat.isdigit() == False):
            noofseat = input("你輸入的資料不是正確的人數喎，麻煩你重新輸入啦: ")
        else:
            noofseat = input("電影院好似冇咁多位喎，麻煩你重新輸入啦: ")    
    print ("親愛的 ", surname, forename, ", 你想預約的電影 **", film, "** 在星期", day, "預約", noofseat, "個座位的電影戲票已經完成。")
    print ("還有什麽服務可以幫你!!!")

    bookings.append(bookingref)
    bookings.append(surname)
    bookings.append(forename)
    bookings.append(film)
    bookings.append(day)
    bookings.append(noofseat)

    with open("cinema.csv","a", newline='') as csvfile:    
        writer = csv.writer(csvfile)
        writer.writerow(bookings) 

def view_booking():
    count = 0
    with open('cinema.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            bookingref = row[0]
            surname = row[1]
            forname = row[2]
            film = row[3]
            day = row[4]
            noofseat = row[5]
            output = (bookingref, surname, forname, '**', film, '**', 'Booked Weekday:', day, 'No. of seat:', noofseat)
    return(output)

def view_booking_ch():
    count = 0
    with open('cinema.csv', 'r', encoding="utf-8", errors='ignore') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            bookingref = row[0]
            surname = row[1]
            forname = row[2]
            film = row[3]
            day = row[4]
            noofseat = row[5]
            output = (bookingref, surname, forname, '**', film, '**', '已經預約星期', day, '人數:', noofseat)
    return(output)

def joking():
    joke_choice = random.randint(1,9)
    joke_choice = str(joke_choice)
    with open('joke.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        num = []
        topic = []
        detl = []
        for row in reader:
            num = row[0]
            topic = row[1]
            detl = row[2]
            if (joke_choice == num):
                return(detl)

def joking_ch():
    joke_choice_ch = random.randint(1,9)
    joke_choice_ch = str(joke_choice_ch)
    with open('joke_ch.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        num = []
        topic = []
        detl = []
        for row in reader:
            num = row[0]
            topic = row[1]
            detl = row[2]
            if (joke_choice_ch == num):
                return(detl)

def Chatbot_1(input_msg):
    bot.read_only = True

    repetitiveReply = [
            "This question seems faimilar",
            "You are so boring , let talk something else",
            "boo...boo... Stop . You just asked it",
            "Ok! Next Question",
            "OMG! Can we talk about something else?",
            "I am not answering such a stupid question",
            "Talking with you is damn boring ! Why are you keep asking the same question",
            "Ok ! Stop it , i am done! . Next Question!",
            "Oh! Come on ! Next Question",
            "@#$545$ You! Why are you keep asking. ",
            "This question seems similar to the last message, Let change another Topic,ok?",
            "Sorry, i have already answer this question"
    ]

    unknownReply = [
            "Sorry, i cannot understnad this question",
            "Sorry, What does it mean? ",
            "I am sorry, I did not catch what you said. Could you repeat it ",
            "I am sorry, I did nott understand that? Would you mind repeating it",
            "I am sorry, what was that?",
            "What did you say?",
            "What was that?",
            "Excuse me? ",
            "What?",
    ]

    last_message = ""
    counter=0

    def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()

    message = (input_msg)
    if message.strip() != 'Bye':
        if ('cinema' in message.strip()) and ('booking' in message.strip()):
            out_msg = booking()
        elif (b'\xe9\x9b\xbb\xe5\xbd\xb1'.decode('utf-8') in message.strip()) and (b'\xe9\xa0\x90\xe7\xb4\x84'.decode('utf-8') in message.strip()):
            out_msg = booking_ch()
        elif ('view' in message.strip()) and ('booking' in message.strip()):
            out_msg = view_booking()
        elif (b'\xe9\xa0\x90\xe7\xb4\x84'.decode('utf-8') in message.strip()) and (b'\xe8\xa7\x80\xe7\x9c\x8b'.decode('utf-8') in message.strip()):
            out_msg = view_booking_ch()
        elif ('joke' in message.strip()) and ('tell' in message.strip()):
            out_msg = joking()
        elif (b'\xe7\xac\x91\xe8\xa9\xb6'.decode('utf-8') in message.strip()) and (b'\xe8\xac\x9b'.decode('utf-8') in message.strip()):
            out_msg = joking_ch()
        else:
            if similar(message, last_message) > 0.4:
                out_msg = random.choice(repetitiveReply)
                counter += 1
                last_message = message
            if message == last_message:
                out_msg = random.choice(repetitiveReply)
                counter += 1
                last_message = message
            if message.strip().lower() != 'bye':
                response = bot.get_response(message)
                if(response.confidence > 0.4):
                    out_msg = response
                    counter = 0
                elif response.confidence <= 0.4:
                    out_msg = random.choice(unknownReply)
                    counter += 1
                last_message = message
            if message.strip().lower() == 'bye':
                out_msg = 'Bye'
            if counter >= 5:
                out_msg = 'I have to go now . Bye Bye!'
    if message.strip() == 'Bye':
        out_msg = 'Bye!'
    return(out_msg)


#--------------Chatterbot---------------------

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

sys.path.append('..')


def test(params,user_text):
    """测试不同参数在生成的假数据上的运行结果"""

    from sequence_to_sequence import SequenceToSequence
    from data_utils import batch_flow
    from word_sequence import WordSequence # pylint: disable=unused-variable
    
    #---------------English Model-------------
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
    res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')
    
    #---------------Chinese Model-------------
    x_data, _ = pickle.load(open('chatbot.pkl', 'rb'))
    ws = pickle.load(open('ws.pkl', 'rb'))

    for x in x_data[:5]:
        print(' '.join(x))

    config = tf.ConfigProto(
        device_count={'CPU': 1, 'GPU': 0},
        allow_soft_placement=True,
        log_device_placement=False
    )

    # save_path = '/tmp/s2ss_chatbot.ckpt'
    save_path = './s2ss_chatbot_anti.ckpt'
    
    #---------------Chinese Model------------- 测试部分
    tf.reset_default_graph()
       
    #--------Create two graphs------------------
    g1=tf.Graph()
    sess1=tf.Session(graph=g1)
    
    g2=tf.Graph()
    sess2=tf.Session(graph=g2,config=config)
    #---------------English Model-------------
    with sess1.as_default():
        with g1.as_default():
            #a=tf.constant([1.0,1.0])
            #b=tf.constant([1.0,1.0])
            #result1=a+b
            predictor = BotPredictor(sess1, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                             result_dir=res_dir, result_file='basic')
           # This command UI has a single chat session only
            session_id = predictor.session_data.add_session()
            
    
    #---------------Chinese Model-------------
    with sess2.as_default():
        with g2.as_default():
            
            model_pred = SequenceToSequence(
                    input_vocab_size=len(ws),
                    target_vocab_size=len(ws),
                    batch_size=1,
                    mode='decode',
                    beam_width=0,
                    **params
                    )
            init = tf.global_variables_initializer()
            sess2.run(init)
            model_pred.load(sess2, save_path)
    
    #call function
    #while True:
        #user_text = input('Input Chat Sentence:')
        
    if re.search(u'[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC]',user_text)!=None:
        isChinese=True
        user_text =HanziConv.toSimplified(user_text)                    
    else:
        isChinese=False
                                    
    if not isChinese:
            #---------------English Model-------------
        with sess1.as_default():
            with sess1.graph.as_default():
                print('English model: ',re.sub(r'_nl_|_np_', '\n', predictor.predict(session_id, user_text)).strip())
                output_chatlearner=re.sub(r'_nl_|_np_', '\n', predictor.predict(session_id, user_text)).strip()    
                #output = Chatbot_1(user_text)
                #print('Chatterbot: ', output)
                return output_chatlearner
    else:
            #---------------Chinese Model-------------
        with sess2.as_default():
            with sess2.graph.as_default():
                date=['日期','时间','日子']
                if any(x in user_text for x in date):
                    print(datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}%H{H}%M{M}%S{S}').format(y='年', m='月', d='日',H='時',M='分',S='秒'))
                else:                    
                    #call seq2seq
                    x_test = [list(user_text.lower())]
                    # x_test = [word_tokenize(user_text)]
                    bar = batch_flow([x_test], ws, 1)
                    x, xl = next(bar)
                    x = np.flip(x, axis=1)
                        
                    #print('x,xl',x, xl)
                    pred = model_pred.predict(
                        sess2,
                        np.array(x),
                         np.array(xl)
                    )
                    #print('pred',pred)
                                    # prob = np.exp(prob.transpose())
                    #print('ws_inverse',ws.inverse_transform(x[0]))
                    for p in pred:
                        ans = ws.inverse_transform(p)
                    
                    random_int= random.randint(0,1)
                                        
                    output_justanother= 'Chinese model: ',''.join(ans).replace('</s>','')    
                    output_chatterbot = Chatbot_1(user_text)
                    
                    if random_int==0:
                        print('just another')
                        return output_justanother
                    else:
                        print('chatterbot')
                        return output_chatterbot
                    

       
'''
        while True:
            user_text = input('Input Chat Sentence:')
            user_text =HanziConv.toSimplified(user_text)            
            if user_text in ('exit', 'quit'):
                exit(0)
            
            
           '''
#---------------Server----------------------
app = Flask(__name__)

#Test Locally in ngrok
ACCESS_TOKEN = 'EAADFF6ZAbMocBABEjfJCNaHufY2InFQvyZBqgL0NctZBZC5ZBplcHmVRZB435VtV7ivHkXwjvIHbL1vvbL6XEH0p2pjhWTyPb1K28KItZBHrjrrV6FpxL4QmBwn3C8wwoI4Gh0Jy4DweGCTi4bkZBTdtmtEovQuhIZAArkZBL1ZAWu5p1aRVvqZAuryL'
VERIFY_TOKEN = 'TESTINGTOKEN'


#Run in heroku web server
#ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#VERIFY_TOKEN = os.environ['VERIFY_TOKEN']

pybot = PYBot (ACCESS_TOKEN)

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
                    
                    response_sent_text_raw = test(json.load(open('params.json')),chatter_input)
                    #response_sent_text_raw = cb.Chatbot_1(chatter_input)
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
    pybot.send_text_message(recipient_id, response)
    return "success"

#---------------Server----------------------



def main():
    """入口程序"""
    import json
    #output= test(json.load(open('params.json')),'你好')
    #print(output)


if __name__ == '__main__':
    #main()
    
    app.run()
