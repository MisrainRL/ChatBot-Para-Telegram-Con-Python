# -*- coding: utf-8 -*-
import telebot
import time
from telebot import types
import os


Tipo_Usuario = "x"

Nombre_Usuario = "x"
Categoria="x"
Sub_categoria="x"
Producto="x"
Prospecto="x"

bot = telebot.TeleBot("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
     

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

	chatid = message.chat.id 
	try:
		nombreUsuario = message.chat.first_name
	
		saludo = "Hola {nombre}, bienvenido a mi bot de Información DXN.  \n\n {nombre} eres socio DXN o nuevo en la empresa?: \n/SocioDXN  \n/nuevo en la empresa"
		bot.send_message(chatid, saludo.format(nombre=nombreUsuario))
	except Exception as e:
		saludo =  "Hola, bienvenido a mi bot de Información DXN.  \n\n eres socio DXN o nuevo en la empresa?: \n/Socio DXN  \n/nuevo en la empresa"
		bot.send_message(chatid, saludo)

###########################################Inicia definir unisario####################################################
@bot.message_handler(commands=["SocioDXN"])
def SocioDXN(message):
	global Nombre_Usuario
	global Tipo_Usuario

	nombreUsuario = message.chat.first_name
	Nombre_Usuario=nombreUsuario
	Tipo_Usuario="SocioDXN"

	try:
		chatid = message.chat.id 

		bot.send_message(chatid, "Este Bot te proporciona informacion de tres áreas principales. \n Seleccione el área que quiera conocer \n\n /AcercaDeNosotros \n /Productos \n /Contacto")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")	
#Evitar Comandos no definidad

@bot.message_handler(commands=["nuevo"])
def nuevo(message):
	global Nombre_Usuario
	global Tipo_Usuario

	nombreUsuario = message.chat.first_name
	Nombre_Usuario=nombreUsuario
	Tipo_Usuario="Prospecto a socio"
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Este Bot te proporciona informacion de tres áreas principales. \n Seleccione el área que quiera conocer \n\n /AcercaDeNosotros \n /Productos \n /Contacto")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")		
###########################################Finaliza definir unisario####################################################



###########################################Inicia bloque Acerca de nosotros####################################################
#Acerca de nosotros
@bot.message_handler(commands=["AcercaDeNosotros"])
def conoce(message):
	global Categoria
	Categoria = "Acerca de nosotros"
	
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Acerca de Nosotros. \n ¿Qué quieres saber? \n Seleccione el área que quiera conocer \n\n /QuienesSomos \n /Concepto \n /Filosofia\n\n /Inicio")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")		

	
	
#QuienesSomos
@bot.message_handler(commands=["QuienesSomos"])
def Somos(message):
	global Sub_categoria
	Sub_categoria="Quienes Somos"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nConsulta: Acerca de."+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/info.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Acerca de Nosotros. \n ¿Qué quieres saber? \n Seleccione el área que quiera conocer \n\n /QuienesSomos \n /Concepto \n /Filosofia \n\n /Inicio")
	
#Concepto
@bot.message_handler(commands=["Concepto"])
def concepto(message):
	global Sub_categoria
	Sub_categoria="Concepto"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nConsulta: Acerca de."+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/concepto.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Acerca de Nosotros. \n ¿Qué quieres saber? \n Seleccione el área que quiera conocer \n\n /QuienesSomos \n /Concepto \n /Filosofia \n\n /Inicio")

#Filosofia
@bot.message_handler(commands=["Filosofia"])
def filosofia(message):
	global Sub_categoria
	Sub_categoria="Filosofía"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nConsulta: Acerca de."+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Filosofia.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Acerca de Nosotros. \n ¿Qué quieres saber? \n Seleccione el área que quiera conocer \n\n /QuienesSomos \n /Concepto \n /Filosofia \n\n /Inicio")
		
###########################################Finaliza bloque Acerca de nosotros####################################################


###########################################Inicia bloque de productos############################################################
#Productos
@bot.message_handler(commands=["Productos"])
def productos(message):
	global Categoria
	Categoria = "Productos"
	
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Productos. \n ¿Qué quieres saber? \n Los productos se Clasifican en 3 bloques, elige uno \n\n /AlimentosyBebidas \n /SuplementosAlimenticios \n /CuidadoPersoal\n\n /Inicio")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")		

