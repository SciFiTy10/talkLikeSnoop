from vowels import vowels
from stop_words import stop_words   

#function for editing from the beginning of the word
def forward_insert(word):
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

#function for editing from the back of the word
def backward_insert(word):

    #create variables for getting the last letters of different cases
    lastFiveLetters = word[len(word)-5:len(word)]
    lastFourLetters = word[len(word)-4:len(word)]
    lastThreeLetters = word[len(word)-3:len(word)]
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

#main conversion function
def convert_to_snoop(words):

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
                word = forward_insert(word)
                #insert that word back into it's proper place
                words[i] = word
                #skip to the next word
                continue
            #otherwise the word is 7 or more letters
            else:
                #add izz into the word
                word = backward_insert(word)
                #insert that word back into it's proper place
                words[i] = word
                #skip to the next word
                continue
    #return the words split by a string
    return " ".join(words)     