CREATE TABLE ShoppingCart (
  ItemID serial PRIMARY KEY,
  Name VARCHAR(255),
  Quantity INT
);
INSERT INTO ShoppingCart (Name, Quantity) VALUES ('LEGO', 3);

SELECT * FROM ShoppingCart WHERE ItemID = 1;