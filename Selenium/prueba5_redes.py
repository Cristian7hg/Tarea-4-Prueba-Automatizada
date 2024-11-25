from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.service import Service# type: ignore
from selenium.webdriver.support.ui import WebDriverWait# type: ignore
from selenium.webdriver.support import expected_conditions as EC# type: ignore
from webdriver_manager.chrome import ChromeDriverManager# type: ignore
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    
    driver.get("http://localhost/LIBRERIA/")  

    
    menu_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.menu-toggle.rounded")))
    menu_button.click()

    
    redes_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Redes")))
    redes_link.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.social-link.rounded-circle.text-black"))).click()

   

   
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])  # Cambiar a la segunda pestaña
    if "github.com" in driver.current_url:
        print("Prueba exitosa: El perfil de GitHub se abrió correctamente.")
    else:
        print("Prueba fallida: No se abrió el perfil de GitHub.")

except Exception as e:
    print(f"Error durante la prueba: {e}")

finally:
   
    time.sleep(2)
    driver.quit()
