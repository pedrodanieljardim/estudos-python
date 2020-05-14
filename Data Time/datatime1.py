from datetime import datetime, timedelta

data = datetime(2020, 5, 14, 12, 00, 00)

print('Padrão NA: {}'.format(data))
print('Padrão BR: {}'.format(data.strftime('%d/%m/%Y %H:%M:%S')))

