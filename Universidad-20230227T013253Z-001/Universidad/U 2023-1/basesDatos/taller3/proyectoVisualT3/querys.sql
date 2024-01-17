CREATE TABLE Administrador (
	id SERIAL PRIMARY KEY,
	nombre TEXT not null,
    	correo TEXT UNIQUE,
	contraseña TEXT not null
);

create table clase(
    id_clase serial not null,
    nombre text not null,
    fecha DATE not null,
    bloque text not null,
    instructor text not null,
    PRIMARY KEY (id_clase,fecha, bloque,instructor)
);


CREATE TABLE Miembro(
	id SERIAL PRIMARY KEY,
	nombre TEXT not null,
	correo TEXT UNIQUE,
	contraseña TEXT not null,
	edad INT not null,
	direccion TEXT not null,
	telefono TEXT not null
);

create table Membresia(
  id serial primary key,
  tipo text not null,
  fecha_vencimiento date not null,
  id_Miembro serial ,
  foreign key(id_Miembro) references Miembro(id)
);

CREATE TABLE asistencia (
    id_asistencia SERIAL PRIMARY KEY,
    id_miembro SERIAL NOT NULL,
    id_clase SERIAL NOT NULL,
    fecha_clase date not null,
    bloque_clase text not null,
    instructor_clase text not null,
    FOREIGN KEY (id_miembro) REFERENCES Miembro (id),
    FOREIGN KEY (id_clase,fecha_clase,bloque_clase,instructor_clase) REFERENCES clase (id_clase,fecha, bloque, instructor)
);

insert into administrador(nombre,correo,contraseña)
values('Carlos','gimnasiocarlos@gmail.com', 'CNaRa11Z')

insert into administrador(nombre,correo,contraseña)
values('a','1', '1')

insert into clase(nombre, fecha, bloque, instructor)
values('zumba', '2024-01-01', 'a', 'jack black')
insert into clase(nombre, fecha, bloque, instructor)
values('power lifting', '2024-01-02', 'c', 'darth vader')
insert into clase(nombre, fecha, bloque, instructor)
values('taekwando', '2024-05-01', 'c', 'jackie chan')

insert into Miembro(nombre, correo, contraseña, edad, direccion, telefono)
values('alex', 'alex@gmail.com', '1', 50, 'calle 3', '45678943')
insert into Miembro(nombre, correo, contraseña, edad, direccion, telefono)
values('bob', 'bob@gmail.com', '1', 34, 'calle 2', '32456787')


insert into Membresia(tipo, fecha_vencimiento, id_miembro)
values('premium', '2025-01-01', 1)

insert into asistencia(id_miembro,  id_clase, fecha_clase, bloque_clase, instructor_clase)
values(2, 2, '2024-01-02', 'c', 'darth vader')
