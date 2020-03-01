#-----------------------------------------------------------------------------------------------------------------------------------------
#  Author: Timcuin Erbas
#  Date: December 26, 2019
#
#  Summary: This is a program that learns how to respond to different things as it speaks to people. The logic is quite simple.
#  If the program does not know how to respond to something, it asks the user. It records all responses under a dictionary, and
#  randomly selcets a response for what the user has asked it. It makes sense. The most common response to the ChatBot's questions
#  will be the most common response to the user's questions.
#
#-----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------
#  Import Necessary Packages
#-----------------------------------------------------------------------------------------------------------------------------------------

import time
import random

#-----------------------------------------------------------------------------------------------------------------------------------------
#  Print the instructions on how to use into the console. Make the console look nice.
#-----------------------------------------------------------------------------------------------------------------------------------------

print("Hello, I am some sort of a learning machine.")
time.sleep(3)
print("I learn responses to different things as people speak to me.")
time.sleep(3)
print("Type in DONE when you are done talking to me.")
time.sleep(3)
print("I want to learn as best as possible so please be careful to be gramatically correct.")
time.sleep(3)
print("-----------------------------------------------------------------------------------------------------------")
print("Lets Begin!")
print("-----------------------------------------------------------------------------------------------------------")
print("BOT: Hello")

#-----------------------------------------------------------------------------------------------------------------------------------------
#  This is the function that records the fetches an appropriate response to the user's words.
#-----------------------------------------------------------------------------------------------------------------------------------------

def findResponse(res):
        tarword = False
        f = open("ChatBotData.csv", "r")
        data = f.readlines()
        for line in data:
                linesplit = line.split("*")
                if linesplit[-1].rstrip() == res:
                        tarnum = random.randint(0,len(linesplit)-2)
                        tarword = linesplit[tarnum]
                robres = tarword
        return robres


#-----------------------------------------------------------------------------------------------------------------------------------------
#  This is the function that records the response of the user in an appropriate spon in the dictionary.
#-----------------------------------------------------------------------------------------------------------------------------------------

def putInCsv(linenum, text):
        with open("ChatBotData.csv", "r") as b:
                lines = b.readlines()
        with open("ChatBotData.csv", "a") as b:
                for i,line in enumerate(lines):
                        b.write(line)
                        if i == linenum:
                                b.write(text)
                                b.close()

#-----------------------------------------------------------------------------------------------------------------------------------------
#  This is main, where all of the function calling happens, the program where the ChatBot responds and the user can too.
#-----------------------------------------------------------------------------------------------------------------------------------------

while True:
        response = input("YOU: ")
                if response == "DONE":
                time.sleep(3)
                print("BOT: It was fun talking to you!")
                time.sleep(3)
                print("BOT: I have learned a lot today!")
                time.sleep(3)
                print("BOT: Thank you!")
                break

        else:
                roboresponse = findResponse(response)
                if roboresponse == False:
                        print("BOT: I do not know how to respond to that.")
                        print("BOT: Please write what a human would say in response:")
                        humresp = input(":::: ")
                        f = open("ChatBotData.csv", "a")
                        f.write(str(humresp) + "*" + str(response))
                        f.write("\n")
                         f.close()
                else:
                        time.sleep(4)
                        print("BOT: "+ str(roboresponse))
                        f = open("ChatBotData.csv")
                        data = f.readlines()
                        l = 0
                        for line in data:
                                linestr = line.split("*")
                                if linestr[-1] == response:
                                        putInCsv(l, str(response))
                                l += 1
print("-----------------------------------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------------------------------------------------
#  END OF PROGRAM
#---------------------------------------------------------------------------------------------------------------------------------------
