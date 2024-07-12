CREATE TABLE IF NOT EXISTS log_sessao (
	id SERIAL PRIMARY KEY,
	data_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	tentativas INT NOT NULL,
	id_usuario INT,
	FOREIGN KEY (id_usuario) REFERENCES cadastro_usuario(id)
	);