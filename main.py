import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=53be2661e42e33ce19f4a8aa4ff94ce2ce3ca725"


headers = {
    'content-type': "multipart/form-data",
    'Content-Type': "multipart/form-data"
    }

files = {
    'answer':open('answer.json','rb')
}

response = requests.request("POST", url, files=files, headers=headers)

print(response.text)