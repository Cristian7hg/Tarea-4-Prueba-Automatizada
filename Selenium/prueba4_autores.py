from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    
    driver.get("http://localhost/LIBRERIA/")  

    
    menu_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.menu-toggle.rounded")))
    menu_button.click()

    
    autores_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Autores")))
    autores_link.click()

    
    time.sleep(2)  

   
    autores_seccion = driver.find_element(By.ID, "autores")
    if autores_seccion.is_displayed():
        print("Prueba exitosa: Sección 'Autores' visible correctamente.")
        
        
        autores = driver.find_elements(By.XPATH, "//p")  
        if autores:
            print("Prueba exitosa: Los autores se muestran correctamente.")
            for autor in autores:
                print(autor.text)  
        else:
            print("Prueba fallida: No se encontraron autores.")
    else:
        print("Prueba fallida: No se pudo acceder a la sección 'Autores'.")

except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
   
    time.sleep(2)
    driver.quit()
