
from requests_html import HTMLSession

s = HTMLSession()

querry = 'litomysl'

url = f'https://www.google.com/search?q=pocasi+{querry}'

r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
how = r.html.find('div.VQF4g span#wob_dc',first=True).text

print(f'V {querry} je {temp}{unit} a {how}')
