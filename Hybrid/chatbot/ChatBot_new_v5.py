# -*- coding: UTF-8 -*-
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
	os.remove("cinema_book.txt")
#	bookings = []
	bookingref = random.randint(0,100000)
	bookingref = str(bookingref)
	out_msg = 'Your Booking number: ' + bookingref + ('. Please enter your last name:')
#	bookings.append(bookingref)
	with open("cinema_book.txt","a", newline='') as myfile:
		write_rec = "Your Booking number: " + bookingref +', '
		myfile.write(write_rec)
	return(out_msg)

def booking_1(message):
	out_msg = 'Please enter your first name: '
	with open("cinema_book.txt","a") as myfile:
		write_rec = "Your name: " + str(message)
		myfile.write(write_rec)
	return(out_msg)

def booking_2(message):
	out_msg = 'Please enter the name of movie you want to watch: '
	with open("cinema_book.txt","a") as myfile:
		write_rec = " " + str(message) + ', '
		myfile.write(write_rec)
	return(out_msg)

def booking_3(message):
	out_msg = 'Please enter the day of the week you want to watch the movie: '
#	while (day not in ['1', '2', '3', '4', '5', '6', '7']):
#		day = input("You input weekday not correct, please try to input again: ")	
	with open("cinema_book.txt","a") as myfile:
		write_rec = "Movie Name: " + str(message) + ', '
		myfile.write(write_rec)
	return(out_msg)

def booking_4(message):
	out_msg = 'Please enter number of the seat you want to reserve: '
#	while ((noofseat.isdigit() == False) or (noofseat.isdigit() == True and int(noofseat) > 50)):
#		if (noofseat.isdigit() == False):
#			noofseat = input("You have input incorrect integer number, please try to input again: ")
#		else:
#			noofseat = input("You have inputted the number exceeds the maxium 50 seats in the cinema, please try to input again: ")	
	with open("cinema_book.txt","a") as myfile:
		write_rec = "Day of the week: " + str(message) + ', '
		myfile.write(write_rec)
	return(out_msg)

def booking_5(message):
	bookings = []
	noofseat = message
	with open("cinema_book.txt","a") as myfile:
		write_rec = "Seat: " + str(message) + '. '
		myfile.write(write_rec)

	with open("cinema_book.txt","r") as myfile:
		out_msg = myfile.read()
	return(out_msg)

def booking_6(message):
	bookings = []
	noofseat = message

	if message.lower()=='yes':
		out_msg = 'Your booking is confirmed. Thank you! :) '
		with open("cinema_book.txt","a") as myfile:
			write_rec = "Confirmed"
			myfile.write(write_rec)
	else:
		out_msg = 'Your booking is canceled. Thank you! :( '
		with open("cinema_book.txt", "a") as myfile:
			write_rec = "Canceled"
			myfile.write(write_rec)
	return(out_msg)

#	with open("cinema.csv","a",newline='') as csvfile:
#		writer = csv.writer(csvfile)
#		writer.writerow(bookings)

def booking_x(message):
	print ("Dear ", forename, surname, ", your booking on the film **", film, "** on day ", day, "with ", noofseat, "people has been confirmed.")
	print ("Thank you for your booking!!!")

	bookings.append(bookingref)
	bookings.append(surname)
	bookings.append(forename)
	bookings.append(film)
	bookings.append(day)
	bookings.append(noofseat)

	with open("cinema.csv","a", newline='') as csvfile:
		writer = csv.writer(csvfile,delimiter='|')
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
	with open('cinema.csv', 'r') as csvfile:
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

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def Chatbot_1(input_msg, language):
	bot.read_only = True

	# repetitiveReply = [
    # 		"This question seems faimilar",
    # 		"You are so boring , let talk something else",
    # 		"boo...boo... Stop . You just asked it",
    # 		"Ok! Next Question",
    # 		"OMG! Can we talk about something else?",
    # 		"I am not answering such a stupid question",
    # 		"Talking with you is damn boring ! Why are you keep asking the same question",
    # 		"Ok ! Stop it , i am done! . Next Question!",
    # 		"Oh! Come on ! Next Question",
    # 		"@#$545$ You! Why are you keep asking. ",
    # 		"This question seems similar to the last message, Let change another Topic,ok?",
    # 		"Sorry, i have already answer this question"
	# ]

	unknownReply = [
    		"😅Sorry, i cannot understnad this question",
            "Sorry,😂 What does it mean? ",
            "I am sorry, 😉I did not catch what you said. ",
            "I am sorry,😘 I did not understand that. say something else please.",
            "I am sorry,😅😅😅 what was that?",
            "What did you😅 say????",
            "What was that?😟",
            "Excuse me?😟 ",
            "What?😐",
	]
	unknownReplyCN = [
		"😅 不懂",
		"😂 什么意思? ",
		"不好意思, 😉 不太明白... ",
		"😘 不明白.",
		"😅😅😅 嗯?",
		"😅 ????",
		"那是什么?😟",
		"你说什么?听不懂 😟 ",
		"什么?😐",
	]

	last_message = ""
	counter=0

	language = (language)
	message = (input_msg)
	if message.strip() != 'Bye':
#		if (func == 1):
#			func = func + 1
#			out_msg = booking_1(message)
#		elif (func == 2):
#			func = func + 1
#			out_msg = booking_2(message)
#		elif (func == 3):
#			func = func + 1
#			out_msg = booking_3(message)
#		elif (func == 4):
#			func = func + 1
#			out_msg = booking_4(message)
#		elif (func == 5):
#			func = 0
#			out_msg = booking_5(message)
#		elif ('cinema' in message.strip()) and ('booking' in message.strip()):
#			func = 1
#			out_msg = booking()
		if (b'\xe9\x9b\xbb\xe5\xbd\xb1'.decode('utf-8') in message.strip()) and (b'\xe9\xa0\x90\xe7\xb4\x84'.decode('utf-8') in message.strip()):
			out_msg = booking_ch()
		elif ('view' in message.strip()) and ('booking' in message.strip()):
			out_msg = view_booking()
		elif (b'\xe9\xa0\x90\xe7\xb4\x84'.decode('utf-8') in message.strip()) and (b'\xe8\xa7\x80\xe7\x9c\x8b'.decode('utf-8') in message.strip()):
			out_msg = view_booking_ch()
		elif ('joke' in message.strip()) and ('tell' in message.strip()):
			out_msg = joking()
		elif (b'\xe7\xac\x91\xe8\xa9\xb1'.decode('utf-8') in message.strip()) and (b'\xe8\xac\x9b'.decode('utf-8') in message.strip()):
			out_msg = joking_ch()
		else:
			if message.strip().lower() != 'bye':
				response = bot.get_response(message)
				if(response.confidence > 0.4):
					out_msg = response
					counter = 0
				elif response.confidence <= 0.4:
					if language == 'eng':
						out_msg = random.choice(unknownReply)
					elif language == 'cn':
						out_msg = random.choice(unknownReplyCN)
					counter += 1
				last_message = message
			if message.strip().lower() == 'bye':
				out_msg = 'Bye'
			if counter >= 5:
				if language == 'eng':
					out_msg = 'I have to go now . Bye Bye!'
				elif language == 'cn':
					out_msg = '完全不懂，走了走了'
	if message.strip() == 'Bye':
		out_msg = 'Bye!'
	return out_msg

#main routine
#func = 0
#while True:
#	Message = input('You:')
##	Message = '你好'
##	Message = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8')
##	print(Message)
#	output = Chatbot_1(Message,func)
#	func = output[1]
#	print('Chatbot: ', output[0], output[1])
#	if Message == 'Bye':
#		break
