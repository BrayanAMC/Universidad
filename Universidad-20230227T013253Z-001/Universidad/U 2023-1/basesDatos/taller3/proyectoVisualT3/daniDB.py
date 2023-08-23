from psycopg2 import connect, Error

import re
import datetime


def user_login():
    print("Ingrese sus credenciales.")
    correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")

    # Conexión a la base de datos
    conn= connection()
    
    # Crear el cursor
    cursor = conn.cursor()

    # Consulta para verificar las credenciales del administrador
    query_admin = "SELECT correo FROM administrador WHERE correo = %s AND contraseña = %s"
    cursor.execute(query_admin, (correo, contraseña))
    result_admin = cursor.fetchone()

    # Consulta para verificar las credenciales del miembro
    query_miembro = "SELECT id FROM miembro WHERE correo = %s AND contraseña = %s"
    cursor.execute(query_miembro, (correo, contraseña))
    result_miembro = cursor.fetchone()

    if result_admin:
        print("Inicio de sesión exitoso como administrador")
        menu_administrador()
    elif result_miembro:
        print("Inicio de sesión exitoso como miembro")
        menu_miembro()
    else:
        print("Credenciales inválidas")


    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()


def menu_administrador():
    while True:
        print("\nMenú Administrador:")
        print("1. Registrar nuevo miembro")
        print("2. Ver información de un miembro")
        print("3. Actualizar membresía")
        print("4. Ver informe de membresías vencidas")
        print("5. Agregar clases")
        print("6. Ver lista de clases")
        print("7. Ver registro de asistencia")
        print("8. Salir del sistema")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            registrar_nuevo_miembro()
        elif opcion == "2":
            ver_informacion_miembro()
        elif opcion == "3":
            actualizar_membresia()
        elif opcion == "4":
            ver_membresias_vencidas()
        elif opcion == "5":
            agregar_clases()
        elif opcion == "6":
            ver_lista_clases(1)
        elif opcion == "7":
            ver_registro_asistencia()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def menu_miembro():
    while True:
        print("\nMenú Miembro:")
        print("1. Ver información personal")
        print("2. Ver horario de clases")
        print("3. Registrar asistencia")
        print("4. Salir del sistema")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            ver_informacion_personal()
        elif opcion == "2":
            ver_horario_clases()
        elif opcion == "3":
            registrar_asistencia()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def registrar_miembro():
    
    pass

def validar_email(email):
    # Conexión a la base de datos
    conn= connection()
    
    # Crear el cursor
    cursor = conn.cursor()
    
    # Patrón para una dirección de email válida
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'  

    cursor.execute("SELECT correo FROM Miembro WHERE correo = %s", (email,))
    existing_email = cursor.fetchone()

    cursor.execute("SELECT correo FROM Administrador WHERE correo = %s", (email,))
    existing_email2 = cursor.fetchone()


    if existing_email or existing_email2:
        print("El correo ya está registrado, ingrese uno nuevo.")
        conn.close()  # Close the database connection


    if re.match(patron, email) and not existing_email:
        if re.match(patron, email) and not existing_email2:
            return True
    else:
        return False

def validar_password(password):
    # Verificar la longitud de la contraseña
    if len(password) < 6 or len(password) > 8:
        return False

    # Verificar si hay al menos una letra mayúscula y un número utilizando regex
    patron_mayuscula = r'[A-Z]'
    patron_numero = r'\d'

    if not re.search(patron_mayuscula, password) or not re.search(patron_numero, password):
        return False

    return True

def registrar_nuevo_miembro():
    # Conexión a la base de datos
    conn= connection()
    
    # Crear el cursor
    cursor = conn.cursor()
    
    print("Ingrese sus credenciales.")
    nombre = input("Ingrese su nombre: ")
    while not validar_string(nombre):
        print("Ingrese un nombre válido.")
        nombre = input("Ingrese su nombre: ")
    
    correo = input("Ingrese su correo: ")
    while not validar_email(correo):
        print("Ingrese un correo válido")
        correo = input("Ingrese su correo: ")

    contraseña = input("Ingrese una contraseña: ")
    while not validar_password(contraseña):
        print("Ingrese una contraseña válida.")
        contraseña = input("Ingrese una contraseña: ")

    edad = int(input("Ingrese su edad: "))
    while not validar_edad(edad):
        print("Ingrese una edad válida.")
        edad = int(input("Ingrese su edad: "))

    direccion =input("Ingrese su dirección: ")
    while not validar_string(direccion):
        print("Ingrese una dirección válida.")
        direccion = input("Ingrese su dirección: ")

    telefono = input("Ingrese su teléfono: ")
    while not validar_telefono(telefono):
        print("Ingrese un teléfono válido.")
        telefono = input("Ingrese su teléfono: ")
    
    #aqui falta validar
    cursor.execute(
        "INSERT INTO Miembro (nombre, correo, contraseña, edad, direccion, telefono) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (nombre, correo, contraseña, edad, direccion, telefono)
    )
    
    conn.commit()

    print("Usuario agregado correctamente.")

