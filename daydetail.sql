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

CREATE TRIGGER update_daycount
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

CREATE TRIGGER update_daycount
    AFTER INSERT ON dayrev
    FOR EACH ROW
    EXECUTE PROCEDURE daydrfill();
