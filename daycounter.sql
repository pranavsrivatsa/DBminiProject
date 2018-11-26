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
