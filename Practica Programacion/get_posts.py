import requests
import json

def obtener_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        return response.json()[:10]  # Obtener solo los primeros 10 posts
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Tiempo de espera excedido: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    return None

def guardar_posts_en_json(posts):
    if posts:
        try:
            with open("posts.json", "w") as file:
                json.dump(posts, file, indent=4)
            print("Posts guardados exitosamente en posts.json.")
        except IOError as io_err:
            print(f"Error al guardar el archivo: {io_err}")
    else:
        print("No hay posts para guardar.")

if __name__ == "__main__":
    posts = obtener_posts()
    guardar_posts_en_json(posts)
