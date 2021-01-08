import requests as rq
from bs4 import BeautifulSoup as bs
import datetime
import table

a = datetime.date.today()
b = str(a.day)+'.'+str(a.month)+'.'+str(a.year)
if len(b)==9:
    c = '0' +str(a.day)+'.'+str(a.month)+'.'+str(a.year)
else:
    c = b


r = rq.get('https://bank.gov.ua/WebSelling/Home/News').text
soup = bs(r, 'lxml')


def find_table():
    find_news = soup.find('div', id='collapse1')
    find_t = find_news.find('tbody')
    if find_t == None:
        return None
    else:
        table.table()


def find_all():
    find_news = soup.find('div', id='collapse1').text
    f = str(find_news.strip())
    find_date = soup.find('span', class_='pull-right').text
    date = str(find_date)
    date1= date[17::]
    if date1 == c:
        find_table()
        return 'Вот что мне удалось найти!\n\n'+ f
    else:
        return f'За сегодня новостей нет.\nПоследняя новость была опубликована {find_date[17::]}'

def find_last():
    find_news = soup.find('div', id='collapse1').text
    f = str(find_news.strip())
    find_date = soup.find('span', class_='pull-right').text
    find_table()
    return f'Вот последняя новость, которая была аж {find_date[17::]}\n\n'+ f




