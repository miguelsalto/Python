'''
Created on Sep 5, 2016

@author: miguelsalto
'''
from tictactoe.game import Game
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.returned_string = ''

    def print_function(self, string):
        self.returned_string += string

    def test_game_creation(self):
        game = Game(None, None)
        self.assertEqual(game.player, 1)
        self.assertIsNotNone(game.board)
        
    def test_print_game_instructions(self):
        game = Game(None, self.print_function)
        game.print_game_instructions()
        printed_messages = self.returned_string.split('\n')
        expected_message = 'Select the number of the cell that you want to mark'
        self.assertEqual(printed_messages[0], expected_message)
        
    def test_print_winner_message(self):
        game = Game(None, self.print_function)
        game.print_winner_message()
        self.assertEqual(self.returned_string, ' Player 1 wins the game!!\n')
        
        game.switch_player()
        self.returned_string = ''
        game.print_winner_message()
        self.assertEqual(self.returned_string, ' Player 2 wins the game!!\n')
        
    def test_print_tied_game_message(self):
        game = Game(None, self.print_function)
        game.print_tied_game_message()
        self.assertEqual(self.returned_string, ' The game is over and this is a tie!!\n')
        
    def test_get_selected_cell(self):
        expected_option = 1
        game = Game(lambda n: expected_option, self.print_function)
        game.board.clean_marks()
        option = game.get_selected_cell()
        self.assertEqual(option, expected_option)
        
    def test_get_selected_cell_with_marked_cell_selection(self):
        expected_option = 2
        selected_options = [2, 1]
        game = Game(lambda n: selected_options.pop(), self.print_function)
        game.board.clean_marks()
        game.board.mark_cell(1, 1)
        option = game.get_selected_cell()
        self.assertEqual(option, expected_option)
        
        expected_printed_messages = 'Player 1s turn\n'
        expected_printed_messages += 'The cell is already marked, please select another one\n'
        expected_printed_messages += 'Player 1s turn\n'
        self.assertEqual(self.returned_string, expected_printed_messages)
        
        
    def test_is_trio_equal(self):
        self.assertFalse(Game.is_trio_equal('X', 'X', 'O'))
        self.assertFalse(Game.is_trio_equal('X', 'O', 'X'))
        self.assertFalse(Game.is_trio_equal('O', 'X', 'X'))
        self.assertTrue(Game.is_trio_equal('X', 'X', 'X'))
        
    def test_is_won_in_rows(self):
        game = Game(None, None)
        game.board.clean_marks()
        self.assertFalse(game.is_won())
        
        game.board.mark_cell(7, 1)
        game.board.mark_cell(8, 1)
        game.board.mark_cell(9, 1)
        self.assertTrue(game.is_won())
        
    def test_is_won_in_columns(self):
        game = Game(None, None)
        game.board.clean_marks()
        self.assertFalse(game.is_won())
        
        game.board.mark_cell(3, 1)
        game.board.mark_cell(6, 1)
        game.board.mark_cell(9, 1)
        self.assertTrue(game.is_won())
    
    def test_is_won_in_diagonals_from_left_to_right_diagonal(self):
        game = Game(None, None)
        game.board.clean_marks()
        self.assertFalse(game.is_won())
        
        game.board.mark_cell(1, 1)
        game.board.mark_cell(5, 1)
        game.board.mark_cell(9, 1)
        self.assertTrue(game.is_won())
    
    def test_is_won_in_diagonals_from_right_to_left_diagonal(self):
        game = Game(None, None)
        game.board.clean_marks()
        self.assertFalse(game.is_won())
        
        game.board.mark_cell(3, 1)
        game.board.mark_cell(5, 1)
        game.board.mark_cell(7, 1)
        self.assertTrue(game.is_won())  
        
    def test_ask_cells_for_won_game(self):
        game = Game(lambda n: 3, self.print_function)
        game.board.clean_marks()
        game.board.mark_cell(1, 1)
        game.board.mark_cell(2, 1)
        
        game.ask_cells()
        self.assertTrue(game.is_won())
        expected_printed_messages = ' Player 1 wins the game!!'
        messages = self.returned_string.split('\n')
        win_message = messages[len(messages) - 2]
        self.assertEqual(win_message, expected_printed_messages)
        
    def test_ask_cells_for_tied_game(self):
        selected_cells = [1, 5, 9, 2, 8, 7, 3, 6, 4]
        game = Game(lambda _: selected_cells.pop(), self.print_function)
        game.board.clean_marks()
        game.ask_cells()
        self.assertFalse(game.is_won())
        expected_printed_messages = ' The game is over and this is a tie!!'
        messages = self.returned_string.split('\n')
        win_message = messages[len(messages) - 2]
        self.assertEqual(win_message, expected_printed_messages)
        
    def test_start_game_for_exit_option(self):
        game = Game(lambda _: 2, self.print_function)
        game.start()
        self.assertFalse(game.is_won())
        
    def test_start_game_for_play_option(self):
        selected_options = [2, 6, 2, 3, 7, 9, 5, 1, 1]
        game = Game(lambda _: selected_options.pop(), self.print_function)
        game.start()
        self.assertTrue(game.is_won())

if __name__ == "__main__":
    unittest.main()
