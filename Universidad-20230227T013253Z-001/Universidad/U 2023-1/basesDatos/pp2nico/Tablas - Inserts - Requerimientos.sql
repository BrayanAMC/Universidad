-------------------------------------------------------------------------------------------------
--Drops
-------------------------------------------------------------------------------------------------
drop table disco_cancion;
drop table integrante_banda;
drop table disco;
drop table cancion;
drop table persona;
drop table banda;
-------------------------------------------------------------------------------------------------
--Tablas
-------------------------------------------------------------------------------------------------
create table persona(
    rut text not null,
    nombre_persona text not null,
    fecha_nacimiento date not null,
    primary key(rut)
);

create table cancion(
    nombre_cancion text not null,
    rut_autor text not null,
    duracion_segundos int not null,
    year_creacion int not null,
    primary key(nombre_cancion, rut_autor),
    foreign key(rut_autor) references persona(rut)
);

create table banda(
    nombre_banda text not null,
    year_formacion int not null,
    primary key(nombre_banda)
);

create table integrante_banda(
    nombre_banda text not null,
    rut text not null,
    fecha_inicio date not null,
    fecha_fin date,
    foreign key(nombre_banda) references banda(nombre_banda),
    foreign key(rut) references persona(rut)
);

create table disco(
    nombre_banda text not null,
    nombre_disco text not null,
    year_publicacion int not null,
    primary key(nombre_banda, nombre_disco),
    foreign key(nombre_banda) references banda(nombre_banda)
);

create table disco_cancion(
    nombre_banda text not null,
    nombre_disco text not null,
    nombre_cancion text not null,
    rut_autor text not null,
    posicion_track int not null,
    foreign key(nombre_banda, nombre_disco) references disco(nombre_banda, nombre_disco),
    foreign key(nombre_cancion, rut_autor) references cancion(nombre_cancion, rut_autor)
);
-------------------------------------------------------------------------------------------------
--Inserts
-------------------------------------------------------------------------------------------------
--Insertar persona
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('18187068-0', 'Danny Carey', '1961-05-10');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('13908444-6', 'Adam Jones', '1965-01-15');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('12556234-5', 'Maynard James Keenan', '1964-04-17');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('19588802-7', 'Justin Chancellor', '1971-11-19');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('10518118-3', 'Paul D.Amour', '1965-05-12');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('17153576-k', 'Serj Tankian', '1967-08-21');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('16777290-0', 'Daron Malakian', '1975-07-18');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('10187943-7', 'Shavo Odadjian', '1974-04-21');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('12829835-5', 'John Dolmayan', '1973-07-15');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('20169104-4', 'Nicolas Bravo', '1989-02-09');
insert into persona(rut, nombre_persona, fecha_nacimiento) values ('19456890-2', 'Lalo Landa', '1975-09-09');

--Insertar banda
insert into banda(nombre_banda, year_formacion) values ('Tool', 1990);
insert into banda(nombre_banda, year_formacion) values ('System of a Down', 1994);

--Insertar integrante_banda
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('Tool', '18187068-0', '1990-08-09');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('Tool', '13908444-6', '1990-08-09');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('Tool', '12556234-5', '1990-08-09');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('Tool', '19588802-7', '1990-08-09');
insert into integrante_banda(nombre_banda, rut, fecha_inicio, fecha_fin) values ('Tool', '20169104-4', '1990-08-09', '2000-05-07');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('System of a Down', '17153576-k', '1994-03-20');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('System of a Down', '16777290-0', '1994-03-20');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('System of a Down', '10187943-7', '1994-03-20');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('System of a Down', '12829835-5', '1994-03-20');
insert into integrante_banda(nombre_banda, rut, fecha_inicio) values ('System of a Down', '20169104-4', '2001-09-02');
insert into integrante_banda(nombre_banda, rut, fecha_inicio, fecha_fin) values ('Tool', '19456890-2', '1990-08-09', '2000-05-07');

--Insertar disco
insert into disco(nombre_banda, nombre_disco, year_publicacion) values ('Tool', 'Lateralus', 2001);
insert into disco(nombre_banda, nombre_disco, year_publicacion) values ('System of a Down', 'Toxicity', 2002);

--Insertar cancion
insert into cancion(nombre_cancion, rut_autor, duracion_segundos, year_creacion) values ('Schism', '12556234-5', 388, 2001);
insert into cancion(nombre_cancion, rut_autor, duracion_segundos, year_creacion) values ('Parabola', '12556234-5', 361, 2001);
insert into cancion(nombre_cancion, rut_autor, duracion_segundos, year_creacion) values ('Lateralus', '12556234-5', 553, 2000);
insert into cancion(nombre_cancion, rut_autor, duracion_segundos, year_creacion) values ('Chop Suey', '17153576-k', 199, 2001);
insert into cancion(nombre_cancion, rut_autor, duracion_segundos, year_creacion) values ('Toxicity', '17153576-k', 203, 2001);
insert into cancion(nombre_cancion, rut_autor, duracion_segundos, year_creacion) values ('Aerials', '17153576-k', 214, 2001);

