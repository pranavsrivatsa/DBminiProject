CREATE OR REPLACE FUNCTION daycountfill ()
RETURNS TRIGGER AS $$
DECLARE
    Carouselcount INTEGER := 0 ;
    Darkridecount INTEGER := 0 ;
    Droptowercount INTEGER := 0 ;
    Ferriswheelcount INTEGER := 0 ;
    Gyrotowercount INTEGER := 0 ;
    Rollercoastercount INTEGER := 0 ;
    Waterridecount INTEGER := 0 ;
    SpiralSlidecount INTEGER := 0 ;
    Circuscount INTEGER := 0 ;
    Gravitroncount INTEGER := 0 ;

BEGIN
    Carouselcount := count(*) from customerrides where "rideId" = 1;
    Darkridecount := count(*) from customerrides where "rideId" = 2;
    Droptowercount := count(*) from customerrides where "rideId" = 3;
    Ferriswheelcount := count(*) from customerrides where "rideId" = 4;
    Gyrotowercount := count(*) from customerrides where "rideId" = 5;
    Rollercoastercount := count(*) from customerrides where "rideId" = 6;
    Waterridecount := count(*) from customerrides where "rideId" = 7;
    SpiralSlidecount := count(*) from customerrides where "rideId" = 8;
    Circuscount := count(*) from customerrides where "rideId" = 9;
    Gravitroncount := count(*) from customerrides where "rideId" = 10;

    insert into daycount("time", "Carousel", "Darkride", "Droptower", "Ferriswheel", "Gyrotower", "Rollercoaster", "Waterride", "SpiralSlide", "Circus", "Gravitron") values (new.time, Carouselcount, Darkridecount, Droptowercount, Ferriswheelcount, Gyrotowercount, Rollercoastercount, Waterridecount, SpiralSlidecount, Circuscount, Gravitroncount);
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_daycount
    AFTER INSERT ON customerrides
    FOR EACH ROW
    WHEN ( extract (hour from new.time ) = 18)
    EXECUTE PROCEDURE daycountfill();

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

CREATE OR REPLACE FUNCTION daydcfill ()
RETURNS TRIGGER AS $$
DECLARE
    totalcount INTEGER := 0;
    Carouselcount INTEGER := 0 ;
    Darkridecount INTEGER := 0 ;
    Droptowercount INTEGER := 0 ;
    Ferriswheelcount INTEGER := 0 ;
    Gyrotowercount INTEGER := 0 ;
    Rollercoastercount INTEGER := 0 ;
    Waterridecount INTEGER := 0 ;
    SpiralSlidecount INTEGER := 0 ;
    Circuscount INTEGER := 0 ;
    Gravitroncount INTEGER := 0 ;

BEGIN
    Carouselcount := new."Carousel";
    Darkridecount := new."Darkride";
    Droptowercount := new."Droptower";
    Ferriswheelcount := new."Ferriswheel";
    Gyrotowercount := new."Gyrotower";
    Rollercoastercount := new."Rollercoaster";
    Waterridecount := new."Waterride";
    SpiralSlidecount := new."SpiralSlide";
    Circuscount := new."Circus";
    Gravitroncount := new."Gravitron";
    totalcount := Carouselcount + Darkridecount + Droptowercount + Ferriswheelcount + Gyrotowercount + Rollercoastercount + Waterridecount + SpiralSlidecount + Circuscount + Gravitroncount;
    insert into daydetails("time", "day_rev", "day_count") values (new.time, 0, totalcount);
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_daydccount
    AFTER INSERT ON daycount
    FOR EACH ROW
    EXECUTE PROCEDURE daydcfill();

CREATE OR REPLACE FUNCTION daydrfill ()
RETURNS TRIGGER AS $$
DECLARE
    totalprice INTEGER := 0;
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

BEGIN
    Carouselprice := new."Carousel";
    Darkrideprice := new."Darkride";
    Droptowerprice := new."Droptower";
    Ferriswheelprice := new."Ferriswheel";
    Gyrotowerprice := new."Gyrotower";
    Rollercoasterprice := new."Rollercoaster";
    Waterrideprice:= new."Waterride";
    SpiralSlideprice := new."SpiralSlide";
    Circusprice := new."Circus";
    Gravitronprice := new."Gravitron";
    totalprice := Carouselprice + Darkrideprice + Droptowerprice + Ferriswheelprice + Gyrotowerprice + Rollercoasterprice + Waterrideprice + SpiralSlideprice + Circusprice + Gravitronprice;
    update daydetails set day_rev = totalprice where id = new.id;
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_daydrcount
    AFTER INSERT ON dayrev
    FOR EACH ROW
    EXECUTE PROCEDURE daydrfill();

CREATE OR REPLACE FUNCTION monthcountfill ()
RETURNS TRIGGER AS $$
DECLARE
    Carouselcount INTEGER := 0 ;
    Darkridecount INTEGER := 0 ;
    Droptowercount INTEGER := 0 ;
    Ferriswheelcount INTEGER := 0 ;
    Gyrotowercount INTEGER := 0 ;
    Rollercoastercount INTEGER := 0 ;
    Waterridecount INTEGER := 0 ;
    SpiralSlidecount INTEGER := 0 ;
    Circuscount INTEGER := 0 ;
    Gravitroncount INTEGER := 0 ;

