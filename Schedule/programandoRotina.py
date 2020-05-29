import schedule

def hello():
	print('hello...')

def hi():
	print('hi...')

schedule.every(10).seconds.do(hello)
schedule.every(5).seconds.do(hi)

while True:
	schedule.run_pending()