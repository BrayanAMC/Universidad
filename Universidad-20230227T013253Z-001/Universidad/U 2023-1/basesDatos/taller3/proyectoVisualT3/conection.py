from psycopg2 import connect, Error
import datetime
import re

import psycopg2


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
def validar_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
      

def check_estado_membresia(membership_date):
    current_date = datetime.date.today()
    if membership_date > current_date:
        print("La membresía está vigente.")
    elif membership_date == current_date:
        print("Hoy es el último día de la membresía.")
    else:
        print("La membresía ha vencido.")
def validar_id():

    while True:
        try:
            id = int(input("Ingrese un ID del miembro que desea saber toda su  (un número entero positivo): "))
            if id <= 0:
                print("El ID debe ser un número entero positivo. Intente nuevamente.")
            else:
                #print("ha elegido el id: "+ str(id))
                return id
        except ValueError:
            print("El ID debe ser un número entero positivo. Intente nuevamente.")

           
def mostrar_opciones_miembros(arr):
    for miembro in arr:
        print(f"ID: {miembro[0]}")
        print(f"Nombre: {miembro[1]}")
        print("--------------------")

def mostrar_datos_clases(arr):
    lista_id_existente = []
    for miembro in arr:
        print(f"ID: {miembro[0]}")
        print(f"Nombre: {miembro[1]}")
        print(f"Fecha: {miembro[2]}")
        print(f"BLoque: {miembro[3]}")
        print(f"Instructor: {miembro[4]}")
        print("--------------------")
        lista_id_existente.append(miembro[0])
    return lista_id_existente    

def mostrar_datos_miembro(arr):
    for miembro in arr:
        print(f"ID: {miembro[0]}")
        print(f"Nombre: {miembro[1]}")
        print(f"Email: {miembro[2]}")
        print(f"Edad: {miembro[4]}")
        print(f"Dirección: {miembro[5]}")
        print(f"Teléfono: {miembro[6]}")
        print("--------------------")

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
        print(f"imprimiendo result_miembro: {result_miembro} ")
        menu_miembro(int(result_miembro[0]))
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

def menu_miembro(id_miembro):
    while True:
        print("\nMenú Miembro:")
        print("1. Ver información personal")
        print("2. Ver horario de clases")
        print("3. Registrar asistencia")
        print("4. Salir del sistema")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            ver_informacion_personal(id_miembro)
        elif opcion == "2":
            ver_lista_clases(1)
        elif opcion == "3":
            registrar_asistencia(id_miembro)
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

def ver_informacion_miembro():
    # Lógica para ver la información de un miembro

    # Conexión a la base de datos
    conn= connection()
    
    # Crear el cursor
    cursor = conn.cursor()
    #paso 1 obtener toda las tuplas de miembro
    query_info_miembro = "select * from miembro"
    cursor.execute(query_info_miembro)
    result_info_miembro = cursor.fetchall()
    #esta funcion mostrara las opciones disponibles de miembros
    #para la cual se desea saber sus datos
    mostrar_opciones_miembros(result_info_miembro)
    id_validado = validar_id()#validamos que el id tenga el formato correcto
    print(f"id validado es: {id_validado}")
    query_info_miembro_id = "select * from miembro where id = %s "
    cursor.execute(query_info_miembro_id,(id_validado,))
    result_info_miembro_id = cursor.fetchone()
    #si el id existe en la tabla miembro devolvera los datos solicitados
    if result_info_miembro_id:
        #print(result_info_miembro_id)
        print("Información del miembro:")
        print(f"ID: {result_info_miembro_id[0]}")
        print(f"Nombre: {result_info_miembro_id[1]}")
        print(f"Correo: {result_info_miembro_id[2]}")
        print(f"Contraseña: {result_info_miembro_id[3]}")
        print(f"Edad: {result_info_miembro_id[4]}")
        print(f"Dirección: {result_info_miembro_id[5]}")
        print(f"Teléfono: {result_info_miembro_id[6]}")

        query_info_miembro_membresia = "select * from membresia where id_miembro = %s"
        cursor.execute(query_info_miembro_membresia,(id_validado,))
        result_info_miembro_membresia = cursor.fetchone()
        if result_info_miembro_membresia:#el miembro si tiene membresia
            check_estado_membresia(result_info_miembro_membresia[2])
            print("fecha vencimiento: " + str(result_info_miembro_membresia[2]))
            #print(result_info_miembro_membresia)
        else:
            print("el miembro no tiene membresia")   

    else:#si el id no existe en la base de datos, retornara "None" indicativo de que el id no existe.

        print("el id no existe,saliendo...")

    #mostrar la informacion solicitada con el id suministrado

    #mostrar_datos_miembro(result_info_miembro)
    #print(result_info_miembro)


    pass

