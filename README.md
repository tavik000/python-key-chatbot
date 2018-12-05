<p align="center">
  <h1 align="center">Python-Key-Chatbot</h1>
  <p align="center">Facebook Chatbot Application Using Python</p>
</p> 


[![Build Status](https://travis-ci.org/angular/angularfire2.svg?branch=master)]() 

### Keyword
> `Chatbot` `Python` `Webhook` `Facebook Messenger` `RNN` `Generation Based` `Sequence to Sequence` `LSTM` `Chatterbot` `Rule Based` `Task-Specific`


## Contents 
<!-- toc -->
* [Introduction](#introduction)
* [Hybrid Approach​](#hybrid-approach)
* [System Structure](#system-structure)
* [Environment](#environment)
* [Author](#author)
* [Function](#function)
* [Screenshots](#screenshots)
* [Installation](#installation)
    * [Command](#command)
* [Contact](#contact)
* [License](#license)

<!-- toc stop -->

## Introduction

**Important Notice**: This project mix some different other project. You may find that the code is extremely **messy**. Do not expect learning something from here. Thank You!
<br>
<br>
The trained model file is oversized. If you want to try this program, you have to download my trained model file from ... nowhere, contact me please.
<br>
<br>
Our chatbot can reply in real time and it supports multi-lingual conversation (both Chinese and English).
<br><br>  
Our system returns a response using generation-based and rule-based ensemble approaches. Our system is ensembled by two sequence-to-sequence models, one trained by Chinese corpus and another one trained by English corpus. We combined the two sequence-to-sequence models together with the Chatterbot model. The system will check the user input first, if it matches one of the rules we defined, the predefined response will be shown, this is task-specificed framed based system. Otherwise, the user input will be passed into one of the generation-based models we trained or the chatterbot for getting response from one of two system.
<br><br>
Our chatbot can chat freely with users as well as complete tasks like booking a cinema ticket. When the input message is detected to have the keywords “book” and “movie” or "ticket", it will trigger to make the booking cinema ticket services. After then, our chatbot will generate the booking reference number, and ask the related booking ticket contents including name, booking film, booking date and seat No. Finally, the booking information will be saved in to a text file called `cinema_book.txt` and generate a confirmation message to user and ask for confirm.
<br><br>
The chatbot also includes functions like replying by using emojis and telling jokes as well as perform simple calculations.



## Hybrid Approach​

- **Generation based** -  (Sequence to Sequence)​​
- **Rule based** – Chatterbot​
- **Task-Specific Approach** – Frame based
- **Additional Functions ​** – Customized

#### Quick links
- [How to Host a Python and Flask Facebook Messenger Bot on Heroku](https://www.twilio.com/blog/2018/02/facebook-messenger-bot-heroku-python-flask.html) - the project is greater than 2G, cannot use heroku<br>
- [Chatterbot Official Website](http://chatterbot.readthedocs.io) - Rule Based Chatbot<br>
- [ChatLearner](https://github.com/bshao001/ChatLearner) - English Sequence to Sequence Chatbot<br>
- [just_another_seq2seq](https://github.com/qhduan/just_another_seq2seq/tree/master/chatbot) - Chinese Sequence to Sequence Chatbot<br>



## System Structure
System Flow Chart <br>
![image](./ScreenShot/Picture1.png) <br>
Chatbot Tech Stack <br>
![image](./ScreenShot/Picture2.png) <br>
Dataflow between User and Chatbot <br>
![image](./ScreenShot/Picture3.png) <br>
Chatterbot and S2S switching (Now is random) <br>
![image](./ScreenShot/Picture4.png) <br>
![image](./ScreenShot/Picture5.png) <br>



## Environment
- Python: 3.6.7 <br>
- pip: 18.1 <br>
- Flask <br>
- Jieba <br>
- NLTK <br>
- Hanziconv <br>
- Chatterbot <br>
- Tensorflow: 1.7.0 <br>


## Author
- <img src="https://github.com/favicon.ico" width="24">[Key](https://github.com/tavik000) <br>
- [Billy](https://www.linkedin.com/in/billy-hawaii-891297170/) <br>
- [Kenneth] (ckinyi0627@yahoo.com.hk) <br>
- [Baron](https://www.linkedin.com/in/baron-fung-098689142/) <br>

## Function
- Generation based (Sequence to Sequence)​
	1. Chinese chit-chat​
	2. English chit-chat​
- Rule based (Chatterbot)
	1. Chinese chit-chat​
	2. English chit-chat​
	3. Confidence evaluation
- Task-specific Approach (Frame based)​
	1. Booking services for movies​
- Additional functions (Chinese and English)​
	1. Emoji response
	2. Telling Joke
	3. Simple calculation
	4. Provide date and time
	5. Prevent repetitive response
	6. Traditional Chinese compatible

### Using Corpus or Dataset
- Chinese conversation corpus​
- Cleaned reddit data​
- Papaya dataset​
- Cleaned Cornell movie dialogs
- Chatterbot dataset (Simplified Chinese & traditional Chinese)
- Chatterbot dataset (English)







-----


## Screenshots
Feature:

- Time checking <br>
<img src="./ScreenShot/time.png" alt="screenshot" width="200"/>

------

- Replying by emoji <br>
<img src="./ScreenShot/emoji1.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/emoji2.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/emoji3.png" alt="screenshot" width="200"/>

------

- Telling jokes <br>
<img src="./ScreenShot/joke.png" alt="screenshot" width="200"/>

------

- Simple calculations <br>
<img src="./ScreenShot/calculation.png" alt="screenshot" width="200"/>

------

- Chinese chit-chat <br>
<img src="./ScreenShot/cn1.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn2.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn3.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn4.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn5.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn6.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn7.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn8.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/cn9.png" alt="screenshot" width="200"/>

------

- Questions to check and confirm user intent and Framed based Template <br>
<img src="./ScreenShot/book1.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/book2.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/book3.png" alt="screenshot" width="200"/>

------

- English Chitchat Template using Facebook API <br>
<img src="./ScreenShot/fb1.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/fb2.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/fb3.png" alt="screenshot" width="200"/>

------

- Repetitive Detection <br>
<img src="./ScreenShot/rd1.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/rd2.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/rd3.png" alt="screenshot" width="200"/>

------

- English chit-chat <br>
<img src="./ScreenShot/eng1.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng2.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng3.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng4.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng5.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng6.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng7.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng8.png" alt="screenshot" width="200"/>
<img src="./ScreenShot/eng9.png" alt="screenshot" width="200"/>


-----

## Installation


### 1. Clone Repo

```bash
$ git clone git@github.com:tavik000/python-key-chatbot.git
```

### 2. Download the trained model 

Download `basic.data-00000-of-00001` and `chatbot.pkl` from me (Contact me) <tavik002@gmail.com>. 

### 3. Put the file in the right location

locate model file `basic.data-00000-of-00001` to "./Hybrid/chatbot/Data/Result/" 
<br>
locate `chatbot.pkl` to "./Hybrid/chatbot/"

### 4. Build a Facebook App

Check this link to build up a Facebook Messenger Chatbot. You don't need to build up the server, it's already in this program <br>
[How to Host a Python and Flask Facebook Messenger Bot on Heroku](https://www.twilio.com/blog/2018/02/facebook-messenger-bot-heroku-python-flask.html) - in this case, heroku are not applied.

### 5. Modify program

Go to "./Hybrid/chatbot/", modify `test_hybrid.py` file, change ACCESS_TOKEN (line 197) to your Facebook Page token generated in Facebook App (Follow the instruction No.4 then you will know what I mean) and set your own VERIFY_TOKEN (line 198) whatever you like

### 6. Set up python server config

Go to project root folder `python-key-chatbot` and set up your own server config base on your situation

### 7. Run the program and start the server

```bash 
$ python3 app.py
``` 
To run the python server
  
### 8. Set up Facebook Webhook

Go to Facebook for developer website and set up your Webhook, put your server url (you can use a real server or using tools such as [ngrok](https://ngrok.com) or [localtunnel](https://github.com/localtunnel/localtunnel) for boardcast your localhost to Internet and get an url) and VERIFY_TOKEN in the textholder.  <br>
![image](./ScreenShot/fbs.jpg) <br>

### 9. Happy Chatbot 

You are ready to go, test your chatbot by sending it message in Facebook Messenger.



**If you like this, please leave a star.**

-----


## Contact



Email:  Key <tavik002@gmail.com>

-----
## License
MIT License

Copyright (c) 2018 key

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


[⬆ Back to top](#contents)

**All Copyright Reserved**
