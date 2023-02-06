import random
import discord
import wolframalpha
import creds

help = 'To ask a question: q "question"'

def get_response(message: str) -> str:

    p_message = message.lower()
    l_msg = p_message.split()
    
    if '1071561802808303666' in message:
        for i in l_msg:
            if i in ['hi', 'hey', 'sup', 'yo', 'hello', 'wsup', 'wassup']:
                return i
        return help

    if message == 'roll':
        return str(random.randint(1, 6))

    if list(message)[0] == 'q':
        
        question = message[1:]


        client = wolframalpha.Client(creds.app_id)

        res = client.query(question)
            
        answer = next(res.results).text

        return answer

            
    

