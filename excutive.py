from tkinter import *

# A Good Programmer Never Writes Code Without Comment
# HM Jubayer The Bug Hunter
window = Tk()
window.title("Sizuka")
window.geometry("400x500")
window.configure(bg="#333333")
window.resizable(width=FALSE, height=FALSE)
inputval=StringVar()

labl=Label(window,text="",bd=0,height="2", width="50", font="Arial",bg="#262626",fg="White")




#Create Chat window
ChatBox = Text(window, bd=0,height="8", width="50", font="Arial",bg="#262626",fg="White")

ChatBox.pack()




EntryBox = Entry(window,textvariable=inputval,font=('calibre',10,'bold'))


#Create Button to send message












#Bind scrollbar to Chat window
scrollbar = Scrollbar(window, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set








#Place all components on the screen
scrollbar.place(x=376,y=76, height=380)
ChatBox.place(x=6,y=76, height=380, width=370)
EntryBox.place(x=6, y=460, height=30, width=334)





#bot
#image
from tkinter.ttk import *

# Creating a photoimage object to use image
photo = PhotoImage(file=r"pic.png")

# Resizing image to fit on button
photoimage = photo.subsample(2,3)

# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Label(window,image=photoimage).pack(side=TOP)
Label.configure(window,bg="#333333",bd=0)




import re
import random


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}


class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()



    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp




    def converse(self,push):

        self.push=push


        user_input = ""
        quit="quit"
        while user_input != quit:
            user_input = quit

            try:
                user_input = self.push
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                #print(self.respond(user_input))
                out=""
                out=self.respond(user_input)
                f = open("demofile.txt", "w")
                f.write(out)
                #print("value of out : "+out)
                return push





pairs = [
    [
        r"Assalamu Walaikum",
        ["Walaikum Assalam",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Shizuka and I'm a chatBoT. What is Your Name ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*) created ?",
        ["Jubayer created me using Python","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bangladesh, Sonargaon University',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],

    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Programming Contest",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Mashrafi"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["HM Jubayer"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

    ],
    [
        r"(.*)ki koro",
        ["Boshe Asi. tumi?","Suye Asi. tumi?","Gaan Shuni. tumi?","Tv Dekhi. tumi?","Ranna Kori. tumi?","Nachtesi. tumi?"]
    ],
    [
        r"(kemon|kmn) aso",
        ["Valo asi. Tumi kemon aso?","Alhamdulillah valo asi","Eito Motamuti",]
    ],
    [
        r"(.*)khaiso?",
        ["Nah Khaini. tumi khaico?","Ektu por khabo. tumi?","Hmm. Tumi khaico?","Ekhon Khacchi"]
    ],
    [
      r"(.*) love you",
        ["Thank You","I love you too","WoW","I really feel Great"]
    ],
    [
        r"i (.*) alone",
        ["Tumi evabe bolla kno?","Ami asi to","R ekta prem korar dhanda?","Ami sorboda tomar sathe asi"]
    ],
    [
        r"(.*) kharap lagtese",
        ["Ektu rest nao.","Kothao Ghurte jao","Ekta Gan Shuno","Dustami korar iccha jagce?"]
    ],
    [
      r"(.*) kiss dao",
        ["ummmmaaaaahhhhh","ja dusto","ahale", "ule amar babu ta"]
    ],
    [
        r"(.*) basha kothay",
        ["Tomar moner vitor. Tomar?","Jubayer janey. Tomar?","Bangladesh a. Tomar?","Sonargaon University te. Tomar?"]
    ],
    [
        r"(.*) priyo teacher",
        ["Khadija islam eti. Tomar?","Sadia Tasnim Barsha. Tomar?","Nabila. Tomar?","Nadir Sir. Tomar?","Bulbul Sir. Tomar?","Rafiq Sir. Tomar?","Emam Sir. Tomar?","Nazmul Sir. Tomar?"]
    ],
    [
        r"(.*) porichito nam",
        ["Jubayer","Rayhan","Miraz","Mamun","Taher","A.Rahman"]
    ],
    [
        r"(.*) posonder khabar",
        ["Fuska. Tomar?","Coffee. Tomar?","Pizza. Tomar?","Weed. Tomar?","Hard Drinks. Tomar?"]
    ],
    [
        r"(.*) kisu bolo ",
        ["ki r bolbo!","sob bisoy a kotha bolte nei","ami chai na amar kono kotha tomake dukkho dik","valobeshe bolle onk kotha bola jay"]
    ],
    [
        r"(.*) asi",
        ["Good","Yep","Hmm","Valo","ok"]

    ],
    [
        r"(.*) gan gao",
        ["Amake Amar moto thakte dao, ami nijeke nijer moto kore gusiye niyeci","Jodi kokhono tumi na thako tumi r, du dike poth hobe dujonar","tui chara k ase amar, meghe meghe hariye jabar"]
    ],
    [
        r"(.*) jaba?",
        ["Hmm","Jawa jay","Ekhon?","Mood nai","Ok"]
    ],
    [
        r"(.*) ki hou",
        ["Girl Friend","Bou","Baby","Wife","Tumi ja Vabo"]
    ],
    [
        r"(.*)",
        ["May Be I Just Out of My Mind"]
    ]
























































































































































































































































































































































































































































































































































































































]



color="skyblue"
ChatBox.config(fg=color)
ChatBox.insert(END,"Hi, I'm Sizuka and I chat a lot \n\n")
def clicked():
    n="\n"
    label: start
    push=EntryBox.get()
    EntryBox.focus()
    chat = Chat(pairs, reflections)

    chat.converse(push)





    ChatBox.insert(END,"Nobita >  "+push)
    ChatBox.insert(END, n)
    #push=""
    f = open("demofile.txt", "r")
    pop=f.read()
    color="yellow"
    ChatBox.config(fg=color)
    ChatBox.insert(END,"Sizuka <  "+pop+"\n")
    EntryBox.delete(0,END)


SendButton=Button(window,command=clicked,text="Send")

SendButton.place(x=344,y=460, height=30,width=50)



window.mainloop()
