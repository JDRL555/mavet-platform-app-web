DROP DATABASE IF EXISTS mavet_db;
CREATE DATABASE IF NOT EXISTS mavet_db;

USE mavet_db;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users( 
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name_user TEXT NOT NULL,
  last_name_user TEXT NOT NULL,
  email_user VARCHAR(100) NOT NULL,
  phone_user TINYINT(12) NOT NULL,
  specialty_user SET("Estudiante", "Profesor") NOT NULL,
  type_user SET("Estandar", "Administrador") NOT NULL,
  avatar_user VARCHAR(100) DEFAULT '',
  username_user VARCHAR(50) NOT NULL,
  password_user VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_DATE,

  PRIMARY KEY(id),
  CONSTRAINT UNIQUE(email_user),
  CONSTRAINT UNIQUE(username_user)
);

DROP TABLE IF EXISTS works_art;
CREATE TABLE IF NOT EXISTS works_art(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_user INT UNSIGNED NOT NULL,
  title_work TEXT NOT NULL,
  img_work VARCHAR(100) NOT NULL,
  description_work TEXT NOT NULL,
  type_work SET("Pintura", "Dibujo", "Fotografia") NOT NULL,
  likes_work INT DEFAULT 0,
  created_at DATETIME DEFAULT CURRENT_DATE,

  PRIMARY KEY(id),
  FOREIGN KEY(id_user) REFERENCES users(id)
);

DROP TABLE IF EXISTS comments;
CREATE TABLE IF NOT EXISTS comments(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_user INT UNSIGNED NOT NULL,
  id_work INT UNSIGNED NOT NULL,
  content_comment TEXT NOT NULL,
  likes_comment INT DEFAULT 0,
  created_at DATETIME DEFAULT CURRENT_DATE,

  PRIMARY KEY(id),
  FOREIGN KEY(id_user) REFERENCES users(id),
  FOREIGN KEY(id_work) REFERENCES works_art(id)
);

DROP TABLE IF EXISTS events;
CREATE TABLE IF NOT EXISTS events(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  img_event TEXT NOT NULL,
  title_event TEXT NOT NULL,
  description_event TEXT NOT NULL,
  likes_event INT DEFAULT 0,
  date_event DATETIME DEFAULT CURRENT_DATE,

  PRIMARY KEY(id)
);

DROP TABLE IF EXISTS courses;
CREATE TABLE IF NOT EXISTS courses(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_teacher INT UNSIGNED NOT NULL,
  title_course TEXT NOT NULL,
  img_course TEXT NOT NULL,
  description_course TEXT NOT NULL,
  price_course FLOAT DEFAULT 0,
  date_course DATETIME DEFAULT CURRENT_DATE,

  PRIMARY KEY(id),
  FOREIGN KEY(id_teacher) REFERENCES users(id)
);
