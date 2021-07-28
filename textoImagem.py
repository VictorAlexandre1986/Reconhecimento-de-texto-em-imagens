import easyocr

#Definindo o idioma a ser usado
reader = easyocr.Reader(['en'])

#Carrega e faz a leitura da imagem
resultados = reader.readtext('imagem.png',paragraph=False)

for resultado in resultados:
    print(f'Texto: {resultado[1]}')