#!/usr/bin/env python3
import os, json

print("Content-Type: application/json")    # HTML is following
print()                            # blank line, end of headers
print(json.dumps(dict(os.environ), indent=2))


# q2

# query string --


# Question 3: What environment variable contains information about the user’s browser?

# should be the user agent -- answer for question 3 



# Question 4: How does the POSTed data come to the CGI script?

# enter data fieldstorage and use get method

# Question 5: What is the HTTP header syntax to set a cookie from the server?
# use set cookie 

# Question 6: What is the HTTP header syntax the browser uses to send the cookie back?
# http_cookie and the information inside it 

# Question 7: In your own words, what are cookies used for?
# used to store user data 