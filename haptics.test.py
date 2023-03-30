import requests

state = input('Enter state: ')

if state == 'r-active':
   requests.get('http://192.168.4.1/right/active')
elif state == 'r-inactive':
   requests.get('http://192.168.4.1/right/active')
   
if state == 'l-active':
   requests.get('http://192.168.4.4/left/active')
elif state == 'l-inactive':
   requests.get('http://192.168.4.4/left/inactive')
