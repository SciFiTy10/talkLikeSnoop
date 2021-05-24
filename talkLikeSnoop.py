#imports
from random import randint

#set of stop words that will be applied
stop_words = ['me', 'much', 'my', 'many', 'myself', 'we', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that','these','those', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'the', 'but', 'if', 'because', 'while', 'by', 'for', 'with', 'between', 'through', 'during', 'before', 'below','to', 'two', 'from', 'down', 'further', 'then','here','there', 'when', 'where', 'why', 'how', 'both','few', 'more', 'most', 'some', 'such','no', 'nor', 'not', 'same', 'so', 'than', 'too', 'very', 'can', 'will','just', 'should','now', 'won']

vowels = ["a", "e", "i", "o", "u", "y"]

#function for editing from the back of the word
def backwardInsert(word):

    #var for lastFiveLetters
    lastFiveLetters = word[len(word)-5:len(word)]
    #var for lastFourLetters
    lastFourLetters = word[len(word)-4:len(word)]
    #var for lastThreeLetters
    lastThreeLetters = word[len(word)-3:len(word)]
    #var for lastTwoLetters
    lastTwoLetters = word[len(word)-2:len(word)]

    #check cases for tion 
    if 'ation' == lastFiveLetters:
        #get the index of the letters
        index = word.index('ation')
        #insert ayshizzle into at that index
        word = word[:index] + 'ayshizzle'
        return word
    if 'etion' == lastFiveLetters:
        #get the index of the letters
        index = word.index('etion')
        #insert eeshizzle into at that index
        word = word[:index] + 'eeshizzle'
        return word
    if 'ition' == lastFiveLetters:
        #get the index of the letters
        index = word.index('ition')
        #insert ishizzle into at that index
        word = word[:index] + 'ishizzle'
        return word
    if 'otion' == lastFiveLetters:
        #get the index of the letters
        index = word.index('otion')
        #insert ohshizzle into at that index
        word = word[:index] + 'ohshizzle'
        return word
    if 'ution' == lastFiveLetters:
        #get the index of the letters
        index = word.index('ution')
        #insert ooshizzle into at that index
        word = word[:index] + 'ooshizzle'
        return word
    if 'tion' == lastFourLetters:
        #get the index of the letters
        index = word.index('tion')
        #insert ooshizzle into at that index
        word = word[:index] + 'shizzle'
        return word
    #check special case if ending is "ght"
    if 'ght' == lastThreeLetters:
        #loop through each word from the end to the beginning
        for e in range(len(word) - 4, -1, -1):
            #if the letter is a consonant
            if word[e] not in vowels:
                #get the index of the letter
                index = word.rfind(word[e+1])
                #insert the izz into at that index
                word = word[:index] + 'izz' + word[index:]
                #break the loop
                break
        return word  
    #check special case if ending is "ing"
    if 'ing' == lastThreeLetters:
        #loop through each word from the end to the beginning
        for e in range(len(word) - 4, -1, -1):
            #if the letter is a consonant
            if word[e] not in vowels:
                #get the index of the letter
                index = word.rfind(word[e+1])
                #insert the izz into at that index
                word = word[:index] + 'izzling'
                #break the loop
                break
        return word
    #handle whether last two letters "es"
    if 'es' == lastTwoLetters:
        #loop through each word from the end to the beginning
        for e in range(len(word) - 3, -1, -1):
            #if the letter is a consonant
            if word[e] not in vowels:
                #get the index of the letter
                index = word.rfind(word[e+1])
                #insert the izz into at that index
                word = word[:index] + 'izzles'
                #break the loop
                break
        return word
    #handle whether last two letters "ed"
    if 'ed' == lastTwoLetters:
        #loop through each word from the end to the beginning
        for e in range(len(word) - 3, -1, -1):
            #if the letter is a consonant
            if word[e] not in vowels:
                #get the index of the letter
                index = word.rfind(word[e+1])
                #insert the izz into at that index
                word = word[:index] + 'izzled'
                #break the loop
                break
        return word
    #check special case if ending is "sh"
    if 'sh' == lastTwoLetters:
        #loop through each word from the end to the beginning
        for e in range(len(word) - 3, -1, -1):
            #if the letter is a consonant
            if word[e] not in vowels:
                #get the index of the letter
                index = word.rfind(word[e+1])
                #insert the izz into at that index
                word = word[:index] + 'izz' + word[index:]
                #break the loop
                break
        return word 
    #handle whether last two letters are consonant then vowel
    if  (lastTwoLetters[0] not in vowels) & (lastTwoLetters[1] in vowels):
            #get the index of the letter
            index = word.index(word[len(word)-1])
            #insert the izz into at that index
            word = word[:index] + 'izzle'    
            return word
    #handle whether last two letters are both consonants
    if  (lastTwoLetters[0] not in vowels) & (lastTwoLetters[1] not in vowels):
            #if the last letter is an s
            if lastTwoLetters[1] == 's':
                #get the index of the letter
                index = word.index(word[len(word)-1])
                #insert the izz into at that index
                word = word[:index] + 'izzles'
            else:
                #insert the izz into at that index
                word = word + 'izzle'    
            return word
    else:
        for e in range(len(word) - 3, -1, -1):
            #if the letter is a consonant
            if word[e] not in vowels:
                #get the index of the letter
                index = word.rfind(word[e+1])
                #insert the izz into at that index
                word = word[:index] + 'izzle'
                #break the loop
                break
        return word
    
    
#function for editing from the beginning of the word
def forwardInsert(word):
    #start the loop at the beginning and add izz in front of the first vowel
    for letter in word:
        #if the letter is a vowel
        if(letter in vowels):
            #get the index of the letter
            index = word.index(letter)
            #insert the izz into at that index
            word = word[:index] + 'izz' + word[index:]
            #break the loop
            break
    return word


def convertToSnoop(words):

    #loop through words and get each individual word
    for i in range(len(words)):
        #get the word from the words list
        word = words[i]

        #check to see if the word is a stop word
        if word in stop_words:
            #skip to the next word
            continue

        #check to see if the first letter is a vowel
        if word[0] in vowels:
            #skip to the next word
            continue
        #check if word is "sure"
        if word == 'sure':
            word = 'shizzle'
            continue
        #else the word begins with a consonant
        else:
            #get the length of the word
            lengthOfWord = len(word)

            #check if the length is < 7 letters
            if lengthOfWord < 7:
                #add izz into the word
                word = forwardInsert(word)
                #insert that word back into it's proper place
                words[i] = word
                #skip to the next word
                continue
            #otherwise the word is 7 or more letters
            else:
                #add izz into the word
                word = backwardInsert(word)
                #insert that word back into it's proper place
                words[i] = word
                #skip to the next word
                continue
    #return the words split by a string
    return " ".join(words)           


##############################
# Welcome Messages
##############################

#random welcome
def welcomeToTalkLikeSnoop():
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
def repromptTalkLikeSnoop():
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


##############################
# Program Entry
##############################

#lambda_handler - this is like main()
def lambda_handler(event, context):
    #event is a python dictionary
    #LaunchRequest is an object that means the user made a request to a skill, but didn't specify the intent
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)

