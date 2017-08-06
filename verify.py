from email_validator import validate_email, EmailNotValidError
import csv

email = 'fabricio@ideape.com'

def verify_email(email):
	try:
	    v = validate_email(email) # validate and get info
	    email = v["email"] # replace with normalized form
	    return True
	except EmailNotValidError as e:
	    return False

counter = 0
good_emails = []
with open('to_verify.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		counter = counter + 1
		response = verify_email(row[0])
		print row[0] + ' - ' + str(response)
		print 'Emails analisados: ' + str(counter)
		if response == True:
			good_emails.append(row[0])

with open('verified.csv', 'wb') as csvfile:
	for email_address in good_emails:
		spamwriter = csv.writer(csvfile, delimiter=';')
		data = []
		data.append(email_address)
		spamwriter.writerows([data])

print 'Finito! <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
print len(good_emails)