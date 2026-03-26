import pprint
import requests
url="https://reqres.in/api/test-suite/collections/users/records"
response=requests.get(url)
logs=response.text.lower()
pprint.pprint(logs)
if "window" in logs:
    print("TDR found")
if "emoji" in logs:
    print("Crash found")
if "tdr" or "crash" in logs:
    print("test failed")
else:
    print("all test passed")