--Insertar disco_cancion
insert into disco_cancion(nombre_banda, nombre_disco, nombre_cancion, rut_autor, posicion_track) values ('Tool', 'Lateralus', 'Schism', '12556234-5', 1);
insert into disco_cancion(nombre_banda, nombre_disco, nombre_cancion, rut_autor, posicion_track) values ('Tool', 'Lateralus', 'Parabola', '12556234-5', 2);
insert into disco_cancion(nombre_banda, nombre_disco, nombre_cancion, rut_autor, posicion_track) values ('Tool', 'Lateralus', 'Lateralus', '12556234-5', 3);
insert into disco_cancion(nombre_banda, nombre_disco, nombre_cancion, rut_autor, posicion_track) values ('System of a Down', 'Toxicity', 'Chop Suey', '17153576-k', 1);
insert into disco_cancion(nombre_banda, nombre_disco, nombre_cancion, rut_autor, posicion_track) values ('System of a Down', 'Toxicity', 'Toxicity', '17153576-k', 2);
insert into disco_cancion(nombre_banda, nombre_disco, nombre_cancion, rut_autor, posicion_track) values ('System of a Down', 'Toxicity', 'Aerials', '17153576-k', 3);
-------------------------------------------------------------------------------------------------
--Triggers
-------------------------------------------------------------------------------------------------
--a) Crear un trigger que no permita agregar/editar integrantes cuya fecha de nacimiento sea menor que la fecha de inicio en la banda:

--Trigger (Funcion)
create or replace function verificar_a() returns trigger
language plpgsql
AS $$
DECLARE
    _var1 RECORD;
    _var2 RECORD;
    _fecha_creacion int;
    _fecha_nacimiento int;
BEGIN
    for _var1 in
        select persona.fecha_nacimiento as fecha_nacimiento
        from persona
        where persona.rut = NEW.rut
    loop
        SELECT EXTRACT(year FROM _var1.fecha_nacimiento) into _fecha_nacimiento;
    end loop;
    for _var2 in
        select banda.year_formacion as year_formacion
        from banda
        where banda.nombre_banda = NEW.nombre_banda
    loop
        _fecha_creacion := _var2.year_formacion;
    end loop;
    if(_fecha_nacimiento < _fecha_creacion) THEN
        return new;
    else
        return null;
    end if;
END; $$;

--Trigger
create or replace trigger t_verificar_a
BEFORE INSERT OR UPDATE
ON integrante_banda
for each row
execute procedure verificar_a();


--b) Crear un trigger que no permita agregar/editar integrantes que tengan fecha inicio o fecha fin anterior al año de formacion de la banda:

--Trigger (Funcion)
create or replace function verificar_b() returns trigger
language plpgsql
AS $$
DECLARE
    _var RECORD;
    _fecha_creacion int;
    _fecha_inicio int;
    _fecha_fin int := 0;
BEGIN
    SELECT EXTRACT(year FROM NEW.fecha_inicio) into _fecha_inicio;
    if(NEW.fecha_fin is not null) then
        SELECT EXTRACT(year FROM NEW.fecha_fin) into _fecha_fin;
    end if;
    for _var in
        select banda.year_formacion as year_formacion
        from banda
        where banda.nombre_banda = NEW.nombre_banda
    loop
        _fecha_creacion = _var.year_formacion;
    end loop;
    if(_fecha_fin != 0) then
        if(_fecha_inicio >= _fecha_creacion and _fecha_fin >= _fecha_creacion) THEN
            return new;
        else
            return null;
        end if;
    else
        if(_fecha_inicio >= _fecha_creacion) then
            return new;
        else
            return null;
        end if;
    end if;
END; $$;

--Trigger
create or replace trigger t_verificar_b
BEFORE INSERT OR UPDATE
ON integrante_banda
for each row
execute procedure verificar_b();


--c) Crear un trigger que no permita agregar/editar integrantes cuya fecha inicio y fecha fin se solape con algun periodo de la misma persona en la misma banda:

--Trigger (Funcion)
create or replace function verificar_c() returns trigger
language plpgsql
AS $$
DECLARE
    _cont int := 0;
BEGIN
    if(NEW.fecha_fin is not null) then
        select count(*) into _cont
        from integrante_banda
        where integrante_banda.rut = NEW.rut and NEW.fecha_inicio BETWEEN integrante_banda.fecha_inicio and integrante_banda.fecha_fin and NEW.fecha_fin BETWEEN integrante_banda.fecha_inicio and integrante_banda.fecha_fin;
        if(_cont = 0) then
            return new;
        else
            return null;
        end if;
    else
        select count(*) into _cont
        from integrante_banda
        where integrante_banda.rut = NEW.rut and NEW.fecha_inicio BETWEEN integrante_banda.fecha_inicio and integrante_banda.fecha_fin;
        if(_cont = 0) then
            return new;
        else
            return null;
        end if;
    end if;
END; $$;

--Trigger
create or replace trigger t_verificar_c
BEFORE INSERT OR UPDATE
ON integrante_banda
for each row
execute procedure verificar_c();


