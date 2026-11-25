-- DBO USER
CREATE USER 'otdef_dbo'@'%' IDENTIFIED BY 'otdef@dbo1';

-- Grant privileges to the user (e.g., full access to a specific database)
GRANT ALL PRIVILEGES ON otdefdb.* TO 'otdef_dbo'@'%';


-- APP USER
CREATE USER 'otdef_user1'@'%' IDENTIFIED BY 'otdef@user1';
-- If setting permissions for the user for the first time:
GRANT SELECT, INSERT, UPDATE,DELETE ON otdefdb.* TO 'otdef_user1'@'%';

-- Refresh the privileges
FLUSH PRIVILEGES;