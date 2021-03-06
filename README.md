# How To Code Whatever You Want In python

How to learn to take a problem, find a solution and then code it.  This is for Danielka, Doral and Betka.

## The Steps:
* Google is your friend, google everything, being as specific as possible.
* NEVER, NEVER EVER copy and paste code ALWAYS type it out so your BRAIN and FINGERS remember it.
* There is "NO MAGIC" computers do what and only what you instruct them to do.
* Learn how to write basic scripts in Python from an interactive learning site such as:
  - codeacademy https://www.codecademy.com/learn/learn-python
  - learnpython https://www.learnpython.org/
  - codecombat https://codecombat.com/play
  - And to practice your new coding knowledge - codewars https://www.codewars.com/dashboard
* Now three step to programming a solution (Model, Pattern, Tests):
  - Model - Think how you are going to store and model the stuff you are working on.  For example constants in rockPaperScissors:
    - choices rock, paper and scissors stored as numbers in variables
    - names of choices modelled / stored in a dictionary (hash/map)
    - rules of winning combinations modelled / stored in dictionary
    - Once choice of model guessed at then program is about manipulating the model to play game.
  - Pattern - The solution should be made of:
    - a pattern made of functions / methods
    - that may have an input;  
    - some behaviour;
    - a state(return value) or output.
    - The patterns often have to be guessed (googled) at using trial and error or are known from experience.
  - Tests - the important bit.  You don't need a flash of inspiration to code solution you just have to build some scaffolding and this will guide you through writing the code to get the desired result.
    - First the big scaffolding to focus your mind on the problem - this is called BDD (Behaviour Driven Development).
    - Second the smaller scaffolding to focus your mind on coding one step / function / method / unit at a time - this is called TDD (Test Driven Development).
* BDD is working from the outside of the solution towards the inside.  You don't focus on how to code the solution but instead what features (what does it do) the solution will have.  For example for rockPaperScissorsGame.feature :
  - To run at command line using "python rockPaperScissors.py"
  - Use raw_input command to get moves (as numbers) and ask if should carry on (y or n)
  - Print out result
  - At end of game print out score
* You can use a package such as radish http://radish-bdd.io/ (similar to cucumber https://cucumber.io/ for Ruby https://www.ruby-lang.org/en/ ).  Basically you write a python program to run your future python app and state using "Given, When, Then" notation what input and output is expected for each feature.  These are tests that the finished application should pass. For example feature, "Only allow valid input to game".  You then run test to make sure it fails then you start writing the python app.
* TDD is working on one unit at a time, again from the outside of solution towards inside.  Using the pattern a guide you write a unit (method / function) only adding enough code to pass a test. This is called Red, Green, Refactor where red is write a failing test. Green is write enough code to just pass this and previous tests. Refactor is then tidy up code while making sure still passes test. For example unit tests for rockPaperScissors in test_rock.py:
  - Use unittest for testing see http://pythontesting.net/framework/unittest/unittest-introduction/
  - Try your best to write units using pure functions. A pure function does not produce side effects. It communicates with the calling program only through parameters (which it does not modify) and a return value.
  - Pattern is an "Infinite While Loop" that calls game function until user doesn't want to continue.
  - From outside in we start with "start" function that takes as parameters needed functions so, start(greeting, print_welcome, game_function, scores_function, score)
  - Write tests for this function.  There are two types of test:
    - State - tests the output of unit e.g. test_print_welcome() when greeting "Testing time to play" input as a parameter then it is expected to print "Testing time to play\n" to standard out (command line).
    - Behaviour - test what the code inside unit does.  This is usually uses mocks which are pre-written functions that remember how they were used. You can test this use and so test the behaviour of the code e.g. my_mock.print_test in test_rock.py:
      - Write failing test (red)
      - Used "my_mock.print_test" in place of print_function in "start"
      - Then test that only called once, "assert my_mock.print_test.call_count == 1"
      - This fails as no code written
      - Write code:
        - def print_welcome(greeting):
        - print greeting
      - Test now passes (green)
      - Refactor to tidy up if necessary
  - Continue writing tests and code for each function until code works as expected_output
* The BDD tests should now pass. Refactor code as appropriate while ensuing BDD and TDD tests continue to pass.
