from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = './chromedriver'
_URL = 'https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-referrers')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )

driver.get(_URL)

def consultar(nit):
    rs = []
    for i in nit:
        if not i:
            continue
        try:
            nit_input = driver.find_element_by_xpath(
            "//input[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit']")
            nit_input.clear()
            nit_input.send_keys(i)
            nit_input.send_keys(Keys.ENTER)
            dv = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:dv']")
            print(i)

            try:
                razon_social = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial']")
                fecha_actual = driver.find_element_by_xpath("//tr//tr//tr[3]//td[1]//table[1]//tbody[1]//tr[1]")
                estado = driver.find_element_by_xpath(
                    "//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:estado']")
                data = {
                    "nit": i,
                    "razon_social": razon_social.text,
                    "regimen": "COMUN",
                    "fecha_actual": fecha_actual.text,
                    "estado": estado.text,
                }
                rs.append(data)
            except:
                primer_apellido = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerApellido']")
                segundo_apllido = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:segundoApellido']")
                primer_nombre = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerNombre']")
                otros_nombres = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:otrosNombres']")
                fecha_actual = driver.find_element_by_xpath("//tr//tr//tr[3]//td[1]//table[1]//tbody[1]//tr[1]")
                estado = driver.find_element_by_xpath("//span[@id='vistaConsultaEstadoRUT:formConsultaEstadoRUT:estado']")

                data = {
                    "nit": i,
                    "primer_apellido": primer_apellido.text,
                    "segundo_apellido": segundo_apllido.text,
                    "primer_nombre": primer_nombre.text,
                    "otros_nombres": otros_nombres.text,
                    "regimen": "simplificado",
                    "fecha_actual": fecha_actual.text,
                    "estado": estado.text,
                }
                rs.append(data)
        except:
            pass
        
    return rs