from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    
    driver.get("http://localhost/LIBRERIA/")  

    
    menu_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.menu-toggle.rounded")))
    menu_button.click()

    
    libros_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Libros")))
    libros_link.click()

    
    time.sleep(2)  

   
    libros_seccion = driver.find_element(By.ID, "libros")
    if libros_seccion.is_displayed():
        print("Prueba exitosa: Sección 'Libros' visible correctamente.")
        
        
        libros = driver.find_elements(By.XPATH, "//p")  
        if libros:
            print("Prueba exitosa: Los libros se muestran correctamente.")
            for libro in libros:
                print(libro.text)  
        else:
            print("Prueba fallida: No se encontraron libros.")
    else:
        print("Prueba fallida: No se pudo acceder a la sección 'Libros'.")

except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
    
    time.sleep(2)
    driver.quit()
