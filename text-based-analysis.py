def validar_arquivo(nome):  # validador se o arquivo existe
    try:
        a = open(nome, "r")
        a.close()
        return True
    except Exception as error:  # caso não exista o programa não fecha e informa ao usuario
        print("arquivo nao encontrado!", error.__class__)
        return False


def organizar_pesos(nome):  # organizar os grupos de palavras em boas neutras e ruins
    global lista_boas
    lista_boas = []
    global lista_neutras
    lista_neutras = []
    global lista_ruins
    lista_ruins = []
    file = open(nome, "r")
    for line in file.readlines():
        espaco = line.index(" ")
        if line[:espaco] == "Good":  # lista de palavras boas
            lista_boas = line[espaco:].split()
        if line[:espaco] == "Neutral":  # lista de palavar neutras
            lista_neutras = line[espaco:].split()
        if line[:espaco] == "Bad":  # lista de palavras ruins
            lista_ruins = line[espaco:].split()
    file.close()


index = 0
while True:
    frase = input(
        "digite o nome do arquivo com as frases a serem analizadas: ")  # ler o nome do arquivo que possui as frases que serao analisadas
    resp = validar_arquivo(frase)
    if resp:
        break
while True:
    nomespesos = input(
        "digite o nome do arquivo dos nomes e pesos: ")  # ler o nome do arquivo com as palavras e seus pesos
    resp = validar_arquivo(nomespesos)
    if resp:
        break
organizar_pesos(nomespesos)

file = open(frase, "r")  # separar as frases do txt
frases = []
texto = file.read().title()
textos = texto.split("\n")
for i in textos:  # tirar pontos e virgulas
    c = i.replace(",", " ").replace(".", " ").split()
    frases.append(c)
file.close()
reconhecidas = []  # lista para palavras encontradas no texto analisado
aprendidas = []  # lista para as palavras aprendidas
arquivo = open(frase, "r")
boa = neutra = ruim = 0
boas = []
neutras = []
ruins = []
reconhecidas_frases = []
for i in frases:
    for palavra in lista_boas:
        if palavra in i:
            boa += i.count(palavra)  # contar a ocorrencia das palavras boas no texto
            if palavra.title() not in reconhecidas:
                reconhecidas.append(palavra)  # contar as palavras boas reconhecidas
    for palavra in lista_neutras:
        if palavra.title() in i:
            neutra += i.count(palavra)  # contar as palavras neutras no texto
            if palavra.title() not in reconhecidas:
                reconhecidas.append(palavra)  # contar as palavras neutras reconhecidas

    for palavra in lista_ruins:
        if palavra.title() in i:
            ruim += i.count(palavra)  # contar a ocorrencia de palavras ruins no texto
            if palavra.title() not in reconhecidas:
                reconhecidas.append(palavra)  # contar as palavras ruins reconhecidas
    reconhecidas_frases.append(reconhecidas)  # separar as palavras reconhecidas de cada frase diferente
    reconhecidas = []  # zerar as reconhecidas para não misturar as frases
    boas.append(boa)  # lista com o numero de palavras boas de cada frase
    boa = 0
    neutras.append(neutra)  # lista com o numero de palavras neutras de cada frase
    neutra = 0
    ruins.append(ruim)  # lista com o numero de palavras ruins de cada frase
    ruim = 0
medias = []

aprendidas_frases = []
for i in frases:
    for palavra in i:  # saber quais palavras sao as palavras aprendidas no texto
        if palavra not in reconhecidas_frases[index]:
            if palavra not in aprendidas:
                aprendidas.append(palavra)
        try:
            numerador_texto = (boas[index] * 5) + (neutras[index] * 0) + (ruins[index] * -5)
            denominador_texto = (boas[index] + neutras[index] + ruins[index])
            media_texto = float(numerador_texto / denominador_texto)  # fazer a nota final de cade texto
        except ZeroDivisionError:
            media_texto = 0
    media_texto = f"{media_texto:.2f}"  # formatar para 2 casas decimais
    media_texto = float(media_texto)
    medias.append(media_texto)  # lista com as medias de cada frase
    aprendidas_frases.append(aprendidas)  # lista com as palavras aprendidas de cada frase
    aprendidas = []
    index += 1

index = 0

for i in range(len(frases)):  # len(frases) == numero de frases recebidas no txt
    if medias[i] > 0:  # atualizar o arquivo de palavras e pesos com as palavras aprendidas baseadas na media da frase
        for palavra in aprendidas_frases[i]:
            if palavra not in lista_boas:
                lista_boas.append(palavra)
        joinboas = " ".join(lista_boas).replace(",", " ")  # formatação para separar em espaços
        joinneutras = " ".join(lista_neutras)
        joinruins = " ".join(lista_ruins)
        file = open(nomespesos, "w")  # reescrever o arquivo das palavras com pesos só que agora com as aprendidas
        file.write(f"Good {joinboas}\n")
        file.write(f"Neutral {joinneutras}\n")
        file.write(f"Bad {joinruins}")
        file.close()
    elif medias[i] == 0:
        for palavra in aprendidas_frases[i]:
            if palavra not in lista_neutras:
                lista_neutras.append(palavra)
        joinboas = " ".join(lista_boas)
        joinneutras = " ".join(lista_neutras).replace(",", " ")
        joinruins = " ".join(lista_ruins)
        file = open(nomespesos, "w")  # reescrever o arquivo das palavras com pesos só que agora com as aprendidas
        file.write(f"Good {joinboas}\n")
        file.write(f"Neutral {joinneutras}\n")
        file.write(f"Bad {joinruins}")
        file.close()
    elif medias[i] < 0:
        for palavra in aprendidas_frases[i]:
            if palavra not in lista_ruins:
                lista_ruins.append(palavra)
        joinboas = " ".join(lista_boas)
        joinneutras = " ".join(lista_neutras)
        joinruins = " ".join(lista_ruins).replace(",", " ")
        file = open(nomespesos, "w")  # reescrever o arquivo das palavras com pesos só que agora com as aprendidas
        file.write(f"Good {joinboas}\n")
        file.write(f"Neutral {joinneutras}\n")
        file.write(f"Bad {joinruins}")
        file.close()
junto_frase = []  # formatação para o csv das frases
junto_aprendidas = []  # formatação para o csv das palavras aprendidas
junto_reconhecidas = []  # formatação para o csv das palavras reconhecidas
for i in frases:
    r = " ".join(i)
    junto_frase.append(r)

for i in aprendidas_frases:
    r = " ".join(i)
    junto_aprendidas.append(r)

for i in reconhecidas_frases:
    r = ' '.join(i)
    junto_reconhecidas.append(r)
a = open("resultado.csv", "w")
a.write("Frase lida, Palavras Reconhecidas, Peso da Frase, Palavras Aprendidas\n")  # cabeçalho do csv
for i in range(len(frases)):
    a.write(f"{junto_frase[i]}, {junto_reconhecidas[i]}, {medias[i]}, {junto_aprendidas[i]}\n")  # formatação de escrita das linhas do csv
a.close()
