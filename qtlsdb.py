import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port='8889',
  database = "TraitsQTLs_genetics"
)

mycursor= mydb.cursor()
mycursor.execute("CREATE TABLE Datos_Generales (Persona_ID INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(100), Sexo ENUM('M','H'), Edad INT, Estado VARCHAR(20))")

mycursor.execute("CREATE TABLE Mediciones (Persona_ID INT, CONSTRAINT Persona_ID_FK FOREIGN KEY (Persona_ID) REFERENCES Datos_Generales (Persona_ID), Medicion_ID INT AUTO_INCREMENT PRIMARY KEY, Tipo VARCHAR(10), Valor FLOAT)")

data1=pd.read_csv('mediciones.csv', usecols=[0,1,2,3])
for row in data1.iterrows():
    sql= "INSERT INTO Datos_Generales (Nombre, Sexo, Edad, Estado) VALUES (%s, %s, %s, %s)"
    values=list(row[1])
    mycursor.execute(sql,values)
#hasta aqui ya esta poblada la primer tabla

mydb.commit()

for i in range(4,20):
    data2= pd.read_csv('mediciones.csv', usecols=[i])
    for row in data2.iterrows():
        sql= "INSERT INTO Mediciones (Valor) values (%s)"
        values=list(row[1])
        mycursor.execute(sql,values)
#con esto ya llenamos el valor de las mediciones de cada individuo

#generamos una lista que contenga el tipo de mediciones y el id
#al cual queremos actualizarlo
tipo= [0]*496
for i in range(len(tipo)):
    if i < 31:
        tipo[i]= ('Altura',i+1)
    if i >= 31 and i < 217:
        tipo[i]= ('Frente',i+1)
    if i >= 217 and i < 403:
        tipo[i]= ('Brazo',i+1)
    if i >= 403 and i < 434:
        tipo[i]= ('Calzado',i+1)
    if i >= 434 and i < 496:
        tipo[i]= ('Presion',i+1)

update= "update mediciones set tipo =%s where medicion_id = %s"
mycursor.executemany(update, tipo)

#un update para indicar a que persona pertenece la medicion
altura=[0]*31
for i in range(1,32):
    altura[i-1]= (i, i)
update= "update mediciones set persona_id =%s where medicion_id= %s"
mycursor.executemany(update, altura)

frente= [0]*186
b= 0
c= 1
for i in range(0,186):
    if b == 6:
        c= c+1
        b= 0
    frente[i]= (c,i+32)
    b= b+1
update= "update mediciones set persona_id=%s where medicion_id=%s"
mycursor.executemany(update, frente)
mydb.commit()

brazo= [0]*186
b= 0
c= 1
for i in range(0,186):
    if b == 6:
        c= c+1
        b= 0
    brazo[i]= (c,i+218)
    b= b+1
update= "update mediciones set persona_id=%s where medicion_id=%s"
mycursor.executemany(update, brazo)

calzado=[0]*31
for i in range(1,32):
    calzado[i-1]= (i, 404+i-1)
update= "update mediciones set persona_id =%s where medicion_id=%s"
mycursor.executemany(update, calzado)

presion= [0]*62
a= 0
for i in range(1,63):
    if i < 32:
        presion[i-1]= (i, 435+i-1)
    if i >= 32:
        a= a+1
        presion[i-1]= (a,466+a-1)
update= "update mediciones set persona_id =%s where medicion_id=%s"
mycursor.executemany(update, presion)
mydb.commit()
#y hasta aqui esta completa la base de datos
