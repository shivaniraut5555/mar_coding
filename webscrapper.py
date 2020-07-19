from bs4 import BeautifulSoup
url='https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-64GB/dp/B07HGH3G6H/ref=sr_1_1?dchild=1&keywords=samsung&qid=1585240791&sr=8-1'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content,"html.parser")
title=soup.find(id="productTitle").get_text()
print(title.strip())
availability=soup.find(id="availability").get_text()
span=availability[0:60]
span_1=span.strip()
if("Currently unavailable" not in span_1):
    message()
def message():
    from twilio.rest import Client 
 
    account_sid = 'AC6f8491e1cff8f78efebf8d54cdd891fa' 
    auth_token = '[AuthToken]' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='+12018311876',  
                              body='Your product is available now.Go and grab!!!'      
                              to='+916291267840' 
                          ) 
 
    print(message.sid)