--d) Crear un trigger que no permita agregar/editar discos a una banda con año de publicacion inferior al año de formacion de esta:

--Trigger (Funcion)
create or replace function verificar_d() returns trigger
language plpgsql
AS $$
DECLARE
    _var RECORD;
    _fecha_creacion int;
BEGIN
    for _var in
        select banda.year_formacion as year_formacion
        from banda
        where banda.nombre_banda = NEW.nombre_banda
    loop
        _fecha_creacion = _var.year_formacion;
    end loop;
    if(NEW.year_publicacion >= _fecha_creacion) then
        return new;
    else
        return null;
    end if;
END; $$;

--Trigger
create or replace trigger t_verificar_d
BEFORE INSERT OR UPDATE
ON disco
for each row
execute procedure verificar_d();


-------------------------------------------------------------------------------------------------
--Requerimientos
-------------------------------------------------------------------------------------------------
--e) Crear una funcion que retorne la duracion (en segundos) de un disco de una banda:

create or replace function funcion_e(_nombre_disco text) returns text
language plpgsql
AS $$
DECLARE
    _var RECORD;
    _existe bool := False;
    _suma int := 0;
    _res text;
BEGIN
    for _var in
        select cancion.duracion_segundos as duracion
        from disco_cancion
        inner join cancion on cancion.nombre_cancion = disco_cancion.nombre_cancion
        where disco_cancion.nombre_disco = _nombre_disco
    loop
        _existe := True;
        _suma := _suma + _var.duracion;
    end loop;
    if(_existe) then
        _res := 'El disco '||_nombre_disco||' tiene una duracion de '||_suma||' segundos';
    else
        _res := 'El disco no existe';
    end if;
    return _res;
END; $$;


--f) Liste la persona que ha sido integrante de mas bandas (puede haber mas de una):

select *
from (
    select persona.nombre_persona as nombre, count(*) as cant_de_grupos
    from persona
    inner join integrante_banda on integrante_banda.rut = persona.rut
    GROUP BY nombre_persona
) as tabla
where cant_de_grupos = (
    select max(cant_de_grupos) 
    from (
    select persona.nombre_persona as nombre, count(*) as cant_de_grupos
    from persona
    inner join integrante_banda on integrante_banda.rut = persona.rut
    GROUP BY nombre_persona) as maximo
)


--g) Liste la banda que ha tenido mas integrantes (phmdu):

select *
from (
    select banda.nombre_banda as nombre, count(*) as cant_de_integrantes
    from banda
    inner join integrante_banda on integrante_banda.nombre_banda = banda.nombre_banda
    GROUP BY banda.nombre_banda
) as tabla
where cant_de_integrantes = (
    select max(cant_de_integrantes) 
    from (
    select banda.nombre_banda as nombre, count(*) as cant_de_integrantes
    from banda
    inner join integrante_banda on integrante_banda.nombre_banda = banda.nombre_banda
    GROUP BY banda.nombre_banda) as maximo
)


--h) Liste la banda con mas discos (phmdu):

select *
from (
    select banda.nombre_banda as nombre, count(*) as cant_de_discos
    from banda
    inner join disco on disco.nombre_banda = banda.nombre_banda
    GROUP BY banda.nombre_banda
) as tabla
where cant_de_discos = (
    select max(cant_de_discos) 
    from (
    select banda.nombre_banda as nombre, count(*) as cant_de_discos
    from banda
    inner join disco on disco.nombre_banda = banda.nombre_banda
    GROUP BY banda.nombre_banda) as maximo
)


--i) Liste la cancion mas usada en discos (phmdu):

select *
from (
    select cancion.nombre_cancion as nombre, count(*) as cant_de_canciones
    from cancion
    inner join disco_cancion on disco_cancion.nombre_cancion = cancion.nombre_cancion
    GROUP BY cancion.nombre_cancion
) as tabla
where cant_de_canciones = (
    select max(cant_de_canciones) 
    from (
    select cancion.nombre_cancion as nombre, count(*) as cant_de_canciones
    from cancion
    inner join disco_cancion on disco_cancion.nombre_cancion = cancion.nombre_cancion
    GROUP BY cancion.nombre_cancion) as maximo
)


--j) Para un rut de una persona, liste las bandas donde ha estado, indicando por cada una la cantidad de dias de permanencia:

create or replace function funcion_j(_rut text) returns table (banda text, dias int)
language plpgsql
AS $$
DECLARE
    _var RECORD;
BEGIN
    for _var in
        select integrante_banda.nombre_banda as banda, integrante_banda.fecha_inicio as fecha_inicio, integrante_banda.fecha_fin as fecha_fin
        from integrante_banda
        where integrante_banda.rut = _rut
    loop
        banda := _var.banda;
        if(_var.fecha_fin is not null) then
            dias := _var.fecha_fin - _var.fecha_inicio;
        else
            dias := current_date - _var.fecha_inicio;
        end if;
        return next;
    end loop;
END; $$;

select * from funcion_j('20169104-4');