def validar_edad(edad):
    # Validar la edad
    if edad < 0 or edad > 120:
        return False
    return True

def validar_string(dato):
    if dato == "":
        return False
    else:
        return True

def validar_telefono(numero_telefono):
    patron = r'^\d{8}$'  # Patrón para números de teléfono de 8 dígitos

    if re.match(patron, numero_telefono):
        return True
    else:
        return False

def check_estado_membresia(membership_date):
    current_date = datetime.date.today()
    if membership_date > current_date:
        print("La membresía está vigente.")
        print(f"La fecha de vencimiento es el {membership_date}.")
    elif membership_date == current_date:
        print("Hoy es el último día de la membresía.")
    else:
        print("La membresía ha vencido.")

def ver_informacion_miembro():
    # Lógica para ver la información de un miembro
    conn= connection()
    cursor = conn.cursor()
    
    query_admin= "SELECT * FROM miembro"
    cursor.execute(query_admin)
    lista_miembros= cursor.fetchall()
    lista_id_miembros= []
    
    print("Mostrando la lista de miembros.")
    for data in lista_miembros:
        lista_id_miembros.append(str(data[0]))
        print(f"ID: {data[0]} | Nombre: {data[1]}")
    print("----------------------")

    id_miembro= (input("Ingrese el ID del miembro para ver toda su información: "))
    if id_miembro not in lista_id_miembros:
        print("ID no encontrado.")
    else:
        query_admin= "SELECT * FROM miembro WHERE id=%s"
        cursor.execute(query_admin, (int(id_miembro),))
        info_miembro= cursor.fetchone()
        print("Información del miembro:")
        print(f"ID: {info_miembro[0]}")
        print(f"Nombre: {info_miembro[1]}")
        print(f"Correo: {info_miembro[2]}")
        print(f"Contraseña: {info_miembro[3]}")
        print(f"Edad: {info_miembro[4]}")
        print(f"Dirección: {info_miembro[5]}")
        print(f"Teléfono: {info_miembro[6]}")


        query2= "SELECT * FROM membresia WHERE id_miembro=%s"
        cursor.execute(query2, (int(id_miembro),))
        info_membresia= cursor.fetchone()
        if info_membresia is None:
            print("No tiene membresía.")
        else:
            check_estado_membresia(info_membresia[2])