BEGIN
    Carouselcount := sum("Carousel") from daycount;
    Darkridecount := sum("Darkride") from daycount;
    Droptowercount := sum("Droptower") from daycount;
    Ferriswheelcount := sum("Ferriswheel") from daycount;
    Gyrotowercount := sum("Gyrotower") from daycount;
    Rollercoastercount := sum("Rollercoaster") from daycount;
    Waterridecount := sum("Waterride") from daycount;
    SpiralSlidecount := sum("SpiralSlide") from daycount;
    Circuscount := sum("Circus") from daycount;
    Gravitroncount := sum("Gravitron") from daycount;

    insert into monthcount("time", "Carousel", "Darkride", "Droptower", "Ferriswheel", "Gyrotower", "Rollercoaster", "Waterride", "SpiralSlide", "Circus", "Gravitron") values (new.time, Carouselcount, Darkridecount, Droptowercount, Ferriswheelcount, Gyrotowercount, Rollercoastercount, Waterridecount, SpiralSlidecount, Circuscount, Gravitroncount);
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_monthcount
    AFTER INSERT ON daycount
    FOR EACH ROW
    WHEN ( extract (day from new.time ) = 27)
    EXECUTE PROCEDURE monthcountfill();

CREATE OR REPLACE FUNCTION monthrevfill ()
RETURNS TRIGGER AS $$
DECLARE
    Carouselcount INTEGER := 0 ;
    Darkridecount INTEGER := 0 ;
    Droptowercount INTEGER := 0 ;
    Ferriswheelcount INTEGER := 0 ;
    Gyrotowercount INTEGER := 0 ;
    Rollercoastercount INTEGER := 0 ;
    Waterridecount INTEGER := 0 ;
    SpiralSlidecount INTEGER := 0 ;
    Circuscount INTEGER := 0 ;
    Gravitroncount INTEGER := 0 ;

BEGIN
    Carouselcount := sum("Carousel") from dayrev;
    Darkridecount := sum("Darkride") from dayrev;
    Droptowercount := sum("Droptower") from dayrev;
    Ferriswheelcount := sum("Ferriswheel") from dayrev;
    Gyrotowercount := sum("Gyrotower") from dayrev;
    Rollercoastercount := sum("Rollercoaster") from dayrev;
    Waterridecount := sum("Waterride") from dayrev;
    SpiralSlidecount := sum("SpiralSlide") from dayrev;
    Circuscount := sum("Circus") from dayrev;
    Gravitroncount := sum("Gravitron") from dayrev;

    insert into monthrev("time", "Carousel", "Darkride", "Droptower", "Ferriswheel", "Gyrotower", "Rollercoaster", "Waterride", "SpiralSlide", "Circus", "Gravitron") values (new.time, Carouselcount, Darkridecount, Droptowercount, Ferriswheelcount, Gyrotowercount, Rollercoastercount, Waterridecount, SpiralSlidecount, Circuscount, Gravitroncount);
    delete from dayrev;
    delete from daydetails;
    delete from daycount;
    alter sequence dayrev_id_seq restart with 1;
    alter sequence daydetails_id_seq restart with 1;
    alter sequence daycount_id_seq restart with 1;
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_monthrev
    AFTER INSERT ON dayrev
    FOR EACH ROW
    WHEN ( extract (day from new.time ) = 27)
    EXECUTE PROCEDURE monthrevfill();

CREATE OR REPLACE FUNCTION monthmcfill ()
RETURNS TRIGGER AS $$
DECLARE
    totalcount INTEGER := 0;
    Carouselcount INTEGER := 0 ;
    Darkridecount INTEGER := 0 ;
    Droptowercount INTEGER := 0 ;
    Ferriswheelcount INTEGER := 0 ;
    Gyrotowercount INTEGER := 0 ;
    Rollercoastercount INTEGER := 0 ;
    Waterridecount INTEGER := 0 ;
    SpiralSlidecount INTEGER := 0 ;
    Circuscount INTEGER := 0 ;
    Gravitroncount INTEGER := 0 ;

BEGIN
    Carouselcount := new."Carousel";
    Darkridecount := new."Darkride";
    Droptowercount := new."Droptower";
    Ferriswheelcount := new."Ferriswheel";
    Gyrotowercount := new."Gyrotower";
    Rollercoastercount := new."Rollercoaster";
    Waterridecount := new."Waterride";
    SpiralSlidecount := new."SpiralSlide";
    Circuscount := new."Circus";
    Gravitroncount := new."Gravitron";
    totalcount := Carouselcount + Darkridecount + Droptowercount + Ferriswheelcount + Gyrotowercount + Rollercoastercount + Waterridecount + SpiralSlidecount + Circuscount + Gravitroncount;
    insert into monthdetails("time", "month_rev", "month_count") values (new.time, 0, totalcount);
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_monthmccount
    AFTER INSERT ON monthcount
    FOR EACH ROW
    EXECUTE PROCEDURE monthmcfill();

CREATE OR REPLACE FUNCTION monthmrfill ()
RETURNS TRIGGER AS $$
DECLARE
    totalprice INTEGER := 0;
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

BEGIN
    Carouselprice := new."Carousel";
    Darkrideprice := new."Darkride";
    Droptowerprice := new."Droptower";
    Ferriswheelprice := new."Ferriswheel";
    Gyrotowerprice := new."Gyrotower";
    Rollercoasterprice := new."Rollercoaster";
    Waterrideprice:= new."Waterride";
    SpiralSlideprice := new."SpiralSlide";
    Circusprice := new."Circus";
    Gravitronprice := new."Gravitron";
    totalprice := Carouselprice + Darkrideprice + Droptowerprice + Ferriswheelprice + Gyrotowerprice + Rollercoasterprice + Waterrideprice + SpiralSlideprice + Circusprice + Gravitronprice;
    update monthdetails set month_rev = totalprice where id = new.id;
    RETURN new;
END;$$
LANGUAGE plpgsql;

CREATE TRIGGER update_monthmrcount
    AFTER INSERT ON monthrev
    FOR EACH ROW
    EXECUTE PROCEDURE monthmrfill();