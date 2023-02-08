import discord
import wolframalpha
import creds
import requests
from bs4 import BeautifulSoup

help = 'To ask a question: q "question"\n To check the price of a stock: price "stock symbol"'

def get_response(message: str) -> str:

    p_message = message.lower()
    l_msg = p_message.split()
    
    if '1071561802808303666' in message:
        for i in l_msg:
            if i in ['hi', 'hey', 'sup', 'yo', 'hello', 'wsup', 'wassup']:
                return i
        return help


    if list(message)[0] == 'q':
        if list(message)[1] == ' ':
        
            question = message[1:]
            client = wolframalpha.Client(creds.app_id)
            res = client.query(question)
            answer = next(res.results).text
            return answer

    message_price = message.split()
    page = requests.get("https://www.marketwatch.com/investing/index/" + message_price[1].lower())
    soup = BeautifulSoup(page.text, "html.parser")

    price = soup.findAll("span", attrs={"class":"value"})
    price2 = soup.findAll("bg-quote", attrs={"class":"value"})
    company = soup.findAll("h1", attrs={"class":"company__name"})
    country = soup.find("span", attrs={"class":"company__market"})
    change = soup.find("bg-quote", attrs={"field":"change"})

    if message_price[0] == 'price':
        
        if country.text[0:6] == 'Canada':
            return f'The current stock price of {message_price[1].upper()} ({company[0].text}) is {price[0].text} CAD.'
        try:
            return f'The current stock price of {message_price[1].upper()} ({company[0].text}) is {price[0].text} USD.'
        except:
            return f'The current stock price of {message_price[1].upper()} ({company[0].text}) is {price2[0].text} USD.'


        

            
    