#######################################Inicia bloque de Alimentos y bebidas###############################
@bot.message_handler(commands=["AlimentosyBebidas"])
def productos(message):
	global Sub_categoria
	Sub_categoria = "Alimentos y Bebidad"
	
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")	


#Cafe_Negro
@bot.message_handler(commands=["Cafe_Negro"])
def CN(message):
	global Producto
	Producto="Cafe negro"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/CNegro.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#CordyCereal
@bot.message_handler(commands=["Cereal_de_cordyceps"])
def cordi(message):
	global Producto
	Producto="Cereal de Cordyceps"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/CCordy.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#SpirulinaCereal
@bot.message_handler(commands=["Cereal_de_spirulina"])
def cordi(message):
	global Producto
	Producto="Cereal de Spirulina"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/CSpirulina.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#Cocozhi
@bot.message_handler(commands=["Cocozhi"])
def coco(message):
	global Producto
	Producto="Cocozhi"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/cocozhi.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")
	
#civatino
@bot.message_handler(commands=["DXN_Civatino"])
def civatino(message):
	global Producto
	Producto="DXN Civatino"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/civatino.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")
			
#3-1 cordi
@bot.message_handler(commands=["DXN_Cordyceps_cofee_3_in_1"])
def cordi3(message):
	global Producto
	Producto="DXN Cordycepscofee 3in1"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/CordiCafe.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")
	
#Goji
@bot.message_handler(commands=["DXN_Goji_Berries"])
def Goji(message):
	global Producto
	Producto="DXN Goji Berries"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Goji.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#Jujube
@bot.message_handler(commands=["DXN_Jujube_fruits"])
def Jujube(message):
	global Producto
	Producto="DXN Jujube"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Jujube.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")


#Vita
@bot.message_handler(commands=["DXN_vita_cafe"])
def vita(message):
	global Producto
	Producto="DXN Vita café"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Vita.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#Zhi Mocha
@bot.message_handler(commands=["DXN_Zhi_Mocha"])
def Zhi(message):
	global Producto
	Producto="DXN Zhi Mocha"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Mocha.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#Crema
@bot.message_handler(commands=["Lingzhi_coffee_3en1"])
def crema(message):
	global Producto
	Producto="Café 3 en 1"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Crema.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Cafe_Negro \n /Cereal_de_cordyceps \n /Cereal_de_spirulina \n/Cocozhi \n /DXN_Civatino \n /DXN_Cordyceps_cofee_3_in_1 \n /DXN_Goji_Berries \n /DXN_Jujube_fruits \n /DXN_vita_cafe \n /DXN_Zhi_Mocha \n /Lingzhi_coffee_3en1\n\n /Inicio")

#######################################Finaliza bloque de Alimentos y bebidas###############################

#######################################Inicia bloque de Suplementos###############################
@bot.message_handler(commands=["SuplementosAlimenticios"])
def Suple(message):
	global Sub_categoria
	Sub_categoria = "Suplementos Alimenticios"
	
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")	

#Pollen
@bot.message_handler(commands=["DXN_Bee_Pollen"])
def Pollen(message):
	global Producto
	Producto="DXN Bee Pollen"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Pollen.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")

#Black
@bot.message_handler(commands=["DXN_Black_Cumin"])
def Black(message):
	global Producto
	Producto="DXN Black Cumin"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Black.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")

#CordyTabs
@bot.message_handler(commands=["DXN_Cordyceps"])
def Tabs(message):
	global Producto
	Producto="DXN Cordyceps Tabletas"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Tabs.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")

#Lion Mane
@bot.message_handler(commands=["DXN_Lion_Mane"])
def Lion(message):
	global Producto
	Producto="DXN Lion Mane"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Lion.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")


#Monascus
@bot.message_handler(commands=["DXN_Monascus"])
def Monascus(message):
	global Producto
	Producto="DXN Monascus"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Monascus.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")

#GL
@bot.message_handler(commands=["Ganocelium"])
def GL(message):
	global Producto
	Producto="GL"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/GL.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")
#RG
@bot.message_handler(commands=["Reishi_Gano"])
def RG(message):
	global Producto
	Producto="RG"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/RG.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")

