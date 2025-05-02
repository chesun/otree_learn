from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'real_effort_numbers'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    PAYMENT_PER_ROUND = cu(1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField()
    sum_of_numbers = models.IntegerField()


# PAGES
class AddNumbers(Page):
    form_model = "player"
    form_fields = ["number_entered"]


class Results(Page):
    pass


page_sequence = [MyPage, Results]
