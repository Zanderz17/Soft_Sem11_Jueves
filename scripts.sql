CREATE TABLE ShoppingCart (
  ItemID serial PRIMARY KEY,
  Name VARCHAR(255),
  Quantity INT
);

SELECT * FROM ShoppingCart WHERE ItemID = 1;