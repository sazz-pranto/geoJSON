import urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js:
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(type(js))
    values = list()
    # this loop will pull out the list within the dictionary
    for key, value in js.items():
        if key == 'comments':
            values = value
            break

    print(values)  # this contains a list of dictionaries
    listOfCounts = list()  # this list will contain the values of 'count'

    # this will go through each of the dictionaries of the list and give us the values of 'count'
    for index in range(len(values)):
        for key in values[index]:
            if key == 'count':
                listOfCounts.append(int(values[index][key]))
                break

    print('Total Counts:', len(listOfCounts))
    print('Sum of counts:', sum(listOfCounts))
    break