def validar_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def actualizar_membresia():
    # Lógica para actualizar la membresía de un miembro
    conn= connection()
    cursor = conn.cursor()

    query_admin= "SELECT * FROM miembro"
    cursor.execute(query_admin)
    lista_miembros= cursor.fetchall()
    lista_id_miembros= []
    
    print("Mostrando la lista de miembros.")
    for data in lista_miembros:
        lista_id_miembros.append(str(data[0]))
        print(f"ID: {data[0]} | Nombre: {data[1]}")
    print("----------------------")

    id_miembro= (input("Ingrese el ID del miembro para actualizar su membresía: "))
    if id_miembro not in lista_id_miembros:
        print("ID no encontrado.")
        print("Saliendo al menú principal.")
    else:
        query2= "SELECT * FROM membresia WHERE id_miembro=%s"
        cursor.execute(query2, (int(id_miembro),))
        info_membresia= cursor.fetchone()
        if info_membresia is None:
            print("No tiene membresía.")
            
            crear_membresia = input("¿Desea otorgar una membresía? Ingrese sí o no: ").lower()
            while crear_membresia not in ["sí", "si", "no"]:
                crear_membresia = input("¿Desea otorgar una membresía? Ingrese sí o no: ").lower()
            
            if crear_membresia in ["sí", "si"]:
                tipo_membresia = input("Ingrese el tipo de membresía (normal o premium): ").lower()
                while tipo_membresia not in ["normal", "premium"]:
                    tipo_membresia = input("Ingrese el tipo de membresía (normal o premium): ").lower()

                f_vencimiento = input("Ingrese la fecha de vencimiento en el formato aaaa/mm/dd: ")
                while not validar_date(f_vencimiento):
                    f_vencimiento = input("Ingrese la fecha de vencimiento en el formato aaaa/mm/dd: ")

                query_crear_membresia = "INSERT INTO membresia(tipo,fecha_vencimiento,id_miembro) VALUES (%s,%s,%s)"
                cursor.execute(query_crear_membresia, (tipo_membresia, f_vencimiento, int(id_miembro)))
                conn.commit()
                print(f"Se ha creado la membresía para el ID {id_miembro}")

            elif crear_membresia == "no":
                print("Saliendo al menú principal.")

        else:
            check_estado_membresia(info_membresia[2])
            tipo_o_fecha= input("Ingrese 'tipo' o 'fecha' dependiendo de lo que quiera cambiar: ").lower()
            while tipo_o_fecha not in ["tipo", "fecha"]:
                tipo_o_fecha= input("Ingrese 'tipo' o 'fecha' dependiendo de lo que quiera cambiar: ").lower()
            if tipo_o_fecha == "tipo":
                tipo_membresia = input("Ingrese el tipo de membresía (normal o premium): ").lower()
                while tipo_membresia not in ["normal", "premium"]:
                    tipo_membresia = input("Ingrese el tipo de membresía (normal o premium): ").lower()
                query_update_tipo = "UPDATE membresia SET tipo=%s WHERE id_miembro = %s"
                cursor.execute(query_update_tipo,(tipo_membresia,id_miembro))
                conn.commit()
                print(f"Se ha actualizado el tipo de membresía a {tipo_membresia}")
                print("Saliendo al menú principal.")
            
            elif tipo_o_fecha == "fecha":
                fecha_membresia = input("Ingrese la fecha de vencimiento de la membresía: ")
                while not validar_date(fecha_membresia):
                    fecha_membresia = input("Ingrese la fecha de vencimiento de la membresía: ")
                
                query_update_tipo = "UPDATE membresia SET fecha_vencimiento=%s WHERE id_miembro = %s"
                cursor.execute(query_update_tipo,(fecha_membresia,id_miembro))
                conn.commit()
                print(f"Se ha actualizado la fecha de vencimiento a {fecha_membresia}")
                print("Saliendo al menú principal.")

def ver_membresias_vencidas():
    conn= connection()
    cursor = conn.cursor()

    current_date= datetime.date.today()

    query_vencidos= "SELECT id_miembro FROM membresia WHERE fecha_vencimiento < %s"
    cursor.execute(query_vencidos,(current_date,))
    id_miembros_vencidos= cursor.fetchall()


    query_miembros_vencidos= "SELECT * FROM miembro WHERE id = %s"
    if query_miembros_vencidos is None:
        print("No hay miembros con membresías vencidas.")
    else:
        print("Los miembros que tienen membresías vencidas son: ")
        for miembro in id_miembros_vencidos:
            cursor.execute(query_miembros_vencidos,(miembro[0],))
            miembros_vencidos= cursor.fetchall()
            print("Información del miembro:")
            print(f"ID: {miembros_vencidos[0][0]}")
            print(f"Nombre: {miembros_vencidos[0][1]}")
            print(f"Correo: {miembros_vencidos[0][2]}")
            print(f"Dirección: {miembros_vencidos[0][5]}")
            print(f"Teléfono: {miembros_vencidos[0][6]}")
            print("-------------------------")
    print("Saliendo al menú principal.")

def validar_bloque(string_bloque):
    if string_bloque not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return False
    else:
        return True

def bloques():
    return "A: 8:00 a 9:30, B: 9:30 a 11:00, C: 11:00 a 12:30, D: 12:30 a 14:00, E: 14:00 a 15:30, F: 15:30 a 17:00, G: 17:00 a 18:30, H: 18:30 a 20:00"

