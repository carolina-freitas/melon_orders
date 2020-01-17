"""Classes for melon orders."""
import random   
from datetime import datetime


class AbstractMelonOrder:

    shipped = False
    #base_price = random.randrange(5, 10)

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        base_price = 5

        now = datetime.now()
        weekday = now.weekday()
        hour = now.hour

        if weekday < 5 and 8 < time < 11:
            return base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()


        if self.species == 'Christmas melon':
            base_price = 5 * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """An US government melon order """
    order_type = "government"
    tax = 0
    passed_inspection = False

    def mark_inspection(self):
        """Updates whether or not the melon has passed inspection"""
        self.passed_inspection = True


# order0 = InternationalMelonOrder("watermelon", 6, "AUS")
# print(order0.get_total())   
print(datetime.today().weekday())

print(now)
