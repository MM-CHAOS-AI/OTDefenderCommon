select * from oui_registry t ;

select * from packets p ;

select * from capture_interfaces ci ;

select * from capture_sessions_files csf ;


delete from packets where interface_id is null;
delete from capture_interfaces where interface_id_in_file =0;
delete from capture_sessions_files where id=1;

select * from capture_interfaces ci ;