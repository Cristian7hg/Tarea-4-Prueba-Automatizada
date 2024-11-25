from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    
    driver.get("http://localhost/LIBRERIA/formulario.php")

    
    driver.find_element(By.NAME, "nombre").send_keys("Cristian Heredia")
    driver.find_element(By.NAME, "correo").send_keys("cristian@itla.edu.do")
    driver.find_element(By.NAME, "asunto").send_keys("Consulta sobre libros")
    driver.find_element(By.NAME, "mensaje").send_keys("Me gustaría saber más sobre los libros disponibles.")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    time.sleep(2)
    confirmacion = driver.find_element(By.TAG_NAME, "body").text
    if "¡Comentario enviado correctamente!" in confirmacion:
        print("Prueba exitosa: El formulario se envió correctamente.")
    else:
        print("Prueba fallida: El mensaje de confirmación no se mostró.")

except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
    time.sleep(2)
    driver.quit()
