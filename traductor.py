import requests
import os

BLACK = '\033[30m'
RED = '\033[1;31m'
GREEN = '\033[32m'
YELLOW = '\033[1;33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def Traduccion(source, target, text):
	parametros = {'sl': source, 'tl': target, 'q': text}
	cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
	response = requests.post(url, data=parametros, headers=cabeceras)
	if response.status_code == 200:
		for x in response.json()['sentences']:
			return x['trans']
	else:
		return "Error"


os.system("clear")
print(CYAN+"""
_________ _______  _______  _____             _______ _________ _______ ________ 
\__   __/(  ____ )(  ___  )(  __  \ |\     /|(  ____ \\__   __/(  ___  )(  ____ )
   ) (   | (    )|| (   ) || (  \  )| )   ( || (    \/   ) (   | (   ) || (    )|
   | |   | (____)|| (___) || |   ) || |   | || |         | |   | |   | || (____)|
   | |   |     __)|  ___  || |   | || |   | || |         | |   | |   | ||     __)
   | |   | (\ (   | (   ) || |   ) || |   | || |         | |   | |   | || (\ (   
   | |   | ) \ \__| )   ( || (__/  )| (___) || (____/\   | |   | (___) || ) \ \__
   )_(   |/   \__/|/     \|(______/ (_______)(_______/   )_(   (_______)|/   \__/""")

while True:
	print()
	texto = input(GREEN+"Texto a traducir: ")
	if "salir" in texto:
		break
	else:
		respuesta = Traduccion("es", "en", texto)
		print()
		print(CYAN+"Resultado: " + str(respuesta))
		print()
