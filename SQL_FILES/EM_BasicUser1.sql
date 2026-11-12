-- Dummy data

-- 1. Insert dummy records into ot_enterprise
INSERT INTO otdefem.ot_enterprise
(entity_name, location, is_active, version, updated_by, updated_at) VALUES
('Global Energy Grid Corp', 'INDIA', 1, 1, 'MM', NOW());

-- 2. Insert dummy records into ot_substation (referencing enterprises)
INSERT INTO otdefem.ot_substations
(enterprise_id, substation_name, scd_file_name, scd_file_hash, commission_date, is_active, version, updated_by, updated_at)
VALUES
(1, 'Alpha Transmission Substation', 'SUB-ALPHA-400', '400kV', NOW(), 1, 1, 'MM', NOW()),
(1, 'Beta Distribution Substation', 'SUB-BETA-110', '110kV', NOW(), 1, 1, 'MM', NOW()),
(1, 'Gamma Renewable Substation', 'SUB-GAMMA-220', '220kV', NOW(), 1, 1, 'MM', NOW());



SELECT * FROM ot_enterprise oe ;

select * from ot_substations os;

select * from ids_sensors is2 ;

select * from ot_assets oa ;

select * from traffic_baselines tb ;
