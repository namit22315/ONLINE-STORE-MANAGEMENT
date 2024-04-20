-- Cart is cleared once the order is placed
CREATE TRIGGER remove_from_cart AFTER INSERT ON `Order`
FOR EACH ROW
   DELETE FROM Cart WHERE username = NEW.username;

-- Funds raised of the particular NGO updated when the person donates some amount to the NGO
CREATE TRIGGER `update_funds_raised` AFTER INSERT ON `Billing`
FOR EACH ROW
  UPDATE `NGO` SET `funds_raised` = `funds_raised` + NEW.amount_donated WHERE `ngoID` = NEW.ngoID;
