import requests

# dodac od malana import json zeby nam ladnie wysweitlało
# zbudowac podtswowy program zeby miecn apodkladke 
respons = requests.get("https://api.artic.edu/api/v1")
content = respons.json()

print(content)


