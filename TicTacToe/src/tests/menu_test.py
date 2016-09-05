'''
Created on Sep 5, 2016

@author: miguelsalto
'''
from tictactoe.menu import Menu
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        self.returned_string = ''
        
    def print_function(self, string):
        self.returned_string += string
    
    @staticmethod
    def get_menu_instructions_string():
        string = 'Press the number key of the option that you want and then press enter to apply your option:\n'
        string += '1) Start the game:\n'
        string += '2) Exit\n'
        return string
    
    def test_print_menu_instructions(self):
        menu = Menu(None, self.print_function)
        menu.print_menu_instructions()
        self.assertEqual(self.returned_string, Test.get_menu_instructions_string())
        
    def test_print_invalid_number_message(self):
        menu = Menu(None, self.print_function)
        menu.print_invalid_number_message()
        expected_string = 'That is not a valid number, try again\n'
        self.assertEqual(self.returned_string, expected_string)
        
    def test_print_invalid_option_message(self):
        menu = Menu(None, self.print_function)
        menu.print_invalid_option_message()
        expected_string = 'Invalid option, you have to select option 1 or 2\n'
        self.assertEqual(self.returned_string, expected_string)
    
    def test_print_player_turn_message(self):
        menu = Menu(None, self.print_function)
        menu.print_player_turn_message(1)
        expected_string = 'Player 1''s turn\n'
        self.assertEqual(self.returned_string, expected_string)

    def test_ask_menu_option_for_start_game_option(self):
        expected_option = 1
        menu = Menu(lambda n: expected_option, self.print_function)
        option = menu.ask_menu_option()
        self.assertEqual(option, expected_option)
        
    def test_ask_menu_option_for_exit_option(self):
        expected_option = 2
        menu = Menu(lambda n: expected_option, self.print_function)
        option = menu.ask_menu_option()
        self.assertEqual(option, expected_option)
    
    def test_ask_menu_option_for_invalid_number(self):
        expected_option = 2
        options = [expected_option, 'x']        
        menu = Menu(lambda _: options.pop(), self.print_function)
        option = menu.ask_menu_option()
        self.assertEqual(option, expected_option)
        
        expected_printed_string = Test.get_menu_instructions_string()
        expected_printed_string += 'That is not a valid number, try again\n'
        expected_printed_string += Test.get_menu_instructions_string()
        self.assertEqual(self.returned_string, expected_printed_string)
        
    def test_ask_menu_option_for_option_lower_than_min_allowed(self):
        expected_option = 2
        options = [expected_option, 0]        
        menu = Menu(lambda _: options.pop(), self.print_function)
        option = menu.ask_menu_option()
        self.assertEqual(option, expected_option)
        
        expected_printed_string = Test.get_menu_instructions_string()
        expected_printed_string += 'Invalid option, you have to select option 1 or 2\n'
        expected_printed_string += Test.get_menu_instructions_string()
        self.assertEqual(self.returned_string, expected_printed_string)
        
    def test_ask_menu_option_for_option_greater_than_max_allowed(self):
        expected_option = 2
        options = [expected_option, 3]        
        menu = Menu(lambda _: options.pop(), self.print_function)
        option = menu.ask_menu_option()
        self.assertEqual(option, expected_option)
        
        expected_printed_string = Test.get_menu_instructions_string()
        expected_printed_string += 'Invalid option, you have to select option 1 or 2\n'
        expected_printed_string += Test.get_menu_instructions_string()
        self.assertEqual(self.returned_string, expected_printed_string)
        
    def test_ask_cell_for_valid_cell(self):
        expected_option = 2
        menu = Menu(lambda n: expected_option, self.print_function)
        option = menu.ask_cell(1)
        self.assertEqual(option, expected_option)
        
    def test_ask_cell_for_invalid_number(self):
        expected_option = 2
        options = [expected_option, 'x']        
        menu = Menu(lambda _: options.pop(), self.print_function)
        option = menu.ask_cell(1)
        self.assertEqual(option, expected_option)
        
        expected_printed_string = 'Player 1''s turn\n'
        expected_printed_string += 'That is not a valid number, try again\n'
        expected_printed_string += 'Player 1''s turn\n'
        self.assertEqual(self.returned_string, expected_printed_string)
        
    def test_ask_cell_for_option_lower_than_min_allowed(self):
        expected_option = 2
        options = [expected_option, 0]        
        menu = Menu(lambda _: options.pop(), self.print_function)
        option = menu.ask_cell(1)
        self.assertEqual(option, expected_option)
        
        expected_printed_string = 'Player 1''s turn\n'
        expected_printed_string += 'Invalid option, you have to select option 1 or 2\n'
        expected_printed_string += 'Player 1''s turn\n'
        self.assertEqual(self.returned_string, expected_printed_string)

    def test_ask_cell_for_option_greater_than_min_allowed(self):
        expected_option = 2
        options = [expected_option, 10]        
        menu = Menu(lambda _: options.pop(), self.print_function)
        option = menu.ask_cell(1)
        self.assertEqual(option, expected_option)
        
        expected_printed_string = 'Player 1''s turn\n'
        expected_printed_string += 'Invalid option, you have to select option 1 or 2\n'
        expected_printed_string += 'Player 1''s turn\n'
        self.assertEqual(self.returned_string, expected_printed_string)
        
if __name__ == "__main__":
    unittest.main()
