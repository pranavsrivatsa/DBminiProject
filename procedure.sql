CREATE OR REPLACE FUNCTION get_day_stats()
RETURNS trigger AS $$
DECLARE
    ridePrice integer;
    existingRevenue integer;
    existingCount integer;
BEGIN
   ridePrice := r.price from ride r where r.id=new."rideId";
   existingRevenue := d.revenue from dayrev d where d."rideId"=new."rideId";
   existingcount := d.count from dayrev d where d."rideId"=new."rideId";
   update dayrev set day = new.time::timestamp::date where "rideId"=new."rideId";
   update dayrev set revenue = ridePrice+existingRevenue where "rideId"= new."rideId";
   update dayrev set count = existingCount+1 where "rideId"=new."rideId";
   return new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_dayrev AFTER INSERT ON customerrides
FOR EACH ROW EXECUTE PROCEDURE get_day_stats();
