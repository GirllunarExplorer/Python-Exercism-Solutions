__author__ = 'tracyrohlin'


class New_Allergies(object):

    def __init__(self, score):
        super(New_Allergies, self).__init__()
        self.allergens = ["eggs",
               "peanuts",
               "shellfish",
               "strawberries",
               "tomatoes",
               "chocolate",
               "pollen",
               "cats"]

        self.list = [allergen for i, allergen
                     in enumerate(self.allergens)
                     if (score >> i) % 2]

    def is_allergic_to(self, allergen):
        return allergen in self.list