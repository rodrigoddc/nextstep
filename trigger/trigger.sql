CREATE OR REPLACE FUNCTION person_audit_trigger()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS $audit_trigger$
BEGIN
	IF new.cpf == IS NULL THEN
		INSERT INTO person_audit (person_audit.person_id_id,
								  person_audit.cpf_old, 
								  person_audit.last_update, 
								  person_audit.type)
		VALUES (old.id, old.cpf, old.last_update, old.type_id);
	RETURN NEW;
	ELSE 
		INSERT INTO person_audit (person_audit.person_id_id,
								  person_audit.cpf_new, 
								  person_audit.cpf_old, 
								  person_audit.last_update, 
								  person_audit.type)
		VALUES (old.id, new.cpf, old.cpf, old.last_update, old.type_id);
	END IF;
	RETURN NEW;
END;
$audit_trigger$


CREATE TRIGGER person_trigger
  AFTER INSERT OR UPDATE
  	ON person
  FOR EACH ROW
  EXECUTE PROCEDURE person_audit_trigger();