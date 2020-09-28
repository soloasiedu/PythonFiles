#! python3
APPID = 'cc42e57d84cce9cfc9718a7d08001229'
#APPID = '54bdb867b4615b2a26b479636caf6721'
import json, requests, sys, textMyself
import pprint
##if len(sys.argv) < 2:
##    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
##    sys.exit()
##location = ' '.join(sys.argv[1:])
url ='https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid=%s' % (APPID)
##https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&
##exclude=hourly,daily&appid=cc42e57d84cce9cfc9718a7d08001229
#https://api.openweathermap.org/data/2.5/forecast/daily?q=San Francisco, CA&cnt=3&APPID=54bdb867b4615b2a26b479636caf6721
response = requests.get(url)
response.raise_for_status()
#print(response.text)
weatherData = json.loads(response.text)
#pprint.pprint(weatherData)
#print(weatherData)
##w = weatherData['list']
##print('Current weather in %s:' % (location))
##print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
##print()
##print('Tomorrow:')
##print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
##print()
##print('Day after tomorrow:')
##print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

w = weatherData['current']['weather'][0]
print('Current weather for today...')
print(w)
#textMyself.textmyself(str(w))
