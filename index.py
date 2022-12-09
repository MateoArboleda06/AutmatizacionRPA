from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.keys import Keys #// ENTER


driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.viajesexito.com/")

""" x = driver.find_element(By.XPATH, '/html/body/div[36]/div/div/div[1]/button')
x.click() """

paqueteVueloHotel = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a')
paqueteVueloHotel.click()

textoDestino = "punta"
destino = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input')
destino.click()
destino.send_keys(textoDestino)

puntaCana = driver.find_element(By.XPATH, '/html/body/ul[21]/li[3]/a/table/tbody/tr/td[2]')
puntaCana.click()

inputSalida = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input')
inputSalida.click()

time.sleep(2)

fechaSalida = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a')
fechaSalida.click()

fechaLlegada = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a')
fechaLlegada.click()

inputHabitacion = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div')
inputHabitacion.click()

time.sleep(2)

adultos = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button')
adultos.click()

aplicarHabitacion = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
aplicarHabitacion.click()

buscar = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a')
buscar.click()

time.sleep(25)

precioUno = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Uno----------")
print(precioUno.text)

precioDos = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Dos----------")
print(precioDos.text)

precioTres = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Tres----------")
print(precioTres.text)

precioCuatro = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Cuatro----------")
print(precioCuatro.text)

precioCinco = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Cinco----------")
print(precioCinco.text)

precioSeis = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Seis----------")
print(precioSeis.text)

precioSiete = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Siete----------")
print(precioSiete.text)

precioOcho = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Ocho----------")
print(precioOcho.text)

precioNueve = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Nueve----------")
print(precioNueve.text)

precioDiez = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]')
print("")
print("---------Precio Diez----------")
print(precioDiez.text)

textoAerolinea = "avianca"
inputAerolinea = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
inputAerolinea.click()
inputAerolinea.send_keys(textoAerolinea)

aerolinea = driver.find_element(By.XPATH, '/html/body/ul[3]/li/a')
aerolinea.click()

buscarNuevo = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscarNuevo.click()

time.sleep(20)

titulo = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/a/span')

subtituloUno = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[1]/div[2]/a')
subtituloDos = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[1]/div[3]/a')
subtituloTres = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[1]/div[4]/a')

resultadoUno = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[2]/a/div/div[2]')
resultadoDos = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[3]/a/div/div[2]')
resultadoTres = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[4]/a/div/div[2]')

print("")
print("-----------NUEVA BUSQUEDA----------")
print(f"Aerolinea: {titulo.text}")
print(f"{subtituloUno.text}: {resultadoUno.text}")
print(f"{subtituloDos.text}: {resultadoDos.text}")
print(f"{subtituloTres.text}: {resultadoTres.text}")

time.sleep(5)

driver.quit()