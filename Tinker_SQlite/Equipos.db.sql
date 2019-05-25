import sqlite3
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tabla2" (
	"Nombres"	INTEGER NOT NULL,
	"Apellidos"	TEXT NOT NULL,
	"Equipo al cual pertenece"	TEXT NOT NULL,
	"Pais"	TEXT NOT NULL,
	"Peso (Kg)"	INTEGER NOT NULL,
	"Altura (Mts)"	INTEGER NOT NULL,
	"Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);
INSERT INTO "tabla2" ("Nombres","Apellidos","Equipo al cual pertenece","Pais","Peso (Kg)","Altura (Mts)","Id") VALUES ('Adolfo','','','',0,0,1),
 ('Hernan','Martinez Perez','Cali','Colombia',81,1.53,2),
 ('Carlos
','Gates Gates','Nacional','Colombia',90,2.1,3),
 ('Miguel','Perreo Perreo','Junior','Colombia',70,1.85,4),
 ('Pedro','Junior Pila','River Play','Argentina',50,1.9,5);
COMMIT;
