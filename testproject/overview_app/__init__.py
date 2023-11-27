from otree.api import *


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    # Constants can be any python variable type
    # string
    name_in_url = 'workshop_overview_app'
    # empty variable
    players_per_group = None
    # integer
    num_rounds = 1
    # boolean
    randomise_question_order = True
    # list
    question_list = ["Question 1", "Question 2"]
    # oTree experimental currency
    base_payment = cu(1)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Use BooleanField for binary variables
    in_treatment_group = models.BooleanField()
    # Use StringField for short texts
    player_id = models.StringField()
    # Use LongStringField for longer text
    feedback = models.LongStringField()
    # Use IntegerField for integers Integer
    number_option_chosen = models.IntegerField()
    # use FloatField for all non Integer Numbers
    asset_price = models.FloatField()
    # use CurrencyField for players earnings
    current_earnings = models.CurrencyField()


# FUNCTIONS
# PAGES
class MyPage(Page):
    form_model = 'player'
    # names must correspond to fields in models.py
    form_fields = ['number_option_chosen',
                   'feedback']
    # decide if this page is displayed
    @staticmethod
    def is_displayed(player: Player):
        # display the page in the first round
        if player.round_number == 1:
            return True
        else:
            return False
    @staticmethod        
    def before_next_page(player: Player,
                         timeout_happened):
        # save something in the database
        player.payoff = 2
    @staticmethod
    def vars_for_template(player: Player):
        # return variables to be used in template
        return {
            'completion_code': "JH/$KJJ",
        }


class Results(Page):
    pass


# the order in which pages are displayed
page_sequence = [MyPage, Results]
