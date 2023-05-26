DROP DATABASE IF EXISTS mavet_app;
CREATE DATABASE IF NOT EXISTS mavet_app;

USE mavet_app;

DROP TABLE IF EXISTS registro;
CREATE TABLE IF NOT EXISTS registro( 

    -- Columnas
    id_usuario INT UNSIGNED AUTO_INCREMENT,
    nombres_usuario TEXT NOT NULL,
    apellidos_usuario TEXT NOT NULL,
    correo_usuario VARCHAR(80) NOT NULL,
    pais_usuario TEXT NOT NULL,
    especialidad_usuario TEXT NOT NULL,
    nombre_de_usuario VARCHAR(30) NOT NULL,
    contraseña_usuario VARCHAR(100) NOT NULL,
    confirmar_clave VARCHAR(100) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),

    -- Llaves
    PRIMARY KEY(id_usuario),
    CONSTRAINT UNIQUE(correo_usuario)

);


DROP TABLE IF EXISTS inicio_sesion;
CREATE TABLE IF NOT EXISTS inicio_sesion(
	
    -- Columnas
    id_sesion INT UNSIGNED AUTO_INCREMENT,
	correo_id VARCHAR(80) NOT NULL,
    contraseña_id VARCHAR(100) NOT NULL,
	fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
	
    -- Llaves
    PRIMARY KEY(id_sesion),
    FOREIGN KEY(correo_id) REFERENCES registro(id_usuario),
    FOREIGN KEY(contraseña_id) REFERENCES registro(id_usuario)

);


DROP TABLE IF EXISTS publicaciones;
CREATE TABLE IF NOT EXISTS publicaciones(

    -- Columnas
    id_publicacion INT UNSIGNED AUTO_INCREMENT,
    -- tipo_de_publicacion TEXT NOT NULL,
    titulo_publicacion TEXT NOT NULL,
    -- imagen_publicacion
    descripcion_publicacion TEXT NOT NULL,
    reacciones_publicacion INT UNSIGNED AUTO_INCREMENT,
    comentarios_publicacion TEXT NOT NULL,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),

    -- Llaves
    PRIMARY KEY(id_publicacion)

);


DROP TABLE IF EXISTS eventos;
CREATE TABLE IF NOT EXISTS eventos(

    -- Columnas
    id_evento INT UNSIGNED AUTO_INCREMENT,
    titulo_evento TEXT NOT NULL,
    -- imagen_evento
    descripcion_eventos TEXT NOT NULL,
    fecha_eventos TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),

    -- Llaves
    PRIMARY KEY(id_evento)

);


DROP TABLE IF EXISTS cursos;
CREATE TABLE IF NOT EXISTS cursos(

    -- Columnas
    id_cursos INT UNSIGNED AUTO_INCREMENT,
    titulo_cursos TEXT NOT NULL,
    -- imagen_cursos
    descripcion_cursos TEXT NOT NULL,
    fecha_cursos TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),

    -- Llaves
    PRIMARY KEY(id_cursos)

);
