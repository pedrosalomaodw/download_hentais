from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests, os, shutil, colorama

colorama.init()


os.system("cls")
url_site = input("url da pagina: ")
browser = webdriver.Firefox()
browser.get(url_site)

##############################################################################################
# pegando div, contando quantos elementos de img tem dentro da div posts
div_single_posts = browser.find_element(By.CLASS_NAME,'single-post')
capturando_img = len(div_single_posts.find_elements(By.TAG_NAME,'img')) # conta quantas tags de img tem
img = browser.find_element(By.CLASS_NAME, "alignnone").get_attribute("class") # captura a tag das imagens, ainda dá para melhorar
dados = img.split()
numero = [] # adicionando numeros
number = dados[2].split("wp-image-") #removendo a parte escrita da class
numero.append(int(number[1]))
##############################################################################################
# ainda dá para melhorar o código e adicionando funções
try:
    for y in range(0,1):
            imgem  = browser.find_element(By.CLASS_NAME, f"wp-image-{numero[0]}").get_attribute("src")
            print(colorama.Fore.RED,imgem)
            imagens_baixando = requests.get(imgem, stream=True)
            with open(f"./imagens/{numero[0]}.jpg","wb") as imagens:
                shutil.copyfileobj(imagens_baixando.raw, imagens)
    ##############################################################################################
            numeroo = numero[0] - capturando_img + 1 # para tag com numeros invertidos
    ##############################################################################################
    for x in range(numeroo, numeroo+capturando_img):
            print(x)
            imgem  = browser.find_element(By.CLASS_NAME, f"wp-image-{x}").get_attribute("src")
            imagens_baixando = requests.get(imgem, stream=True)
            with open(f"./imagens/{x}.jpg","wb") as imagens:
                shutil.copyfileobj(imagens_baixando.raw, imagens)
except Exception as error:
        print("error no: ", error)
        for p in range(numero[0], numero[0]+capturando_img):
            imgem  = browser.find_element(By.CLASS_NAME, f"wp-image-{p}").get_attribute("src")
            print(imgem)
            imagens_baixando = requests.get(imgem, stream=True)
            print(p)
            with open(f"./imagens/{p}.jpg","wb") as imagens:
                shutil.copyfileobj(imagens_baixando.raw, imagens)

        print(colorama.Fore.GREEN,"download concluído!")
browser.quit()
