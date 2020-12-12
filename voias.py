'''
	This is a simple voice based, assistant where we can use the basic concepts of programming for building something fun.
'''

# Import the required packages
import speech_recognition as sr
import os
import time
import schedule
from modules import open_mail, read_time

# Initi. the speech recognition module
r = sr.Recognizer()

# Give a welcome message
os.system("espeak ' Hello BOSS. I am voias, I am your simple personal assistant, how can i help you' - s 60")		    

# First while loop for triggering our assistant
while True:
	# Init, the microphone setting for listening the voice input from the user.

	with sr.Microphone(device_index = 0, sample_rate = 48000, chunk_size = 1024) as source1:
		r.adjust_for_ambient_noise(source1)
		audio = r.listen(source1)
		print("Listened your command, please wait i'm processing it")	

	try:
		trigger_word = r.recognize_google(audio)
		print(trigger_word)

		#check for the trigger word.
		if trigger_word == "okay" or trigger_word == "ok":
			print(trigger_word)
			print("Triggering VOIAS")

		if trigger_word == "buy" or trigger_word== "bye" or trigger_word== "end" :
			os.system("espeak 'Any time at your service' - s 60")
			os.system("espeak 'have a good day' - s 60")
			break


		# Second loop for getting the command form the user.

		while trigger_word=="okay" or trigger_word == "ok":
			print("Please give your command")
			os.system("espeak 'triggered Voias, please give your command.' - s 60")		
			ir = sr.Recognizer()
			with sr.Microphone(device_index = 0, sample_rate = 48000, chunk_size = 1024) as source:
				ir.adjust_for_ambient_noise(source)		
				audio = ir.listen(source)
				print ("Listened, please wait I'm processing it......")
			res = ir.recognize_google(audio)
			print(res)
			os.system("espeak 'Listened please wait i'm processing it' - s 60")
			if res == "mail":
				os.system("espeak 'Opening the mail BOSS'")
				open_mail()
			if res == "time":
				message = "espeak " + "'"+"time is "+str(read_time()) +"'"
				os.system(message)
			if res=="thank you":
				os.system("espeak 'Thanks for using'")
				break
			re= "espeak "+ "'"+res+"'"+" -s 60"
			os.system(re)
	except sr.RequestError:
		os.system("espeak 'request error' -s 80")
	except sr.UnknownValueError as e:
		print(e)
		os.system("espeak 'unable to understant' ")
	schedule.run_pending()
	time.sleep(1)	
