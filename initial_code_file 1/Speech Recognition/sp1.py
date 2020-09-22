# Import packages
import speech_recognition as sr
import webbrowser as wb
import datetime
import wikipedia
import os



r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
r4 = sr.Recognizer()

#with sr.Microphone() as source:
#print('WELCOME SIR! WHAT CAN I DO FOR YOU?')
#command()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        print("GOOD MORNING SIR!")
    if(hour>=12 and hour<18):
        print("GOOD AFTERNOON SIR!")
    else:
        print("GOOD EVENING SIR!")

def command():

    global r1,r2,r3,r4

    r1.pause_threshold = 1;
    r2.pause_threshold = 1;
    r3.pause_threshold = 1;
    r4.pause_threshold = 1;

    with sr.Microphone() as source:
        print('Listening....')
        audio = r3.listen(source)


    if 'open YouTube' in r1.recognize_google(audio):
        print("User:",r1.recognize_google(audio))
        r1 = sr.Recognizer()
        url = 'https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            print('What do you want to search?')
            audio = r1.listen(source)

            try:
                get = r1.recognize_google(audio)
                print("User:",get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print('SORRY! COULD NOT UNDERSTAND YOU.')
            except sr.RequestError as e:
                print('failed'.format(e))
        command()

    if 'open Google' in r4.recognize_google(audio):
        print("User:",r4.recognize_google(audio))
        r4 = sr.Recognizer()
        url = 'https://www.google.com/search?q='
        with sr.Microphone() as source:
            print('What do you want to search?')
            audio = r4.listen(source)

            try:
                get = r4.recognize_google(audio)
                print("User:",get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError:
                print('SORRY! COULD NOT UNDERSTAND YOU.')
            except sr.RequestError as e:
                print('failed'.format(e))
        command()

    if 'open Twitter' in r2.recognize_google(audio):
        print("User:",r2.recognize_google(audio))
        r2 = sr.Recognizer()
        url = 'https://twitter.com/'
        try:
            wb.get().open_new(url)
            command()
        except sr.UnknownValueError:
            print('SORRY! COULD NOT UNDERSTAND YOU.')
        except sr.RequestError as e:
            print('failed'.format(e))
    

    if 'open Facebook' in r2.recognize_google(audio):
        print("User:",r2.recognize_google(audio))
        r2 = sr.Recognizer()
        url = 'https://facebook.com/'
        try:
            wb.get().open_new(url)
            command()
        except sr.UnknownValueError:
            print('SORRY! COULD NOT UNDERSTAND YOU.')
        except sr.RequestError as e:
            print('failed'.format(e))
    

    if 'open Instagram' in r2.recognize_google(audio):
        print("User:",r2.recognize_google(audio))
        r2 = sr.Recognizer()
        url = 'https://instagram.com/'
        try:
            wb.get().open_new(url)
            command()
        except sr.UnknownValueError:
            print('SORRY! COULD NOT UNDERSTAND YOU.')
        except sr.RequestError as e:
            print('failed'.format(e))


    if 'Wikipedia' in r2.recognize_google(audio):
        print("User:",r2.recognize_google(audio))
        r2 = sr.Recognizer()

        try:
            results = wikipedia.summary(r2.recognize_google(audio), sentences=2)
            print(results)
            command()
        except sr.UnknownValueError:
            print('SORRY! COULD NOT UNDERSTAND YOU.')
        except sr.RequestError as e:
            print('failed'.format(e))

    
    if 'play movie' in r2.recognize_google(audio):
        print("User:",r2.recognize_google(audio))
        print('Which movie do you like to be played?')
        r2 = sr.Recognizer()
        if 'arrival' in r2.recognize_google(audio):
            print("User:",r2.recognize_google(audio))
            r2 = sr.Recognizer()
            movie_dir = 'F:\\Arrival (2016)'
            movie = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movie[0]))
        if 'avengers end game' in r2.recognize_google(audio):
            print("User:",r2.recognize_google(audio))
            r2 = sr.Recognizer()
            movie_dir = 'F:\\Avengers - End Game (2019)'
            movie = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movie[0]))

        

    if 'close' in r2.recognize_google(audio):
        print("User:",r2.recognize_google(audio))
        print("THANK YOU SIR! HAVE A NICE DAY!")
        
def main(): 
    wish_me()
    print('I AM ANITALK. WHAT CAN I DO FOR YOU?')
    command()
  
if __name__=="__main__": 
    main() 