def actualizar_membresia():
    # Lógica para actualizar la membresía de un miembro
    pass

def ver_membresias_vencidas():
    # Lógica para ver el informe de membresías vencidas
    pass

def agregar_clases():
    # Lógica para agregar nuevas clases al programa del gimnasio
    pass

#def ver_lista_clases():
    # Lógica para ver la lista de clases disponibles
    pass



def ver_informacion_personal(id_miembro):
    # Lógica para ver la información personal del miembro
    # Conexión a la base de datos
    conn= connection()
    # Crear el cursor
    cursor = conn.cursor()

    query_info_miembro_id = "select * from miembro where id = %s "
    cursor.execute(query_info_miembro_id,(id_miembro,))
    result_info_miembro_id = cursor.fetchone()
    print("su informacion es la siguiente:")
    print(f"ID: {result_info_miembro_id[0]}")
    print(f"Nombre: {result_info_miembro_id[1]}")
    print(f"Correo: {result_info_miembro_id[2]}")
    print(f"Contraseña: {result_info_miembro_id[3]}")
    print(f"Edad: {result_info_miembro_id[4]}")
    print(f"Dirección: {result_info_miembro_id[5]}")
    print(f"Teléfono: {result_info_miembro_id[6]}")

    query_info_miembro_membresia = "select * from membresia where id_miembro = %s"
    cursor.execute(query_info_miembro_membresia,(id_miembro,))
    result_info_miembro_membresia = cursor.fetchone()
    if result_info_miembro_membresia:#el miembro si tiene membresia
        check_estado_membresia(result_info_miembro_membresia[2])
        print("fecha vencimiento membresia: " + str(result_info_miembro_membresia[2]))
        #print(result_info_miembro_membresia)
    else:
        print("el miembro no tiene membresia") 

    pass



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

def registrar_asistencia(id_miembro):
    # Lógica para registrar la asistencia del miembro a una clase
    
    # Conexión a la base de datos
    conn= connection()
    # Crear el cursor
    cursor = conn.cursor() 
    listaID = ver_lista_clases(2)
    id_submit = int(input("seleccione el id de la clase que desea registrar asistencia: "))
    
    #preguntar por fecha 
    if  id_submit not in listaID:
        print("el id ingresado no existe en la lista de clases:")
    else:
        query = "select fecha, bloque, instructor from clase where id_clase = %s"
        cursor.execute(query,(id_submit,))
        resultado = cursor.fetchone()
        fecha_clase = resultado[0]
        bloque_clase = resultado[1]
        instructor_clase = resultado[2]
        cursor.execute(
            "insert into asistencia (id_miembro, id_clase, fecha_clase, bloque_clase, instructor_clase)"
            "values (%s, %s, %s, %s, %s)",
            (id_miembro, id_submit, fecha_clase, bloque_clase, instructor_clase)
        )
        conn.commit()
        print("asistencia ingresada satisfactoriamente")

    """
    try:

        cursor.execute(
            "insert into asistencia (fecha,id_miembro, id_clase)"
            "values (%s, %s, %s)",
            (fecha_asistencia, id_miembro, id_validado_clase)
        )
        
    except psycopg2.errors.lookup("23503"):
        print("debe seleccionar una clase que exista")

    
    if cursor.rowcount > 0:
        print("La asistencia se ha registrado correctamente.")
        
    """
    #result_info_miembro = cursor.fetchall()
    #print(result_info_miembro)
    pass

def connection():
    try:
        connection = connect(host='localhost',database='GimnasioDB',user='postgres', password='123', port='5432')
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