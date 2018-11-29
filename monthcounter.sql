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
    WHEN ( extract (day from new.time ) = 28)
    EXECUTE PROCEDURE monthcountfill();
