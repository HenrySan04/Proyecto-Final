#importamos todas las clases
from perfil import Perfil
from multimedia import Multimedia
from interaccion import Interaccion
from moderacion import Moderacion
from estadisticas import Estadisticas
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Crea instancias de las clases Perfil, Multimedia, Interaccion, Moderacion y Estadisticas
    perfil = Perfil()
    multimedia = Multimedia()
    interaccion = Interaccion()
    moderacion = Moderacion()
    estadisticas = Estadisticas()

    # Inicia un bucle infinito para mostrar el menú principal
    while True:
        # Imprime el mensaje de bienvenida y las opciones del menú
        print("\n\t\t\t---||| Bienvenido a Metrogram |||---\t\n")
        print("Metrogram es una red social especial para estudiantes y profesores de la Universidad Metropolitana. Estas son las gestiones a las cuales puedes acceder dentro de esta red: \n")
        print("1. Gestión de perfil")
        print("2. Gestión de multimedia")
        print("3. Gestión de interacción")
        print("4. Gestión de moderación")
        print("5. Gestión de estadísticas")
        print("6. Salir")
        # Solicita al usuario que seleccione una opción del menú
        # Solicita al usuario que seleccione una opción del menú principal
        option = input("\nSeleccione una opción: ")

        # Si la opción seleccionada es "1", entra en la gestión de perfil
        if option == "1":
            # Inicia un bucle infinito para mostrar el submenú de gestión de perfil
            while True:
                # Imprime las opciones del submenú de gestión de perfil
                print("\n---||| Gestión de perfil |||---\n")
                print("1. Registrar usuario")
                print("2. Buscar perfiles")
                print("3. Cambiar información de la cuenta")
                print("4. Mostrar todos los perfiles")
                print("5. Regresar")
                # Solicita al usuario que seleccione una opción del submenú
                sub_option = input("\nSeleccione una opción: ")

                # Si la opción seleccionada es "1", inicia el proceso de registro de usuario
                if sub_option == "1":
                    # Solicita al usuario que ingrese su nombre, apellido, correo electrónico, nombre de usuario y tipo de usuario
                    name = input("Ingrese nombre: ")
                    lastName = input("Ingrese apellido: ")
                    email = input("Ingrese correo electrónico: ")
                    username = input("Ingrese nombre de usuario: ")
                    tipo = input("Ingrese tipo: ")
                    # Si el tipo de usuario es "Estudiante", solicita que se ingrese la carrera
                    # Si el tipo de usuario es "Profesor", solicita que se ingrese el departamento
                    if tipo == "Estudiante":
                        tipo = "student"
                        department = None
                        career = input("Ingrese carrera: ")
                    elif tipo == "Profesor":
                        tipo = "professor"
                        department = input("Ingrese departamento: ")
                        career = None
                    # Llama al método register_user para registrar al nuevo usuario
                    perfil.register_user(name, lastName, email, username, tipo, department, career, multimedia)
                    # Imprime un mensaje de confirmación de registro
                    print("\nUsuario registrado\n")
                    # Da la bienvenida al nuevo usuario
                    print("Bienvenido a Metrogram, " + name + " " + lastName + "!\n")

                # Si la opción seleccionada es "2", inicia el proceso de búsqueda de perfiles
                elif sub_option == "2":
                    # Solicita al usuario que ingrese el tipo de filtro y su valor
                    filter_type = input("Ingrese tipo de filtro: ")
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Llama al método view_profile para buscar perfiles que coincidan con el filtro y muestra los resultados
                    print(f"\n{perfil.view_profile(filter_type, filter_value)}")
                    print("\n")

                # Si la opción seleccionada es "3", inicia el proceso de cambio de información de la cuenta
                elif sub_option == "3":
                    # Solicita al usuario que ingrese el tipo de filtro y su valor para identificar su cuenta
                    filter_type = input("Ingrese tipo de filtro: ")
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Solicita al usuario que ingrese el nuevo tipo de información y su valor
                    new_info_type = input("Ingrese nuevo tipo de información: ")
                    new_info_value = input(f"Ingrese nuevo {new_info_type}: ")
                    # Llama al método change_account_info para cambiar la información de la cuenta
                    perfil.change_account_info(filter_type, filter_value, new_info_type, new_info_value)
                    # Imprime un mensaje de confirmación de cambio de información
                    print("\nInformación cambiada\n")

                # Si la opción seleccionada es "4", muestra todos los perfiles de usuario
                elif sub_option == "4":
                    print("\nPerfiles:\n")
                    # Llama al método view_users para obtener y mostrar todos los perfiles de usuario
                    print(f"\t{perfil.view_users()}")

                # Si la opción seleccionada es "5", sale del submenú de gestión de perfil y regresa al menú principal
                elif sub_option == "5":
                    break

        # Si la opción seleccionada es "2", entra en la gestión de multimedia
        elif option == "2":
            # Inicia un bucle infinito para mostrar el submenú de gestión de multimedia
            while True:
                # Imprime las opciones del submenú de gestión de 
                print("\n---||| Gestión de multimedia |||---\n")
                print("1. Registrar post")
                print("2. Ver posts de un usuario")
                print("3. Buscar post en especifico")
                print("4. Dar like")
                print("5. Comentar")
                print("6. Regresar")
                print("7. Ver todos los posts")
                print("\nAccede con estos filtros: \n\n\t- username \t- caption\n\t- id       \t- url \n\t- email \t- publisher o id")
                # Solicita al usuario que seleccione una opción del submenú
                sub_option = input("\nSeleccione una opción: ")

                # Si la opción seleccionada es "1", inicia el proceso de registro de post
                if sub_option == "1":
                    # Solicita al usuario que ingrese el tipo de filtro y su valor para el usuario que realiza el post
                    filter_type = input("Ingrese tipo de filtro para el usuario que realiza el post: ")
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Solicita al usuario que ingrese el tipo de post, el caption y los hashtags
                    tipo = input("Ingrese tipo de post: ")
                    caption = input("Ingrese caption: ")
                    tags = input("Ingrese hashtags: ").split()
                    # Llama al método publish_post para registrar el nuevo post
                    multimedia.publish_post(filter_type, filter_value, tipo, caption, tags)
                    # Imprime un mensaje de confirmación de publicación del post
                    print("\nPost publicado\n")

                # Si la opción seleccionada es "2", inicia el proceso de visualización de posts
                elif sub_option == "2":
                    # Solicita al usuario que ingrese el tipo de filtro
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Imprime los posts
                    print("\nPosts:\n")
                    # Llama al método view_post para obtener y mostrar los posts que coinciden con el filtro
                    print(f"\t{multimedia.view_post(filter_type, filter_value)}")

                # Si la opción seleccionada es "3", inicia el proceso de búsqueda de posts
                elif sub_option == "3":
                    # Solicita al usuario que ingrese el tipo de filtro para ver un post en especifico
                    filter_type = input("Ingrese tipo de filtro para ver un post en especifico: ")
                    # Solicita al usuario que ingrese el valor del filtro
                    filter_value = input("Ingrese valor del filtro: ")
                    # Imprime los posts
                    print("\nPosts:\n")
                    # Llama al método search_posts para buscar y mostrar los posts que coinciden con el filtro
                    print(f"\t{multimedia.search_posts(filter_type, filter_value)}")
                # Si la opción seleccionada es "4", inicia el proceso de dar like a un post
                elif sub_option == "4":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que da el like
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que da el like
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que recibe el like
                    filter_type2 = input("\nIngrese tipo de filtro del usuario que recibe el like: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que recibe el like
                    filter_value2 = input(f"Ingrese {filter_type2}: ")
                    # Imprime los posts del usuario que recibe el like
                    print(f"\nPosts de {filter_value2}:\n")
                    # Llama al método view_post_urls para obtener y mostrar las URLs de los posts del usuario que recibe el like
                    print(f"\t{multimedia.view_post_urls(filter_type2, filter_value2)}")
                    # Solicita al usuario que ingrese la URL del post al que quiere dar like
                    url = input("\nIngrese url: ")
                    # Llama al método like_post para dar like al post seleccionado
                    multimedia.like_post(filter_type, filter_value, filter_type2, filter_value2, url)
                    # Imprime un mensaje de confirmación de que se ha dado like al post
                    print(f"\n[{filter_value2}]: {filter_value} le ha dado like a tu post:\n{url} \n")
                # Si la opción seleccionada es "5", inicia el proceso de comentar un post
                elif sub_option == "5":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que comenta
                    filter_type = input("Ingrese tipo de filtro del usuario: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que comenta
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario autor del post que va a comentar
                    filter_type2 = input("\nIngrese tipo de filtro del usuario autor del post que va a comentar: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario autor del post que va a comentar
                    filter_value2 = input(f"Ingrese {filter_type2}: ")
                    # Imprime los posts del usuario autor del post
                    print(f"\nPosts de {filter_value2}:\n")
                    # Llama al método view_post_urls para obtener y mostrar las URLs de los posts del usuario autor del post
                    print(f"\t{multimedia.view_post_urls(filter_type2, filter_value2)}")
                    # Solicita al usuario que ingrese la URL del post que quiere comentar
                    url = input("\nIngrese url: ")
                    # Solicita al usuario que ingrese el comentario
                    comment = input("\nIngrese comentario: ")
                    # Llama al método comment_post para agregar el comentario al post seleccionado
                    multimedia.comment_post(filter_type, filter_value, filter_type2, filter_value2, url, comment)
                    # Imprime un mensaje de confirmación de que se ha comentado el post
                    print(f"\n[{filter_value2}]: {filter_value} ha comentado tu post:\n{url} \n'{comment}'\n")

                # Si la opción seleccionada es "6", se rompe el bucle y se regresa al menú principal
                elif sub_option == "6":
                    break

                # Si la opción seleccionada es "7", se inicia el proceso de visualización de todos los posts
                elif sub_option == "7":
                    # Imprime un mensaje de encabezado
                    print("\nPosts:\n")
                    # Llama al método view_all_posts para obtener y mostrar todos los posts
                    print(f"\t{multimedia.view_all_posts()}")
                    # Imprime un salto de línea para separar los posts
                    print("\n")

        # Si la opción seleccionada es "3", se inicia el proceso de gestión de interacción
        elif option == "3":
            # Inicia un bucle infinito para mantener al usuario en el menú de gestión de interacción hasta que decida salir
            while True:
                # Imprime el menú de gestión de interacción
                print("\n---||| Gestión de interacción |||---\n")
                print("\nAccede con estos filtros: \n\t- username\n\t- id\n\t- email")
                print("\n1. Seguir usuario")
                print("2. Dejar de seguir usuario")
                print("3. Ver seguidos")
                print("4. Ver posts de seguidos")
                print("5. Ver likes de un post")
                print("6. Ver comentarios de un post")
                print("7. Eliminar comentario de un post")
                print("8. Ver solicitudes de usuarios")
                print("9. Regresar")
                # Solicita al usuario que seleccione una opción del menú
                sub_option = input("\nSeleccione una opción: ")

                # Si la opción seleccionada es "1", inicia el proceso de seguir a un usuario
                if sub_option == "1":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que sigue
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que sigue
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que va a seguir
                    filter_type2 = input("\nIngrese tipo de filtro del usuario que va a seguir: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que va a seguir
                    filter_value2 = input(f"Ingrese {filter_type2}: ")
                    # Llama al método follow_user para seguir al usuario seleccionado
                    interaccion.follow_user(filter_type, filter_value, filter_type2, filter_value2)

                # Si la opción seleccionada es "2", inicia el proceso de dejar de seguir a un usuario
                elif sub_option == "2":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que deja de seguir
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que deja de seguir
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que va a ser dejado de seguir
                    filter_type2 = input("\nIngrese tipo de filtro del usuario que va a dejar de seguir: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que va a ser dejado de seguir
                    filter_value2 = input(f"Ingrese {filter_type2}: ")
                    # Llama al método unfollow_user para dejar de seguir al usuario seleccionado
                    interaccion.unfollow_user(filter_type, filter_value, filter_type2, filter_value2)
                    # Imprime un mensaje de confirmación de que ya no se sigue al usuario
                    print("\nYa no sigues a este usuario\n")

                # Si la opción seleccionada es "3", inicia el proceso de ver a quién sigue el usuario
                elif sub_option == "3":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario cuyos seguidos se van a visualizar
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario cuyos seguidos se van a visualizar
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Imprime un mensaje de encabezado
                    print("\nSeguidos:\n")
                    # Llama al método view_following para obtener y mostrar la lista de seguidos del usuario
                    print(f"\t{perfil.view_following(filter_type, filter_value)}")

                # Si la opción seleccionada es "4", inicia el proceso de ver los posts de los usuarios seguidos
                elif sub_option == "4":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario cuyos seguidos se van a visualizar
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario cuyos seguidos se van a visualizar
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Imprime un mensaje de encabezado
                    print("\nPosts:\n")
                    # Llama al método view_following_posts para obtener y mostrar los posts de los usuarios seguidos
                    print(f"\t{interaccion.view_following_posts(filter_type, filter_value)}")

                # Si la opción seleccionada es "5", inicia el proceso de ver los likes de un post
                elif sub_option == "5":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario autor del post
                    filter_type = input("Ingrese tipo de filtro para el usuario autor del post: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario autor del post
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Llama al método view_user_posts para obtener y mostrar los posts del usuario
                    interaccion.view_user_posts(filter_type, filter_value)
                    # Solicita al usuario que ingrese la URL del post cuyos likes se van a visualizar
                    url = input("\nEnter the URL of the post: ")
                    # Imprime un mensaje de encabezado
                    print("\nLikes:\n")
                    # Llama al método view_post_likes_url para obtener y mostrar los likes del post
                    interaccion.view_post_likes_url(url)
                # Si la opción seleccionada es "6", inicia el proceso de ver los comentarios de un post
                elif sub_option == "6":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario autor del post
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario autor del post
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Llama al método view_user_posts para obtener y mostrar los posts del usuario
                    interaccion.view_user_posts(filter_type, filter_value)
                    # Solicita al usuario que ingrese la URL del post cuyos comentarios se van a visualizar
                    url = input("\nEnter the URL of the post: ")
                    # Imprime un mensaje de encabezado
                    print("\nComentarios:\n")
                    # Llama al método view_post_comments_url para obtener y mostrar los comentarios del post
                    interaccion.view_post_comments_url(url)

                # Si la opción seleccionada es "7", inicia el proceso de eliminar un comentario de un post
                elif sub_option == "7":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario autor del post
                    filter_type = input("Ingrese tipo de filtro para el post del usuario: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario autor del post
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Llama al método view_user_posts para obtener y mostrar los posts del usuario
                    interaccion.view_user_posts(filter_type, filter_value)
                    # Solicita al usuario que ingrese la URL del post del cual se va a eliminar un comentario
                    url = input("\nEnter the URL of the post: ")
                    # Llama al método view_post_comments_url para obtener y mostrar los comentarios del post
                    interaccion.view_post_comments_url(url)
                    # Solicita al usuario que ingrese el texto del comentario que desea eliminar
                    comment_to_delete = input("\nEscribe el texto del comment que quieras eliminar: ")
                    # Llama al método delete_post_comment para eliminar el comentario seleccionado del post
                    interaccion.delete_post_comment(filter_type, filter_value, url, comment_to_delete)
                # Si la opción seleccionada es "8", inicia el proceso de ver las solicitudes de seguimiento
                elif sub_option == "8":
                    # Solicita al usuario que ingrese el tipo de filtro para el usuario que va a gestionar las solicitudes
                    filter_type = input("Ingrese tipo de filtro: ")
                    # Solicita al usuario que ingrese el valor del filtro para el usuario que va a gestionar las solicitudes
                    filter_value = input(f"Ingrese {filter_type}: ")
                    # Imprime un mensaje de encabezado
                    print("\nSolicitudes:\n")
                    # Llama al método show_follow_requests para obtener y mostrar las solicitudes de seguimiento
                    print(f"\t{interaccion.show_follow_requests(filter_type, filter_value)}")
                    # Pregunta al usuario si desea aceptar o rechazar alguna solicitud
                    answer = input("\nDesea aceptar o rechazar alguna solicitud? (Si/No): ")
                    # Si el usuario desea gestionar las solicitudes
                    if answer == "Si":
                        # Solicita al usuario que ingrese el id del perfil de la solicitud que desea aceptar o rechazar
                        opciones = input("\nIngrese el id del perfil de la solicitud que desea aceptar o rechazar: ")
                        # Si el id del perfil ingresado corresponde a una solicitud existente
                        if opciones in interaccion.show_follow_requests(filter_type, filter_value):
                            # Imprime las opciones para aceptar o rechazar la solicitud
                            print("\n1. Aceptar solicitud")
                            print("2. Rechazar solicitud")
                            # Solicita al usuario que seleccione una opción
                            sub_option = input("\nSeleccione una opción: ")
                            # Si la opción seleccionada es "1", acepta la solicitud
                            if sub_option == "1":
                                interaccion.accept_follow_request(filter_type, filter_value, opciones)
                                print("\nSolicitud aceptada\n")
                            # Si la opción seleccionada es "2", rechaza la solicitud
                            elif sub_option == "2":
                                interaccion.decline_follow_request(filter_type, filter_value, opciones)
                                print("\nSolicitud rechazada\n")
                # Si la opción seleccionada es "9", se rompe el ciclo del menú
                elif sub_option == "9":
                    break

        # Si la opción seleccionada es "4", se inicia el proceso de gestión de moderación
        elif option == "4":
            # Se inicia un bucle infinito
            while True:
                # Se imprime un mensaje preguntando si el usuario es administrador de Metrogram
                print("\nEs usted administrador de Metrogram? \n\n- Si\n- No")
                # Se solicita al usuario que seleccione una opción
                admin = input("\nSeleccione una opción: ")
                # Si el usuario selecciona "Si", es decir, es un administrador
                if admin == "Si":
                    # Se imprime el menú de gestión de moderación
                    print("\n---||| Gestión de moderación |||---\n")
                    print("1. Eliminar post")
                    print("2. Eliminar comentario")
                    print("3. Eliminar usuario")
                    print("4. Eliminar posts de un usuario")
                    print("5. Eliminar comentarios de un usuario")
                    print("6. Regresar")
                    # Se solicita al usuario que seleccione una opción del menú de gestión de moderación
                    # Solicita al usuario que seleccione una opción
                    sub_option = input("\nSeleccione una opción: ")

                    # Si la opción seleccionada es "1"
                    if sub_option == "1":
                        # Solicita al usuario que ingrese un tipo de filtro
                        filter_type = input("Ingrese tipo de filtro: ")
                        # Solicita al usuario que ingrese un valor para el tipo de filtro seleccionado
                        filter_value = input(f"Ingrese {filter_type}: ")
                        # Solicita al usuario que ingrese una URL
                        url = input("Ingrese url: ")
                        # Llama al método delete_post de la clase moderacion para eliminar la publicación correspondiente
                        moderacion.delete_post(filter_type, filter_value, url)
                        # Imprime un mensaje indicando que la publicación ha sido eliminada
                        print("\nPost eliminado\n")

                    # Si la opción seleccionada es "2"
                    elif sub_option == "2":
                        # Solicita al usuario que ingrese un tipo de filtro para el post del usuario
                        filter_type = input("Ingrese tipo de filtro para el post del ususario: ")
                        # Solicita al usuario que ingrese un valor para el tipo de filtro seleccionado
                        filter_value = input(f"Ingrese {filter_type}: ")
                        # Solicita al usuario que ingrese una URL
                        url = input("Ingrese url: ")
                        # Solicita al usuario que ingrese un comentario
                        comment = input("Ingrese comentario: ")
                        # Llama al método delete_comment de la clase moderacion para eliminar el comentario correspondiente
                        moderacion.delete_comment(filter_type, filter_value, url, comment)
                        # Imprime un mensaje indicando que el comentario ha sido eliminado
                        print("\nComentario eliminado\n")
                    # Si la opción seleccionada es "3"
                    elif sub_option == "3":
                        # Solicita al usuario que ingrese un tipo de filtro
                        filter_type = input("Ingrese tipo de filtro: ")
                        # Solicita al usuario que ingrese un valor para el tipo de filtro seleccionado
                        filter_value = input(f"Ingrese {filter_type}: ")
                        # Llama al método delete_user de la clase moderacion para eliminar el usuario correspondiente
                        moderacion.delete_user(filter_type, filter_value)
                        # Imprime un mensaje indicando que el usuario ha sido eliminado
                        print("\nUsuario eliminado\n")

                    # Si la opción seleccionada es "4"
                    elif sub_option == "4":
                        # Solicita al usuario que ingrese un tipo de filtro
                        filter_type = input("Ingrese tipo de filtro: ")
                        # Solicita al usuario que ingrese un valor para el tipo de filtro seleccionado
                        filter_value = input(f"Ingrese {filter_type}: ")
                        # Llama al método delete_user_posts de la clase moderacion para eliminar las publicaciones del usuario correspondiente
                        moderacion.delete_user_posts(filter_type, filter_value)
                        # Imprime un mensaje indicando que las publicaciones del usuario han sido eliminadas
                        print("\nPosts eliminados\n")

                    # Si la opción seleccionada es "5"
                    elif sub_option == "5":
                        # Solicita al usuario que ingrese un tipo de filtro
                        filter_type = input("Ingrese tipo de filtro: ")
                        # Solicita al usuario que ingrese un valor para el tipo de filtro seleccionado
                        filter_value = input(f"Ingrese {filter_type}: ")
                        # Llama al método delete_user_comments de la clase moderacion para eliminar los comentarios del usuario correspondiente
                        moderacion.delete_user_comments(filter_type, filter_value)
                        # Imprime un mensaje indicando que los comentarios del usuario han sido eliminados
                        print("\nComentarios eliminados\n")

                    # Si la opción seleccionada es "6", se rompe el ciclo del submenú
                    elif sub_option == "6":
                        break

                    # Si el usuario selecciona "No" cuando se le pregunta si es un administrador de Metrogram
                    elif admin == "No":
                        # Se imprime un mensaje indicando que no tiene permisos de administrador
                        print("\nNo tiene permisos de administrador\n")
                        # Se rompe el ciclo del menú principal
                        break

                    # Si el usuario ingresa una opción inválida cuando se le pregunta si es un administrador de Metrogram
                    else:
                        # Se imprime un mensaje de error
                        print("\nOpción inválida\n")
                        # Se rompe el ciclo del menú principal
                        break

        elif option == "5":
            while True:
                print("\nEs usted administrador de Metrogram? \n\n- Si\n- No")
                admin = input("\nSeleccione una opción: ")
                if admin == "Si":
                    print("\n---||| Gestión de estadísticas |||---\n")
                    print("1. Informes de publicaciones")
                    print("2. Informes de interacción")
                    print("3. Informes de moderación")
                    print("4. Regresar")
                    sub_option = input("\nSeleccione una opción: ")

                    if sub_option == "1":
                        print("\n---||| Informes de publicaciones |||---\n")
                        print("1. Usuarios con mayor cantidad de publicaciones")
                        print("2. Carreras con mayor cantidad de publicaciones")
                        print("3. Regresar")
                        sub_option = input("\nSeleccione una opción: ")
                        if sub_option == "1":
                            print("\nUsuarios con mayor cantidad de publicaciones:\n")
                            print(f"\t{estadisticas.users_posts()}")
                            # grafico de barras
                            users = estadisticas.users_posts()
                            users_names = list(users.keys())
                            users_posts = list(users.values())
                            y_pos = np.arange(len(users_names))

                            plt.figure(figsize=(10, 5))  
                            plt.bar(y_pos, users_posts, align='center', alpha=0.5)
                            plt.xticks(y_pos, users_names, rotation=45, fontsize=12)  
                            plt.ylabel('Cantidad de publicaciones')
                            plt.title('Usuarios con mayor cantidad de publicaciones')
                            plt.show()

                        elif sub_option == "2":
                            print("\nCarreras con mayor cantidad de publicaciones:\n")
                            print(f"\t{estadisticas.careers_posts()}")
                            # grafico de barras
                            careers = estadisticas.careers_posts()
                            careers_names = list(careers.keys())
                            careers_posts = list(careers.values())
                            y_pos = np.arange(len(careers_names))

                            plt.figure(figsize=(10, 5))  
                            plt.bar(y_pos, careers_posts, align='center', alpha=0.5)
                            plt.xticks(y_pos, careers_names, rotation=45, fontsize=12)
                            plt.ylabel('Cantidad de publicaciones')
                            plt.title('Carreras con mayor cantidad de publicaciones')
                            plt.show()

                        elif sub_option == "3":
                            break

                        else:
                            print("\nOpción inválida\n")
                            break

                    elif sub_option == "2":
                        print("\n---||| Informes de interacción |||---\n")
                        print("1. Post con la mayor cantidad de interacciones")
                        print("2. Usuarios con la mayor cantidad de interacciones (dadas y enviadas)")
                        print("3. Regresar")
                        sub_option = input("\nSeleccione una opción: ")
                        if sub_option == "1":
                            if sub_option == "1":
                                print("\nPost con la mayor cantidad de interacciones:\n")
                                posts = estadisticas.post_interactions()
                                print(f"\t{posts}")
                                # grafico de barras
                                posts_urls = list(posts.keys())
                                posts_interactions = list(posts.values())
                                y_pos = np.arange(len(posts_urls))

                                plt.figure(figsize=(10, 5))
                                plt.bar(y_pos, posts_interactions, align='center', alpha=0.5)
                                plt.xticks(y_pos, posts_urls, rotation=45, fontsize=12)
                                plt.ylabel('Cantidad de interacciones')
                                plt.title('Post con la mayor cantidad de interacciones')
                                plt.show()

                        elif sub_option == "2":
                            print("\nUsuarios con la mayor cantidad de interacciones (dadas y enviadas):\n")
                            print(f"\t{estadisticas.users_interactions()}")
                            # grafico de barras
                            users = estadisticas.users_interactions()
                            users_names = list(users.keys())
                            users_interactions = list(users.values())
                            y_pos = np.arange(len(users_names))

                            plt.figure(figsize=(10, 5))
                            plt.bar(y_pos, users_interactions, align='center', alpha=0.5)
                            plt.xticks(y_pos, users_names, rotation=45, fontsize=12)
                            plt.ylabel('Cantidad de interacciones')
                            plt.title('Usuarios con la mayor cantidad de interacciones')
                            plt.show()
                            
                    elif sub_option == "3":
                        print("\n---||| Informes de moderación |||---\n")
                        print("1. Usuarios con mayor cantidad de post tumbados")
                        print("2. Carreras con mayor cantidad de comentarios eliminados")
                        print("3. Usuarios eliminados por infracciones")
                        print("4. Regresar")
                        sub_option = input("\nSeleccione una opción: ")
                        if sub_option == "1":
                            print("\nUsuarios con mayor cantidad de post tumbados:\n")
                            print(f"\t{estadisticas.users_with_posts_removed()}")
                            # grafico de barras
                            users = estadisticas.users_with_posts_removed()
                            users_names = list(users.keys())
                            users_posts_removed = list(users.values())
                            y_pos = np.arange(len(users_names))

                            plt.figure(figsize=(10, 5))
                            plt.bar(y_pos, users_posts_removed, align='center', alpha=0.5)
                            plt.xticks(y_pos, users_names, rotation=45, fontsize=12)
                            plt.ylabel('Cantidad de posts tumbados')
                            plt.title('Usuarios con mayor cantidad de posts tumbados')
                            plt.show()

                        elif sub_option == "2":
                            print("\nCarreras con mayor cantidad de comentarios eliminados:\n")
                            print(f"\t{estadisticas.major_comments_removed()}")
                            # grafico de barras
                            careers = estadisticas.major_comments_removed()
                            careers_names = list(careers.keys())
                            careers_comments = list(careers.values())
                            y_pos = np.arange(len(careers_names))
                            plt.bar(y_pos, careers_comments, align='center', alpha=0.5)
                            plt.xticks(y_pos, careers_names)
                            plt.ylabel('Cantidad de comentarios eliminados')
                            plt.title('Carreras con mayor cantidad de comentarios eliminados')
                            plt.show()

                        elif sub_option == "3":
                            print("\nUsuarios eliminados por infracciones:\n")
                            print(f"\t{estadisticas.users_deleted_in_moderation()}")
                            # grafico de barras
                            users = estadisticas.users_deleted_in_moderation()
                            users_names = users  
                            users_deleted = [1] * len(users)  
                            y_pos = np.arange(len(users_names))

                            plt.figure(figsize=(10, 5))  
                            plt.bar(y_pos, users_deleted, align='center', alpha=0.5)
                            plt.xticks(y_pos, users_names, rotation=45, fontsize=12)
                            plt.ylabel('Cantidad de usuarios eliminados')
                            plt.title('Usuarios eliminados por infracciones')
                            plt.show()

                        elif sub_option == "4":
                            break

                        else:
                            print("\nOpción inválida\n")
                            break

                    elif sub_option == "4":
                        break

                    else:
                        print("\nOpción inválida\n")
                        break
                elif admin == "No":
                    print("\nNo tiene permisos de administrador\n")
                    break
                else:
                    print("\nOpción inválida\n")
                    break

        elif option == "6":
            print("\nGracias por usar Metrogram!\n")
            break

        else:
            print("\nOpción inválida\n")
            break

main()