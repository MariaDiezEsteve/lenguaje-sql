#Para utilizar la librería de sqlite3 tenemos que importar el módulo
import sqlite3

#1. Conexión con la BBDD: universidad.db
#Si no existe al BBDD crea un archivo.
con = sqlite3.connect("universidad.db")
#Terminal: python sqlite_proyecto.py

#3.Crear un objeto cursor para hacer peticiones(querys)= consulta a la BBDD(sqlite3)
#cursor() = Se utiliza para hacer peticiones
cu = con.cursor()

#4. 1º Consulta: Crear una tabla -> En los parámetros ponemos la consulta que queremos hacer. Utilizamos  triple comillas porque va a ser un string párrafo.
#execute() sirve para manipular la BBDD de sqlite, solo escribe

cu.execute(""" CREATE TABLE IF NOT EXISTS estudiantes (
                matricula TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                promedio REAL)
            """)

#Si la tabla existe no la crea

#5. 2º Consulta: Insertar los datos de la tabla, varias maneras de hacerlo
#5.1 Ingresar directamente los datos: VALUES
cu.execute(""" INSERT INTO estudiantes VALUES("118", "Nadine", "Diez", 10) """)

#5.2 Insertar datos en una tabla con variables en forma de tupla:
#Se crea una clase estudiantes.py para añadir estudiantes mediante variables y no con con.execute()
#from estudiantes import Estudiante

# est_1 = Estudiante("222", "María", "Esteve", 10)
# est_2 = Estudiante("223", "Carolina", "Esteve", 5.5)
# est_3 = Estudiante("224", "Ana", "Esteve", 6.5)
# est_4 = Estudiante("213", "Fran", "Esteve", 8.5)

#Le estamos pasando dos argumentos al método execute: 1. La consulta que queremos hacer en este caso introducir los datos, y 2. que datos queremos introducir en forma de tupla
# cu.execute(" INSERT INTO estudiantes VALUES(?,?,?,?)",
#            (est_3.matricula, est_3.nombre, est_3.apellido, est_3.promedio))

#También se podrían introducir solo los valores que son obligatorios (NOT NULL) en este caso sería:
# cu.execute(" INSERT INTO estudiantes (matricula, nombre, apellidos) VALUES(?,?,?,?)",
#            (est_3.matricula, est_3.nombre, est_3.apellido))
#Para este caso el promedio del estudiante sería None porque no lo hemos incluido

#5.3 Insertar los datos con varibales en forma de diccionario

# cu.execute(" INSERT INTO estudiantes VALUES(:matricula,:nombre,:apellido,:promedio)", {
#     "matricula": est_4.matricula, "nombre": est_4.nombre, "apellido": est_4.apellido, "promedio":est_4.promedio})

#5.4 Insertar todos los datos de las variables est_1, est_2, est_4, est_4 a la vez con executemany()
# many_students = [
#     est_1 = Estudiante("222", "María", "Esteve", 10)
#     est_2 = Estudiante("223", "Carolina", "Esteve", 5.5)
#     est_3 = Estudiante("224", "Ana", "Esteve", 6.5)
#     est_4 = Estudiante("213", "Fran", "Esteve", 8.5)
# ]
# cu.execute(" INSERT INTO estudiantes VALUES(?,?,?,?)", many_students)

#commmit = guarda la petición en la BBDD "la crea"
con.commit()

#6. 3º Consulta: Seleccionar todos los estudiantes que están en mi BBDD
#* Selecciona todas las propiedades (matricula, nombre, apellido, promedio)
cu.execute("SELECT  * FROM estudiantes")

#Le asignamos a una variable toda la BBDD de la petición
#fetchall: nos devuelve todos los estudiantes
estudiantes = cu.fetchall()
print(estudiantes) #[('111', 'María', 'Diez', 9.5), ('112', 'Diez', 'Esteve', 9.5)] te devuelve una lista

#fetchmany(numero): cuantos estudiantes queremos que nos devuelva, y nos lo devuelve
estudiantes = cu.fetchmany(5)
print(estudiantes)

#7. 4º Consulta: selecionar un estudiante concreto de mi BBDD
#Necesito dos argumentos: 1º la consulta/petición a la BBDD donde WHERE sería la matricula concreta, y como 2º argumento le pasamos una tupla tenemos que incluir la "," para que se convierta en tupla
cu.execute("SELECT * FROM estudiantes WHERE matricula=?",("111",))

#Ejemplo para que me devuelva todos los elementos que contengan el apellido = "Diez"
#cu.execute("SELECT * FROM estudiantes WHERE apellido=?",("Diez",))
#En este caso, necesitariamos para recoger los datos: estudiantes = cu.fetchall()
#Cerra la BBDD
con.close()


""" CREAR UN CRUD MEDIANTE FUNCIONES """

# Insertar Valores 
#Crearemos una función que se llama estudiantes para ejecutar la inserción de estudiantes

def insertar_estudiantes(estu):
    con = sqlite3.connect("universidad.db")
    cu = con.cursor()
    cu.execute("INSERT INTO estudiantes VALUES (?,?,?,?)", 
               (estu.matricula, estu.nombre, estu.apellido, estu.promedio))
    con.commit()
    con.close()
    
#Crear la tabla de estudiantes
def create_student_table():
    con = sqlite3.connect("universidad.db")
    cu = con.cursor()
    cu.execute("""CREATE TABLE IF NOT EXISTS estudiantes (
        matricula TEXT PRIMARY KEY, 
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        promedio REAL)""")
    con.close()

#Seleccionar los estudiantes por matricula
def select_student(matricula):
    con = sqlite3.connect("universidad.db")
    cu = con.cursor()
    cu.execute("SELECT * FROM estudiantes WHERE matricula =?", (matricula,))
    estudiante = cu.fetchall()
    print(estudiante)
    con.close()
    return estudiante

#Actualizar la BBDD
def update_prom(matricula, prom):
    con = sqlite3.connect("universidad.db")
    cu = con.cursor()
    cu.execute("""UPDATE estudiantes SET promedio =? WHERE matricula=?, (prom, matricula)""")
    con.commit()
    con.close()

#Eliminar de la BBD
def delete_student(matricula):
    con = sqlite3.connect("universidad.db")
    cu =con.cursor()
    cu.execute("DELETE from estudiantes WHERE matricula=?", (matricula,))
    con.commit()
    con.close()
    return "" #En duda si hay que retornar algo vacío

#Seleccionar todos los valores
def select_all():
    con = sqlite3.connect("universidad.db")
    cu =con.cursor()
    cu.execute("SELECT * from estudiantes")
    estudiantes = cu.fetchall()
    con.commit()
    con.close()
    return estudiantes #Duda si hay que devolver los estudiantes aquí
