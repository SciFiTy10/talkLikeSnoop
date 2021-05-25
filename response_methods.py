from build_methods import build_PlainSpeech, build_SimpleCard, build_Reprompt, build_response 
from messages import reprompt

def statement(title, body, shouldEndSession):
    #speechlet is a dictionary that will be turned into a JSON object
    speechlet = {}
    #build_PlainSpeech builds the OutputSpeech object
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    #builds a Card object
    speechlet['card'] = build_SimpleCard(title, body)
    #I think before here I need to build a reprompt
    speechlet['reprompt'] = build_Reprompt(reprompt())
    #set to False
    speechlet['shouldEndSession'] = shouldEndSession
    #builds the Response body
    return build_response(speechlet)