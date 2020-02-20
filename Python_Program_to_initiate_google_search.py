import speech_recognition as sr
import webbrowser as wb

chrome_path='C:/Program Files (x86)/Google/Chrome?application?chrome.exe %s'

r=sr.Recognizer()

with sr.Microphone() as source:
	print('Say something!')
	audio=r.listen(source)
	print('Searched!')
try:
	text=r.recongnize_google(audio)
	print('Google thinks you said:\n'+text)
	f_text='https://www.google.co.in/search?q='+text
	wb.get(chrome_path).open(f_text)
except Exception as e:
	print(e)