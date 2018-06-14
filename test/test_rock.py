import unittest
from mock import MagicMock
from mock import Mock
from mock import patch
import sys
from StringIO import StringIO

from rockPaperScissors import start
from rockPaperScissors import print_welcome
from rockPaperScissors import game
from rockPaperScissors import move
from rockPaperScissors import result
from rockPaperScissors import play_again
from rockPaperScissors import scores


# setup values for testing state and mocks for testing behaviour
greeting = "Testing time to play" # print welcome
my_mock = Mock()
game_one_round = MagicMock(side_effect = [(True, [0,0]), (False, [0,0])]) # one round game
score_test = [0,0]
score_test2 = [2,3]
result_mock = MagicMock(side_effect = [score_test])
move_mock = MagicMock(side_effect = [2])

class Test_rockPaperScissors(unittest.TestCase):

    def setUp(self):
        pass

    def test_start(self):
        # test behaviour for one round
        start(greeting, my_mock.print_test, game_one_round, my_mock.scores_test, score_test) # test
        assert my_mock.print_test.call_count == 1 # verify print_welcom called once
        assert game_one_round.call_count == 2 # verify game called twice
        assert my_mock.scores_test.call_count == 1 # verify score called once

    def test_print_welcome(self):
        # test state
        self.assert_stdout(greeting, 'Testing time to play\n')

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, greeting, expected_output, mock_stdout):
        print_welcome(greeting)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', return_value= 2)
    def test_game(self,mock_randint):
        expected_output = game(move_mock, result_mock, my_mock.play_again, score_test)
        # test state
        self.assertEqual(expected_output, (my_mock.play_again(), score_test))
        # test behaviour
        assert move_mock.call_count == 1 # verify move called once
        assert result_mock.call_count == 1 # verify result called once
        assert mock_randint.call_count == 1 # verify randint called once

    def test_valid_move(self):
        # test both return value and message for asking for a move
        with patch('__builtin__.raw_input', return_value = '2') as _raw_input:
            self.assertEqual(move(), 2)
            _raw_input.assert_called_once_with('Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ')

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_move(self, mock_stdout):
        # test what happens with invalid input
        with patch('__builtin__.raw_input', return_value = '4') as _raw_input:
            self.assertEqual(move(), 4)
            self.assertEqual(mock_stdout.getvalue(), "\nOops! I didn't understand that.\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_result(self, mock_stdout):
        # test state
        self.assertEqual(result(1, 1, [0,0]),[0,0]) # a tie
        self.assertEqual(mock_stdout.getvalue(), "Tie game.\n")
        mock_stdout.truncate(0)
        self.assertEqual(result(2, 1, [0,0]),[1,0]) # player wins, computer as paper>rock
        self.assertEqual(mock_stdout.getvalue(), "Your victory has been assured.\n")
        mock_stdout.truncate(0)
        self.assertEqual(result(3,1,[0,0]),[0,1]) # player loses,  scissors<rock
        self.assertEqual(mock_stdout.getvalue(), "Computer wins ha ha. Na na na na na you lose.\n")
        mock_stdout.truncate(0)
        self.assertEqual(result(2,3,[1,1]),[1,2]) # player loses, second round paper losses to scissors
        self.assertEqual(mock_stdout.getvalue(), "Computer wins ha ha. Na na na na na you lose.\n")
        mock_stdout.truncate(0)
        self.assertEqual(result(3,2,[1,2]),[2,2]) # player wins, scissors beats paper so back to two all
        self.assertEqual(mock_stdout.getvalue(), "Your victory has been assured.\n")
        mock_stdout.truncate(0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_play_again(self, mock_stdout):
        # Ask user if they want to play again
        with patch('__builtin__.raw_input', return_value = 'yes') as _raw_input:
            self.assertEqual(play_again(), 'yes')
            _raw_input.assert_called_once_with('Would you like to play again? y/n: ')
        with patch('__builtin__.raw_input', return_value = 'no') as _raw_input:
            self.assertEqual(play_again(), None)
            self.assertEqual(mock_stdout.getvalue(), "Bye. Thank you for playing\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_scores(self, mock_stdout):
        # print out scores
        scores(score_test2)
        self.assertEqual(mock_stdout.getvalue(),"HIGH SCORES\nPlayer: 2\nComputer: 3\n")

if __name__ == '__main__':
    unittest.main()
