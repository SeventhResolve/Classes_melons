"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """ Docstring here """

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        # self.tax = 0.08

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas melons":
            base_price = 7.5

        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.tax = 0.08
        self.order_type = "domestic"
        return super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.tax = 0.17
        self.country_code = country_code
        self.order_type = "international"
        
        return super(InternationalMelonOrder, self).__init__(species, qty)

   
    def get_total(self):
        """Calculate price."""

        flat_fee = 3    

        total =  super(InternationalMelonOrder, self).get_total()

        if self.qty < 10: 
            total += flat_fee

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code