import datetime
import openai
import speech_recognition as sr
import os
import webbrowser
from config import apikey

chatStr = ""
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Sir : {query}\n Mavrik: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")

    # with open(f"Openai/{prompt[1:]}.txt", "w") as f:
    #     f.write(text)
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt}\n ****************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response['choices'][0]['text'])
    text += response['choices'][0]['text']
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{prompt[1:]}.txt","w") as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Listening...")
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry didn't get you"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Mavrik")
    while True:
        say("What can I do for you sir..")
        query = take_command()
        if "open".lower() in query.lower():
            try:
                sites = [["youtube", "https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["saavn","https://www.saavn.com"],["spotify"],["https://www.spotify.com"]]
                for site in sites:
                    if f"{site[0]}".lower() in query.lower():
                        say(f"Opening {site[0]} sir...")
                        webbrowser.open(site[1])
                    else:
                        say("I cant open that site")
            except Exception as e:
                say("I cant open that site")

        elif "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        elif "using ai".lower() in query.lower():
            ai(prompt=query)

        elif "stop".lower() in query.lower():
            say("Ok sir Bye")
            exit()


        # say(text)