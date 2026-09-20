import requests

res=requests.get("https://lms.ithillel.ua/groups/6a3128ebee95904e1dc8d51f/lessons/6a3128ebee95904e1dc8d534")
print(res.status_code)
