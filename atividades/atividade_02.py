import wget

print('Digite a URL da imagem que deseja baixar: ', end='')

url = input()

wget.download(url)
