import requests
import json
import base64


image_path = "変身.jpg"

image =  open(image_path, "rb").read()
response_type = "json"
request_body = {"response_type": response_type}
url = "https://ai-api.userlocal.jp/human_pose"
res = requests.post(url, data=request_body, files={"image_data": image})
data = json.loads(res.content)
image = base64.b64decode(data["image_data"])
with open("test.jpg", "wb") as f:
    f.write(image)
print(data["result"])