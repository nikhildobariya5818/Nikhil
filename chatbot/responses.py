import random

def get_response(message: str) -> str :
    p_message = message.lower() 

    if p_message =='hello' :
        return 'hey there!'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!help':
        return '`This is a help message the you can modify.`'
    
    return 'I didn\'t understand what you wrote. Try typinf "!help".'
    