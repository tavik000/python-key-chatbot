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

#---------------English Model-------------
import os
import re
from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

sys.path.append('..')


def test(params):
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
    while True:
        user_text = input('Input Chat Sentence:')
        
        if re.search(u'[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC]',user_text)!=None:
            isChinese=True
            user_text =HanziConv.toSimplified(user_text)                    
        else:
            isChinese=False
                                    
        if not isChinese:
            #---------------English Model-------------
            with sess1.as_default():
                with sess1.graph.as_default():
                    print('English model: ')
                    print(re.sub(r'_nl_|_np_', '\n', predictor.predict(session_id, user_text)).strip())
            
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
                        print('Chinese model: ')
                        print('x,xl',x, xl)
                        pred = model_pred.predict(
                            sess2,
                            np.array(x),
                            np.array(xl)
                        )
                        print('pred',pred)
                                    # prob = np.exp(prob.transpose())
                        print('ws_inverse',ws.inverse_transform(x[0]))
                        for p in pred:
                            ans = ws.inverse_transform(p)
                            print('ans',ans)
            

       
'''
        while True:
            user_text = input('Input Chat Sentence:')
            user_text =HanziConv.toSimplified(user_text)            
            if user_text in ('exit', 'quit'):
                exit(0)
            
            
           '''


def main():
    """入口程序"""
    import json
    test(json.load(open('params.json')))


if __name__ == '__main__':
    main()
