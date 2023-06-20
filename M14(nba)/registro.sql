create schema if not exists NBA;
use NBA;
create table if not exists usuario(

usuario varchar(50) not null primary key,
nombre varchar(50) not null,
apellidos varchar(50) not null,
edad int not null,
nacionalidad varchar(100),
contraseña varchar(50) not null
);

