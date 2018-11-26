CREATE OR REPLACE FUNCTION dayrevfill ()
RETURNS TRIGGER AS $$
DECLARE
    Carouselprice INTEGER := 0 ;
    Darkrideprice INTEGER := 0 ;
    Droptowerprice INTEGER := 0 ;
    Ferriswheelprice INTEGER := 0 ;
    Gyrotowerprice INTEGER := 0 ;
    Rollercoasterprice INTEGER := 0 ;
    Waterrideprice INTEGER := 0 ;
    SpiralSlideprice INTEGER := 0 ;
    Circusprice INTEGER := 0 ;
    Gravitronprice INTEGER := 0 ;
    Carouselprice1 INTEGER := 0 ;
    Darkrideprice1 INTEGER := 0 ;
    Droptowerprice1 INTEGER := 0 ;
    Ferriswheelprice1 INTEGER := 0 ;
    Gyrotowerprice1 INTEGER := 0 ;
    Rollercoasterprice1 INTEGER := 0 ;
    Waterrideprice1 INTEGER := 0 ;
    SpiralSlideprice1 INTEGER := 0 ;
    Circusprice1 INTEGER := 0 ;
    Gravitronprice1 INTEGER := 0 ;
BEGIN
    Carouselprice := count(*) from customerrides where "rideId" = 1;
    Carouselprice1 := r.price from ride r where id = 1;
    Carouselprice := Carouselprice * Carouselprice1;

    Darkrideprice := count(*) from customerrides where "rideId" = 2;
    Darkrideprice1 := r.price from ride r where id = 2;
    Darkrideprice := Darkrideprice * Darkrideprice1;

    Droptowerprice := count(*) from customerrides where "rideId" = 3;
    Droptowerprice1 := r.price from ride r where id = 3;
    Droptowerprice := Droptowerprice * Droptowerprice1;

    Ferriswheelprice := count(*) from customerrides where "rideId" = 4;
    Ferriswheelprice1 := r.price from ride r where id = 4;
    Ferriswheelprice := Ferriswheelprice * Ferriswheelprice1;

    Gyrotowerprice := count(*) from customerrides where "rideId" = 5;
    Gyrotowerprice1 := r.price from ride r where id = 5;
    Gyrotowerprice := Gyrotowerprice * Gyrotowerprice1;

    Rollercoasterprice := count(*) from customerrides where "rideId" = 6;
    Rollercoasterprice1 := r.price from ride r where id = 6;
    Rollercoasterprice := Rollercoasterprice * Rollercoasterprice1;

    Waterrideprice := count(*) from customerrides where "rideId" = 7;
    Waterrideprice1 := r.price from ride r where id = 7;
    Waterrideprice := Waterrideprice * Waterrideprice1;

    SpiralSlideprice := count(*) from customerrides where "rideId" = 8;
    SpiralSlideprice1 := r.price from ride r where id = 8;
    SpiralSlideprice := SpiralSlideprice * SpiralSlideprice1;

    Circusprice := count(*) from customerrides where "rideId" = 9;
    Circusprice1 := r.price from ride r where id = 9;
    Circusprice := Circusprice * Circusprice1;

    Gravitronprice := count(*) from customerrides where "rideId" = 10;
    Gravitronprice1 := r.price from ride r where id = 10;
    Gravitronprice := Gravitronprice * Gravitronprice1;

    insert into dayrev("time", "Carousel", "Darkride", "Droptower", "Ferriswheel", "Gyrotower", "Rollercoaster", "Waterride", "SpiralSlide", "Circus", "Gravitron") values (new.time, Carouselprice, Darkrideprice, Droptowerprice, Ferriswheelprice, Gyrotowerprice, Rollercoasterprice, Waterrideprice, SpiralSlideprice, Circusprice, Gravitronprice);
    delete from customerrides;
    alter sequence customerrides_id_seq restart with 1;
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_dayrev
    AFTER INSERT ON customerrides
    FOR EACH ROW
    WHEN ( extract (hour from new.time ) = 18)
    EXECUTE PROCEDURE dayrevfill();
