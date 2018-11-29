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
    Carouselcount := sum(Carousel) from dayrev;
    Darkridecount := sum(Darkride) from dayrev;
    Droptowercount := sum(Droptower) from dayrev;
    Ferriswheelcount := sum(Ferriswheel) from dayrev;
    Gyrotowercount := sum(Gyrotower) from dayrev;
    Rollercoastercount := sum(Rollercoaster) from dayrev;
    Waterridecount := sum(Waterride) from dayrev;
    SpiralSlidecount := sum(SpiralSlide) from dayrev;
    Circuscount := sum(Circus) from dayrev;
    Gravitroncount := sum(Gravitron) from dayrev;

    insert into monthrev("time", "Carousel", "Darkride", "Droptower", "Ferriswheel", "Gyrotower", "Rollercoaster", "Waterride", "SpiralSlide", "Circus", "Gravitron") values (new.time, Carouselcount, Darkridecount, Droptowercount, Ferriswheelcount, Gyrotowercount, Rollercoastercount, Waterridecount, SpiralSlidecount, Circuscount, Gravitroncount);
    delete from dayrev;
    delete from daydetials;
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
    WHEN ( extract (day from new.time ) = 28)
    EXECUTE PROCEDURE monthrevfill();
