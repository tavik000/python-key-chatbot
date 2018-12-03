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
import ChatBot_new_v5 as cb

#--------------Chatterbot---------------------

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

sys.path.append('..')


ws = pickle.load(open('ws.pkl', 'rb'))


def build_model(params):
    from sequence_to_sequence import SequenceToSequence
    from word_sequence import WordSequence # pylint: disable=unused-variable
    
    #---------------English Model-------------
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
    res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')
    
    #---------------Chinese Model-------------
    x_data, _ = pickle.load(open('chatbot.pkl', 'rb'))

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
    
    return sess1,sess2,predictor,session_id,model_pred
    
def test(sess1,sess2,predictor,session_id,model_pred,user_text,language):
    from data_utils import batch_flow
    """测试不同参数在生成的假数据上的运行结果"""
   
    #call function
    #while True:
        #user_text = input('Input Chat Sentence:')
    language = (language)
    if re.search(u'[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC]',user_text)!=None:
        isChinese=True
        user_text =HanziConv.toSimplified(user_text)                    
    else:
        isChinese=False
                                    
    if not isChinese:
            #---------------English Model-------------
        with sess1.as_default():
            with sess1.graph.as_default():
                random_int= random.randint(0,100)
                


                if random_int>=20:
                    print('chatlearner Eng S2S')
                    output_chatlearner = re.sub(r'_nl_|_np_', '\n', predictor.predict(session_id, user_text)).strip()
                    return output_chatlearner
                else:
                    print('chatterbot Eng')
                    output_chatterbot = cb.Chatbot_1(user_text,language)
                    output_chatterbot = str(output_chatterbot)
                    output_chatterbot = output_chatterbot.replace('-', '')
                    return output_chatterbot
                                          
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
                    
                    random_int= random.randint(0,100)
                                        




                    if random_int > 20:
                        print('just another CN S2S')
                        output_justanother = ''.join(ans).replace('</s>', '')
                        return output_justanother
                    else:
                        print('chatterbot CN')
                        output_chatterbot = cb.Chatbot_1(user_text,language)
                        output_chatterbot = str(output_chatterbot)
                        output_chatterbot = output_chatterbot.replace('-', '')
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

sess1,sess2,predictor,session_id,model_pred= build_model(json.load(open('params.json')))
print('# Program Init')

pybot = PYBot (ACCESS_TOKEN)

booking_step = 0
repetive_time = 0
last_message = ""
language = ""
repetitiveReply = [
            "This question seems faimilar 😅",
            "You are so boring , let talk something else 😂",
            "boo...boo... Stop . You just asked it 😏",
            "😏Ok! Next Question",
            "OMG!😖 Can we talk about something else?",
            "😩I am not answering such a stupid question",
            "Talking with you is damn boring !😓 Why are you keep asking the same question",
            "Ok ! Stop it , i am done! . Next one!",
            "Oh! Come on ! Next Question😏",
            "@#$545$ You!😩 Why are you keep asking. ",
            "This question seems similar to the last message, Let change another Topic,ok?😅",
            "Sorry, i have already answer this question😜"
            "Are you feeling good to fool me?",
            "Is your life always repetitive like saying the same thing?",
            ":( Farily well, are you a chatbot?"
]

repetitiveReplyCN = [
            "可以说点别的吗 😅",
            "真无聊，说点别的吧 😂",
            "你刚说过了 😓",
            "😏这样重复没有意思",
            "😖 可以说点别的吗?",
            "你的人生难道就跟你说的话一样重复吗？ 😳",
            "有意思吗？😓",
            "你难道是机器人🤖？",
            "😑",
            "😑 看来我要考虑无视你了. ",
            "说点别的？ 😅",
            "😜呵呵"
            "你当我是机器人吗？",
            "😧",
            ":( 净说同样的话.."
]

# unknownReply = [
#             "Sorry, i cannot understnad this question",
#             "Sorry, What does it mean? ",
#             "I am sorry, I did not catch what you said. Could you repeat it ",
#             "I am sorry, I did not understand that. say something else please. ",
#             "I am sorry, what was that?",
#             "What did you say?",
#             "What was that?",
#             "Excuse me? ",
#             "What?",
# ]
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
          if ('message' in messaging[0]):
              for message in messaging:
                if message.get('message'):
                    #Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    #Detect input is not from chatbot
                    if recipient_id != '1594483620652493':
                        if message['message'].get('text'):
        #                   response_sent_text = get_message()
                            global booking_step,last_message,repetive_time
                            chatter_input = message['message'].get('text')
                            print('user input: ',chatter_input)

                            if re.search(u'[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC]', chatter_input) != None:
                                language = "cn"
                            else:
                                language = "eng"

                            # print('booking step: ',booking_step)
                            if ('movie ticket' in chatter_input.lower()) and ('book' in chatter_input.lower()):
                                booking_step = 1
                                print('booking step after: ',booking_step)
                                response_sent_text = cb.booking()
                            elif (booking_step == 1):
                                booking_step=booking_step+1
                                response_sent_text = cb.booking_1(chatter_input)
                            elif (booking_step == 2):
                                booking_step=booking_step+1
                                response_sent_text = cb.booking_2(chatter_input)
                            elif (booking_step == 3):
                                booking_step=booking_step+1
                                response_sent_text = cb.booking_3(chatter_input)
                            elif (booking_step == 4):
                                booking_step=booking_step+1
                                response_sent_text = cb.booking_4(chatter_input)
                            elif (booking_step == 5):
                                booking_step = booking_step + 1
                                response_sent_text = str(cb.booking_5(chatter_input)) + '\r\n Do you confirm the above booking is correct?'
                            elif (booking_step == 6):
                                booking_step = 0
                                response_sent_text = cb.booking_6(chatter_input)
                            elif ('how' in chatter_input.lower()) and ('feel' in chatter_input.lower()):
                                feelings= ["I am happy :D",
                                "I feel excited :P",
                                "I feel good ;)",
                                "Great today ^_^",
                                "Not so much -_-",
                                "I don't have any emotion maybe o.O",
                                "I feel roboty :|]"]
                                response_sent_text = str(random.choice(feelings))
                            else:
                                if cb.similar(chatter_input, last_message) > 0.7:
                                    repetive_time = repetive_time + 1
                                    if language == 'eng':
                                        response_sent_text = str(random.choice(repetitiveReply))
                                    elif language == 'cn':
                                        response_sent_text = str(random.choice(repetitiveReplyCN))
                                elif chatter_input == last_message:
                                    if language == 'eng':
                                        response_sent_text = str(random.choice(repetitiveReply))
                                    elif language == 'cn':
                                        response_sent_text = str(random.choice(repetitiveReplyCN))
                                    repetive_time = repetive_time + 1
                                else:                                                            
                                    response_sent_text_raw = test(sess1,sess2,predictor,session_id,model_pred,chatter_input,language)
                                    #response_sent_text_raw = cb.Chatbot_1(chatter_input)
                                    response_sent_text = str(response_sent_text_raw)
                                    repetive_time = 0
                                last_message = chatter_input
                                if repetive_time < 2:
                                    print(response_sent_text)
                                else:
                                    print("Repetive over 2 time, no response.")

                            if repetive_time < 2:
                                #Chatbot reply
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
    output= test(sess1,sess2,predictor,session_id,model_pred,'can you help me book a movie ticket')
    print(output)



if __name__ == '__main__':
#    main()

    app.run()
