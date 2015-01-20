import csv
import urllib2
import requests
import json

f = open('book.csv')
csv_f = csv.reader(f)

myfile = open('book_result.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

error_file = open('book_error.csv', 'wb')
wr_error = csv.writer(error_file, quoting=csv.QUOTE_ALL)

i = 1

for row in csv_f:
	request = "http://calculateurdomainepublic.fr/api/pd?jurisdiction=france/bnf&detail=medium&lang=fr&work="
	fromyear='Unknown'	
	try:
		response = urllib2.urlopen(row[0])
	except urllib2.HTTPError, err:
  			row.append(err.code)
			wr_error.writerow(row)
			print i 
			print "error: ", row[6]
			i += 1      			
   	else:
   		pass

	try:
	  	url = response.geturl()
	except urllib2.HTTPError, err:
			row.append(err.code)
			wr_error.writerow(row)
			print i 
			print "error: ", row[6]
			i += 1
	else:
		pass

	request += url
	request += "rdf.xml"
	
	try:
		api= requests.get(request)
	except requests.HTTPError, err:
			row.append(err.code)
			wr_error.writerow(row)
			print i 
			print "error: ", row[6]
			i += 1
	else:
		pass

	try:
		json_data = json.loads(api.text)
		fromyear = json_data['output'][0]['data']['fromyear']
	except Exception: 
	 	pass						  	
	
	row.append(fromyear)
	wr.writerow(row)
	print i 
	print row[6]
	i += 1






