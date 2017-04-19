import json


with open('books.json') as data_file:
	data = json.load(data_file)

print(data[0]['Book'])
