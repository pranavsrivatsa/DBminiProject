CREATE OR REPLACE FUNCTION get_day_stats()
RETURNS trigger AS $$
DECLARE
    rideName text;
    ridePrice integer;
    existingPrice integer;
    query text;
BEGIN            
   rideName := r.name from ride r where r.id=new."rideId";
   ridePrice := r.price from ride r where r.id=new."rideId";
   EXECUTE format('INSERT INTO dayrev(time,%I) VALUES(%I,%L)',rideName,new.time::timestamp::date,ridePrice);
   return new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_dayrev AFTER INSERT ON customerrides
FOR EACH ROW EXECUTE PROCEDURE get_day_stats();
