'''
Prints out the current version of the requests library installed in the system.
'''
import requests

print(requests.__version__)



'''
GET the google homepage

credits: aaronasterling
profile: https://stackoverflow.com/users/376728/aaronasterling
source: https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python
'''

print(requests.get('https://www.google.com'))


'''
Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub.

'''

print(requests.get("https://raw.githubusercontent.com/jteengfo/CMPUT404-lab/main/requests_ver.py").text)





