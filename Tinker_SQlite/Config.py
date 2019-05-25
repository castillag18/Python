#import sqlite3

#conn = sqlite3.connect('Agenda.db')
#c = conn.cursor()

#def create_table():
#  c.execute("CREATE TABLE IF NOT EXISTS tabla1(Nombre TEXT, Apellido_Paterno TEXT, Apellido_Materno TEXT, Teléfono TEXT, correo TEXT)")
 
#def data_entry():
#  c.execute("INSERT INTO tabla1 VALUES('Man', 'Basto', 'Piñon', '3115647890', 'Man@gmail.com')")
#  conn.commit()
#  c.close()
#  conn.close()

#create_table()
#data_entry()