create table Movies (
    ID serial primary key,
    TITLE varchar(50),
    THUMBNAIL_TRENDING varchar(250),
    THUMBNAIL_REGULAR varchar(250),
    RELEASE_YEAR varchar(5),
    CATEGORY varchar(50),
    RATING varchar(10),
    IS_TRENDING bool_enum
)