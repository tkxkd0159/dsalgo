DROP TABLE IF EXISTS airports;

CREATE TABLE airports (
    idx int NOT NULL AUTO_INCREMENT,
    iata varchar(255),
    city varchar(255),
    country varchar(255),
    PRIMARY KEY (idx)
);


INSERT INTO airports (iata, city, country)
VALUES
    ("ORD", "Chicago", "United States"),
    ("CDG", "Paris", "France"),
    ("LHR", "London", "United Kingdom"),
    ("DME", "Moscow", "Russia"),
    ("SVO", "Moscow", "Russia");