##############################
# On Launch
##############################

#on_launch
#should make a call to a customer welcome title and speech in the second parameter
def on_launch(event, context):

    #change this title to reflect the skill
    #call another function to work with the welcome portion of the skill
    #for the 2nd parameter
    
    #passing false on_launch
    shouldEndSession = False
    return statement("Welcome to the TalkLikeSnoop Skill!", welcomeToTalkLikeSnoop(), shouldEndSession)

##############################
# Responses
##############################

#statement is a helper function that builds a response
#it takes a title and body to build the spoken and card output
def statement(title, body, shouldEndSession):
    #speechlet is a dictionary that will be turned into a JSON object
    speechlet = {}
    #build_PlainSpeech builds the OutputSpeech object
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    #builds a Card object
    speechlet['card'] = build_SimpleCard(title, body)
    #I think before here I need to build a reprompt
    speechlet['reprompt'] = build_Reprompt(repromptTalkLikeSnoop())
    #set to False
    speechlet['shouldEndSession'] = shouldEndSession
    #builds the Response body
    return build_response(speechlet)


##############################
# Builders
##############################

#this builds the outputSpeech object
def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech

#will need to create an array for possible stuff to say
#may need to erase body as a caught parameter
#may need to handle multiple different calls depending on whether this follows open or intent
def build_Reprompt(body):
    reprompt = {}
    reprompt['outputSpeech'] = build_PlainSpeech(body)
    return reprompt

def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card

#this is called at the end of the statement function
def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response

##############################
# Routing
##############################

#if a specific intent is selected, this is where that logic is routed
def intent_router(event, context):
    intent = event['request']['intent']['name']
    

    # Custom Intents
    if intent == "talkLikeSnoop":
        return talkLikeSnoop_intent(event, context)


##############################
# Required Intents
##############################
    # Required Intents
    if intent == "AMAZON.CancelIntent" or intent == "AMAZON.StopIntent":
        #set shouldEndSession to true
        shouldEndSession = True
        return statement("Thanks for hanging nephew, uncle snoop will catch you on the flip side!", "Thanks for hanging nephew, uncle snoop will catch you on the flip side!", shouldEndSession)
    if intent == "AMAZON.HelpIntent" or intent == "AMAZON.NavigateHomeIntent":
        #set shouldEndSession to False
        shouldEndSession = False
        return statement("Make sure you use the word \"Say.\" or \"Translate.\" before your phrase to have snoop translizzle what you say", "Make sure you use the word \"Say.\" or \"Translate.\" before your phrase to have snoop translizzle what you say", shouldEndSession)
    # if intent == "AMAZON.StopIntent":
    #     return stop_intent()


##############################
# Custom Intents
##############################

def talkLikeSnoop_intent(event, context):
    #get the user's input
    words = event['request']['intent']['slots']['customerQuery']['value']

    #get all of the individual words from the user's input
    words = words.split(" ")

    #set a variable to catch convertedString after passing words through convertToSnoop
    convertedString = convertToSnoop(words)
    
    #make sure this loops
    shouldEndSession = False
    
    #print this to the user
    return statement("Snoop says", convertedString + "\n\n " + repromptTalkLikeSnoop(), shouldEndSession)