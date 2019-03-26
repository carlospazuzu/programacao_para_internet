import requests, time

print("Digite a URL: ", end='')

url = input()

response = requests.get(url)

print("URL: {}".format(url))
print("STATUS CODE: {}".format(response.status_code))
print("TAMANHO: {}".format(len(response.text)))
time.sleep(1)
print("HEADERS: {}".format(response.headers))

answer = ""

while True: 
    print("Mostrar o corpo HTML?  (S/N)")
    answer = input()
    if answer == "S" or answer == "N":
        break

if answer == "S":
    print(response.text)
