-- DROP TABLE IF EXISTS `capture_sessions_files`;

CREATE TABLE capture_sessions_files (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	filename VARCHAR(255) NOT NULL, 
	file_size_bytes BIGINT NOT NULL, 
	sha256_hash VARCHAR(64) NOT NULL, 
	shb_comment TEXT, 
	uploaded_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
)


;


-- DROP TABLE IF EXISTS `ot_enterprises`;

CREATE TABLE ot_enterprises (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	entity_name VARCHAR(255) NOT NULL, 
	location VARCHAR(255) NOT NULL, 
	updated_by VARCHAR(100) NOT NULL, 
	timestamp DATETIME NOT NULL DEFAULT (now()), 
	PRIMARY KEY (id)
)


;


-- DROP TABLE IF EXISTS `oui_registry`;

CREATE TABLE oui_registry (
	oui VARCHAR(50) NOT NULL, 
	manufacturer VARCHAR(255) NOT NULL, 
	registry VARCHAR(100), 
	short_name VARCHAR(100), 
	device_type VARCHAR(100), 
	registered_date VARCHAR(50), 
	address TEXT, 
	sources TEXT, 
	registrant_raw TEXT, 
	status VARCHAR(50), 
	deregistered_date VARCHAR(50), 
	registrant_history TEXT, 
	last_updated VARCHAR(50) DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (oui)
)


;


-- DROP TABLE IF EXISTS `users`;

CREATE TABLE users (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	username VARCHAR(100) NOT NULL, 
	email VARCHAR(200) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
)


;


-- DROP TABLE IF EXISTS `capture_interfaces`;

CREATE TABLE capture_interfaces (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	session_id INTEGER NOT NULL, 
	interface_id_in_file INTEGER NOT NULL, 
	name VARCHAR(100), 
	link_type VARCHAR(50), 
	os_info VARCHAR(255), 
	filter_string VARCHAR(255), 
	mac_address VARCHAR(17), 
	PRIMARY KEY (id), 
	FOREIGN KEY(session_id) REFERENCES capture_sessions_files (id) ON DELETE RESTRICT
)


;


-- DROP TABLE IF EXISTS `ot_sensors`;

CREATE TABLE ot_sensors (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	enterprise_id INTEGER NOT NULL, 
	sensor_name VARCHAR(255) NOT NULL, 
	location VARCHAR(255) NOT NULL, 
	mac VARCHAR(20) NOT NULL, 
	ip VARCHAR(45) NOT NULL, 
	sensor_tag VARCHAR(200) NOT NULL, 
	installation_date DATETIME NOT NULL, 
	updated_by VARCHAR(100) NOT NULL, 
	timestamp DATETIME NOT NULL DEFAULT (now()), 
	PRIMARY KEY (id), 
	FOREIGN KEY(enterprise_id) REFERENCES ot_enterprises (id) ON DELETE RESTRICT
)


;


-- DROP TABLE IF EXISTS `ot_assets`;

CREATE TABLE ot_assets (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	sensor_id INTEGER NOT NULL, 
	asset_name VARCHAR(255) NOT NULL, 
	asset_company VARCHAR(255), 
	asset_description TEXT, 
	asset_type VARCHAR(255) NOT NULL, 
	mac VARCHAR(20) NOT NULL, 
	ip VARCHAR(45) NOT NULL, 
	ports VARCHAR(255), 
	criticality VARCHAR(50) NOT NULL, 
	vulnerability_score INTEGER NOT NULL, 
	level VARCHAR(50) NOT NULL, 
	registration_date DATETIME NOT NULL, 
	location VARCHAR(255) NOT NULL, 
	protocol VARCHAR(50), 
	software_version VARCHAR(100), 
	updated_by VARCHAR(100) NOT NULL, 
	timestamp DATETIME NOT NULL DEFAULT (now()), 
	PRIMARY KEY (id), 
	FOREIGN KEY(sensor_id) REFERENCES ot_sensors (id) ON DELETE RESTRICT
)


;


-- DROP TABLE IF EXISTS `ot_sensor_health`;

CREATE TABLE ot_sensor_health (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	sensor_id INTEGER NOT NULL, 
	health_status VARCHAR(50) NOT NULL, 
	cpu FLOAT NOT NULL, 
	memory FLOAT NOT NULL, 
	uptime BIGINT NOT NULL, 
	timestamp DATETIME NOT NULL DEFAULT (now()), 
	PRIMARY KEY (id), 
	FOREIGN KEY(sensor_id) REFERENCES ot_sensors (id) ON DELETE RESTRICT
)


;


-- DROP TABLE IF EXISTS `packets`;

CREATE TABLE packets (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	session_id INTEGER NOT NULL, 
	interface_id INTEGER, 
	packet_index BIGINT NOT NULL, 
	timestamp DATETIME NOT NULL, 
	captured_length INTEGER NOT NULL, 
	original_length INTEGER NOT NULL, 
	src_mac VARCHAR(20), 
	dst_mac VARCHAR(20), 
	src_ip VARCHAR(45), 
	dst_ip VARCHAR(45), 
	protocol VARCHAR(30), 
	src_port INTEGER, 
	dst_port INTEGER, 
	payload BLOB, 
	PRIMARY KEY (id), 
	FOREIGN KEY(session_id) REFERENCES capture_sessions_files (id) ON DELETE RESTRICT, 
	FOREIGN KEY(interface_id) REFERENCES capture_interfaces (id) ON DELETE SET NULL
)


;


-- DROP TABLE IF EXISTS `live_packets`;

CREATE TABLE live_packets (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	asset_id INTEGER NOT NULL, 
	in_sensor_id INTEGER NOT NULL, 
	interface_id INTEGER, 
	interface_name VARCHAR(100), 
	packet_index BIGINT NOT NULL, 
	timestamp DATETIME NOT NULL, 
	captured_length INTEGER NOT NULL, 
	original_length INTEGER NOT NULL, 
	is_gap BOOL NOT NULL, 
	gap_size INTEGER, 
	packet_comment TEXT, 
	src_mac VARCHAR(20), 
	dst_mac VARCHAR(20), 
	src_ip VARCHAR(45), 
	dst_ip VARCHAR(45), 
	protocol VARCHAR(30), 
	src_port INTEGER, 
	dst_port INTEGER, 
	payload BLOB, 
	PRIMARY KEY (id), 
	FOREIGN KEY(asset_id) REFERENCES ot_assets (id) ON DELETE RESTRICT
)


;


-- DROP TABLE IF EXISTS `ot_asset_health`;

CREATE TABLE ot_asset_health (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	asset_id INTEGER NOT NULL, 
	health_status VARCHAR(50) NOT NULL, 
	last_packet_timestamp DATETIME NOT NULL DEFAULT (now()), 
	timestamp DATETIME NOT NULL DEFAULT (now()), 
	PRIMARY KEY (id), 
	FOREIGN KEY(asset_id) REFERENCES ot_assets (id) ON DELETE RESTRICT
)


;
