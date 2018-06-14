# Use python cucumber behaviour driven development test such as raddish
# To think through

# example:
# pip install radish-bdd
#
# see http://radish.readthedocs.io/en/latest/quickstart.html#writing-the-first-feature-file

# Things you want game to do:
# - take user input of rock, paper or scissors
# - randomly generate computer turn
# - determine winner correctly
# - output score
# - keep playing until user asks it to stop
# These are features

# see example at chttps://github.com/dunossauro/radish-bdd-examples


Feature: Take only valid user input that represent rock paper scissors
  In order to make sure the game
  only takes valid inputs I have the following
  test scenarios:

  Scenario: Only allow valid input to game
    Given I have input 2
    When I check them
    Then I expect to play then asked, Would you like to play again
