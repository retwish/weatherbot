import requests, bs4
from datetime import datetime
from dateutil.relativedelta import relativedelta

now  = (datetime.now() + relativedelta(days=1))

r    = datetime.strftime(datetime.now(), "%Y-%m-%d")  # получаем текущую дату в виде спсиска
r1   = datetime.strftime(now, "%Y-%m-%d")  

url  = ('https://sinoptik.com.ru/погода-синельниково-303024317#'+ r)   # получаем урл. с датой
url1 = ('https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B8%D0%BD%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%BE-303024317/' + r1)


def parse(url):
	s       = requests.get(url)
	b       = bs4.BeautifulSoup(s.text, "html.parser")

	pnow    = b.select('.imgBlock .today-temp')
	weatnow = pnow[0].getText()
	
	details = b.find('table', class_="weatherDetails")
	icos 	= details.find('tr', class_="img weatherIcoS")
	

	morn1   = b.select('.temperature .p3')
	mornmin = morn1[0].getText()
	morn2   = b.select('.temperature .p4')
	mornmax = morn2[0].getText()

	p3      = icos.find('td', class_="p3")
	p3info  = p3.find('div', title=True)

	day1    = b.select('.temperature .p5')
	daymin  = day1[0].getText()
	day2    = b.select('.temperature .p6')
	daymax  = day2[0].getText()

	p5      = icos.find('td', class_="p5")
	p5info  = p5.find('div', title=True)

	even1   = b.select('.temperature .p7')
	evenmin = even1[0].getText()
	even2   = b.select('.temperature .p8')
	evenmax = even2[0].getText()

	p7      = icos.find('td', class_="p7")
	p7info  = p7.find('div', title=True)
	p8      = icos.find('td', class_="p8")
	p8info  = p8.find('div', title=True)

	try:
		warning = b.find('div', class_="oWarnings clearfix")
		warinfo = warning.select('.rSide .description')
		warn  = warinfo[0].getText()
	except AttributeError:
		warn = "погодных проишествий сегодня не наблюдается"

	descrip = b.find('div', class_="wDescription clearfix")
	desinfo = descrip.select('.rSide .description')
	pogoda  = desinfo[0].getText()
	desc    = pogoda.strip()

	global pogoda1
	pogoda1 = ('✨Сейчас на улице ' + weatnow + '\n'
		'⛅Утром на улице ' + p3info['title'].lower() + '\n'
		'🌡Температура воздуха: от ' + mornmin + ' до ' + mornmax + 'C' '\n'
		'\n'
		'☀Днём на улице ' + p5info['title'].lower() + '\n'
		'🌡Температура воздуха: от ' + daymin + ' до ' + daymax + 'С' '\n'
		'\n'
		'🌒Вечером на улице ' + p7info['title'].lower() + '\n'
		'🌡Температура воздуха: ' + evenmin + 'С' '\n'
		'\n'
		'🌑Ночью на улице ' + p8info['title'].lower() + '\n'
		'🌡Температура воздуха: ' + evenmax + 'С' '\n'
		'\n'
		'&#9888;Внимание '+ warn + '\n'
		'\n'
		'&#128227;'+ desc + '\n'
		'\n'
		'Желаем вам удачного дня и хорошего настроения✨'
		)
	

	


def next_day(url1):
	s       = requests.get(url1)
	b       = bs4.BeautifulSoup(s.text, "html.parser")

	leftcol = b.find('div', id='leftCol')
	maincon = leftcol.find('div', id="mainContentBlock")
	bd2     = maincon.find('div', id="blockDays")
	tabs    = bd2.find('div', class_="tabsContent")

	details = b.find('table', class_="weatherDetails")
	icos 	= details.find('tr', class_="img weatherIcoS")
	
	morn1   = bd2.select('.temperature .p3')
	mornmin = morn1[0].getText()
	morn2   = bd2.select('.temperature .p4')
	mornmax = morn2[0].getText()

	p3      = icos.find('td', class_="p3")
	p3info  = p3.find('div', title=True)

	day1    = bd2.select('.temperature .p5')
	daymin  = day1[0].getText()
	day2 	= bd2.select('.temperature .p6')
	daymax 	= day2[0].getText()

	p5      = icos.find('td', class_="p5")
	p5info  = p5.find('div', title=True)

	even1 	= bd2.select('.temperature .p7')
	evenmin = even1[0].getText()
	even2 	= bd2.select('.temperature .p8')
	evenmax = even2[0].getText()

	p7      = icos.find('td', class_="p7")
	p7info  = p7.find('div', title=True)
	p8      = icos.find('td', class_="p8")
	p8info  = p8.find('div', title=True)

	try:
		warning = b.find('div', class_="oWarnings clearfix")
		warinfo = warning.select('.rSide .description')
		warn  = warinfo[0].getText()
	except AttributeError:
		warn = "погодных проишествий сегодня не наблюдается"
	

	descrip = b.find('div', class_="wDescription clearfix")
	desinfo = descrip.select('.rSide .description')
	pogoda  = desinfo[0].getText()
	desc    = pogoda.strip()
	global pogoda2
	pogoda2 = ('✨Прогноз погоды на завтра:' '\n'
		'⛅Утром на улице ' + p3info['title'].lower() + '\n'
		'🌡Температура воздуха: от ' + mornmin + ' до ' + mornmax + 'C' '\n'
		'\n'
		'☀Днём на улице ' + p5info['title'].lower() + '\n'
		'🌡Температура воздуха: от ' + daymin + ' до ' + daymax + 'С' '\n'
		'\n'
		'🌒Вечером на улице ' + p7info['title'].lower() + '\n'
		'🌡Температура воздуха: ' + evenmin + 'С' '\n'
		'\n'
		'🌑Ночью на улице ' + p8info['title'].lower() + '\n'
		'🌡Температура воздуха: ' + evenmax + 'С' '\n'
		'\n'
		'&#9888;Внимание '+ warn + '\n'
		'\n'
		'&#128227;'+ desc + '\n'
		'\n'
		'Желаем вам удачного дня и хорошего настроения✨'
		)
	
def main():
	parse(url)
	next_day(url1)
if __name__ == '__main__': #main() в вызывается если его запускают их консоли, а не импортируют 
	main()
