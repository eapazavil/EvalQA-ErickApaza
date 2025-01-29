from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook
from urllib.parse import urlparse

# Función busqueda
def search_product(driver, url, search_term):
    driver.get(url)
    
    if "mercadolibre" in url:
        search_box = driver.find_element(By.NAME, "as_word")
    elif "amazon" in url:
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    elif "ripley" in url:
        search_box = driver.find_element(By.ID, "buscador-search-input")
    elif "falabella" in url:
        search_box = driver.find_element(By.NAME, "as_word")
    else:
        raise Exception("Sitio web no soportado")

    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)

# Función principal
def main():
    # Configuración de Selenium para Firefox
    driver = webdriver.Firefox() 

    # Diccionario de sitios web y términos de búsqueda
    websites = {
        "amazon": ("https://www.amazon.com/", "motos"),
        "mercadolibre": ("https://www.mercadolibre.com.pe/", "motos"),
        "ripley": ("https://simple.ripley.com.pe/", "polos"),
        "saga_falabella": ("https://www.falabella.com.pe/", "libros"),
    }

    # Selección del sitio web
    print("Selecciona el sitio web:")
    for index, site in enumerate(websites.keys()):
        print(f"{index + 1}. {site.capitalize()}")
    choice = int(input("Ingrese el número correspondiente a su elección: ")) - 1
    selected_site = list(websites.keys())[choice]
    url, search_term = websites[selected_site]

    # búsqueda
    search_product(driver, url, search_term)

    # Lista para almacenar los datos
    data = []

    for i in range(1, 6):
        xpath = f"/html/body/main/div/div[3]/section/ol/li[{i}]/div/div/div[2]/h3/a"
        try:
            result_link_element = driver.find_element(By.XPATH, xpath)
            result_link = result_link_element.get_attribute("href")
            
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(result_link)
            time.sleep(3)  
            final_url = driver.current_url

            product_title = driver.find_element(By.CSS_SELECTOR, ".ui-pdp-title").text

            domain = urlparse(final_url).netloc
            org_name = domain.split('.')[1]  

            data.append((org_name, product_title, final_url))
    
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"No se encontró el elemento {i} en el sitio {selected_site}: {e}")

    # Crear un nuevo archivo Excel
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Links y Nombres de Productos"

    # Escribir los títulos de las columnas
    sheet['A1'] = "WEB"
    sheet['B1'] = "NOMBRE PRODUCTO"
    sheet['C1'] = "LINK DEL PRODUCTO"

    for index, (org_name, title, link) in enumerate(data, start=2):  
        sheet[f'A{index}'] = org_name
        sheet[f'B{index}'] = title
        sheet[f'C{index}'] = link

    workbook.save("productos_links.xlsx")

    for org_name, title, link in data:
        print(f"ORGANIZACIÓN: {org_name}, NOMBRE PRODUCTO: {title}, LINK DEL PRODUCTO: {link}")

    driver.quit()

if __name__ == "__main__":
    main()
