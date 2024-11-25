from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:

    driver.get("http://localhost/LIBRERIA/")  


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary.btn-xl"))).click()

   
    time.sleep(2)  
    tiendas = driver.find_elements(By.XPATH, "//p[contains(text(),'Ubicación')]")
    
    if tiendas:
        print("Prueba exitosa: Las tiendas se muestran correctamente.")
        for tienda in tiendas:
            print(tienda.text)
    else:
        print("Prueba fallida: No se encontraron tiendas o no se cargaron correctamente.")

except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
    
    time.sleep(2)
    driver.quit()