def agregar_clases():
    conn = connection()
    cursor = conn.cursor()
    print("Agregando una clase nueva")

    nombre_clase = input("Ingrese el nombre de la clase: ")
    while not validar_string(nombre_clase):
        nombre_clase = input("Ingrese el nombre de la clase: ")

    fecha_clase = input("Ingrese la fecha de la clase en el formato aaaa/mm/dd: ")
    while not validar_date(fecha_clase):
        fecha_clase = input("Ingrese la fecha de la clase en el formato aaaa/mm/dd: ")

    print(bloques())
    bloque_clase = input("Ingrese el bloque de la clase: ").lower()
    while not validar_bloque(bloque_clase):
        bloque_clase = input("Ingrese el bloque de la clase: ").lower()

    instructor_clase = input("Ingrese el nombre del instructor de la clase: ")
    while not validar_string(instructor_clase):
        instructor_clase = input("Ingrese el nombre del instructor de la clase: ")

    try:
        query_clases = "INSERT INTO clase(nombre, fecha, bloque, instructor) VALUES (%s, %s, %s, %s)"
        cursor.execute(query_clases, (nombre_clase, fecha_clase, bloque_clase, instructor_clase))
        conn.commit()
        print("La clase ha sido agregada satisfactoriamente.")
    except Exception as e:
        print("Error al ingresar la clase, el instructor ya tiene una clase registrada en este bloque y fecha.")
    finally:
        cursor.close()
        conn.close()


def ver_lista_clases(modo):
    conn = connection()
    cursor = conn.cursor()
    lista_id_clases= []

    query_lista_clases= "SELECT * FROM clase"
    try:
        cursor.execute(query_lista_clases)
        lista_clases= cursor.fetchall()
        if not lista_clases:
            print("No hay clases registradas.")
        else:
            print("Desplegando la lista de clases.")
            if modo == 1:
                for clase in lista_clases:
                    print(f"Nombre de la clase: {clase[1]} | Fecha: {clase[2]} | Bloque: {clase[3]} | Instructor: {clase[4]}")
            elif modo == 2:
                for clase in lista_clases:
                    lista_id_clases.append(clase[0])
                    print(f"ID de la clase: {clase[0]} | Nombre de la clase: {clase[1]} | Fecha: {clase[2]} | Bloque: {clase[3]} | Instructor: {clase[4]}")
                return lista_id_clases
    except Exception as e:
        print("Error malo.")
    finally:
        cursor.close()
        conn.close()


def ver_registro_asistencia():
    conn = connection()
    cursor = conn.cursor()
    
    lista_id_clases= ver_lista_clases(2)

    id_submit= int(input("Ingrese el ID de la clase a revisar asistencia: "))
    if id_submit not in lista_id_clases:
        print("El id ingresado no se encuentra en la lista de clases.")
    else:
        query_asistencia= "SELECT id_miembro FROM asistencia WHERE id_clase = %s"
        cursor.execute(query_asistencia,(id_submit,))
        id_miembros_asistencia= cursor.fetchall()
        if not id_miembros_asistencia:
            print("No hay nadie registrado en la clase.")
        else:
            for id_miembros in id_miembros_asistencia:
                query_miembro= "SELECT nombre FROM miembro WHERE id = %s"
                cursor.execute(query_miembro,(id_miembros,))
                nom_miembro= cursor.fetchone()
                print(f"ID: {id_miembros[0]} | Nombre miembro: {nom_miembro[0]}")

    cursor.close()
    conn.close()



    

def ver_informacion_personal():
    # Lógica para ver la información personal del miembro
    pass

def ver_horario_clases():
    # Lógica para ver el horario de clases disponibles
    pass

def registrar_asistencia():
    # Lógica para registrar la asistencia del miembro a una clase
    pass

def connection():
    try:
        connection = connect(host='localhost',database='GimnasioDB',user='postgres', password='0', port='5432')
        #print("it works, it connected.")
        return connection
       
    except(Exception, Error) as error:
        connection.rollback()
        print("Error: %s" % error)

def menu_login():
    while True:
        print("Bienvenido a la plataforma del gimnasio Carlos")
        print("Seleccione una de las siguientes opciones: ")
        print("1. Ingresar al sistema")
        print("2. Registrarse")
        print("3. Salir")
        
        opcion = input("Ingrese su respuesta: ")

        if opcion == "1":
            user_login()
        elif opcion == "2":
            registrar_nuevo_miembro()
        elif opcion == "3":
            print("Gracias por usar nuestro sistema")
            break;
        else:
            #cualquier otra opción le hace repetir el menú
            print("Opción no válida.")

# Ejecutar el menú de inicio de sesión
menu_login()