#SPITUTABS
@bot.message_handler(commands=["Spirulina_Tabletas"])
def spitulin(message):
	global Producto
	Producto="Spirulina"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/SpirulinaTab.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /DXN_Bee_Pollen \n /DXN_Black_Cumin \n /DXN_Cordyceps \n/DXN_Lion_Mane \n /DXN_Monascus \n /Ganocelium \n /Reishi_Gano \n /Spirulina_Tabletas\n\n /Inicio")

#######################################Finaliza bloque de Suplementos###############################


#######################################Inicia bloque de Cuidado Personal###############################
@bot.message_handler(commands=["CuidadoPersoal"])
def Personal(message):
	global Sub_categoria
	Sub_categoria = "Cuidado Personal"
	
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Aceite_de_Masaje_Gano \n /Gel \n /Jabon_Ganozhi \n/Pasta_de_dientes \n /Shampoo_Ganozhi \n\n /Inicio")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")	

#Aceite
@bot.message_handler(commands=["Aceite_de_Masaje_Gano"])
def aceite(message):
	global Producto
	Producto="Aceite de masaje gano"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Aceite.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Aceite_de_Masaje_Gano \n /Gel \n /Jabon_Ganozhi \n/Pasta_de_dientes \n /Shampoo_Ganozhi \n\n /Inicio")

#Gel de baño
@bot.message_handler(commands=["Gel"])
def gel(message):
	global Producto
	Producto="Gel de baño"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Gel.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Aceite_de_Masaje_Gano \n /Gel \n /Jabon_Ganozhi \n/Pasta_de_dientes \n /Shampoo_Ganozhi \n\n /Inicio")

#Jabon
@bot.message_handler(commands=["Jabon_Ganozhi"])
def Jabon(message):
	global Producto
	Producto="Jabón Ganozhi"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Jabon.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Aceite_de_Masaje_Gano \n /Gel \n /Jabon_Ganozhi \n/Pasta_de_dientes \n /Shampoo_Ganozhi \n\n /Inicio")

#Pasta
@bot.message_handler(commands=["Pasta_de_dientes"])
def pasta(message):
	global Producto
	Producto="Pasta de dientes"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Pasta.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Aceite_de_Masaje_Gano \n /Gel \n /Jabon_Ganozhi \n/Pasta_de_dientes \n /Shampoo_Ganozhi \n\n /Inicio")

#Shampoo
@bot.message_handler(commands=["Shampoo_Ganozhi"])
def shampoo(message):
	global Producto
	Producto="Shampoo Ganozhi"
	try:
		fecha = time.strftime("%c")
		f = open ("../Consultas.txt", "a", encoding = 'utf-8')
		f.write("Fecha de consulta: "+fecha+"\nNombre de usuario: "+Nombre_Usuario+"\nTipo de Usuario: "+Tipo_Usuario+"\nCategoria: "+Categoria+"\nSub-Categoria: "+Sub_categoria+"\nProducto: "+Producto+"\n--------------------------------------------------------\n")
		f.close()
		chatid = message.chat.id 
		photo = open('../BD/Shampoo.png', 'rb')
		bot.send_photo(chatid, photo)
		bot.send_photo(chatid, "FILEID")
	except Exception as e:
		bot.send_message(chatid, "Productos. \n Que productos quieres conocer? \n\n /Aceite_de_Masaje_Gano \n /Gel \n /Jabon_Ganozhi \n/Pasta_de_dientes \n /Shampoo_Ganozhi \n\n /Inicio")

#######################################Finaliza bloque de Cuidado Personal###############################
###########################################Finaliza bloque de productos############################################################


#########Comando para mostrar el menu principal###########################
#inicio
@bot.message_handler(commands=["Inicio"])
def Inicio(message):
	try:
		chatid = message.chat.id 
		bot.send_message(chatid, "Este Bot te proporciona informacion de tres áreas principales. \n Seleccione el área que quiera conocer \n\n /AcercaDeNosotros \n /Productos \n /Contacto")
	except Exception as e:
		bot.reply_to(message, "Ha ocurrido un error. Por favor inténtelo de nuevo")	
#Evitar Comandos no definidad
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	chatid= message.chat.id
	bot.send_message(chatid,"No existe ese comando")
print("El bot se está ejecutando")
bot.polling()