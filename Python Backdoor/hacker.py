import requests

url = 'http://localhost:1000'  # Replace <server-ip> with the IP address of the server

while True:
    data = {'input': input()}  # Prompt the user for input and store it in the 'input' key

    response = requests.post(url, data=data)

    print(response.text)  # Print the response received from the server
