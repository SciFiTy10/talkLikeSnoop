from random import randint 

#random welcome
def welcome():
    #create an array of welcome messages
    welcomeMessages = ["What up nephew? It's the dogfather himself big Snoop Dogg. Start your response with either \"Say\" or \"Translate\" followed by a few words and I'll translizzle them for you", \
    "You already know its the S., N., double O. P., D O double G big snoop dogg! Respond with either \"Say\" or \"Translate\" followed by a phrase and I'll show you how to talk like Snoop", \
    "What up cuzz, it's uncle snoop dizzle. Use the word \"Say\" or \"Translate\" followed by a phrase and I'll translizzle it for you"]
    #get the length of the array
    arrayLength = len(welcomeMessages)
    #create a randomIndex number for our array of welcome messages
    randomIndex = randint(0, arrayLength - 1)
    #choose the welcome message at random
    welcome = welcomeMessages[randomIndex]

    #return this value to the welcome body
    return welcome

#function for reprompt phrases
def reprompt():
    #create an array of welcome messages
    repromptMessages = ["Speak the word \"Say\" or \"Translate\" followed by your phrase and I'll drop a translizzle like it's hizzle", \
    "Word to Pharrell, if you respond with \"Say\" or \"Translate\" before you say your phrase, I'll tell you how Big Snoop would say it"]
    #get the length of the array
    arrayLength = len(repromptMessages)
    #create a randomIndex number for our array of welcome messages
    randomIndex = randint(0, arrayLength - 1)
    #choose the welcome message at random
    reprompt = repromptMessages[randomIndex]

    #return this value to the welcome body
    return reprompt