drop database admintrading;
create database admintrading;
use admintrading;
create table activo(
id int auto_increment primary key,
nombre_activo varchar(100)
);
create table usuario(
id int auto_increment primary key,
usuario varchar(100),
contraseña varchar(100),
inicioCuenta decimal(9,2),
totalActual decimal(9,2),
correo varchar(100)
);

create table operaciones(
id int auto_increment primary key,
id_usuario int,
id_activo int,
foreign key (id_usuario) references usuario (id),
foreign key (id_activo) references activo (id),
valor decimal(9,2),
valorPorcentaje decimal(9,2),
fecha date,
id_operacion int unique
);