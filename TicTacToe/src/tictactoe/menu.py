'''
Created on Sep 5, 2016

@author: miguelsalto
'''
from tictactoe.board import Board

class Menu(object):
    
    def __init__(self, read_function, print_function):
        self.read_function = read_function
        self.print_function = print_function
        
    def print_menu_instructions(self):
        self.print_function('Press the number key of the option that you want and then press enter to apply your option:\n')
        self.print_function('1) Start the game:\n')
        self.print_function('2) Exit\n')
    
    def print_invalid_number_message(self):
        self.print_function('That is not a valid number, try again\n')
    
    def print_invalid_option_message(self):
        self.print_function('Invalid option, you have to select option 1 or 2\n')
        
    def print_player_turn_message(self, player):
        self.print_function('Player {p}''s turn\n'.format(p = player))
    
    def ask_menu_option(self):
        return self.ask_valid_option(self.print_menu_instructions, '>> ', 2)
                
    def ask_cell(self, player):
        print_message_function = lambda : self.print_player_turn_message(player)
        return self.ask_valid_option(print_message_function, 'Cell Number: ', Board.NUMBER_OF_CELLS)
    
    def ask_valid_option(self, print_message_function, input_label, max_allowed_option):
        while True:
            print_message_function()
            try:
                option = int(self.read_function(input_label))
                if 1 <= option <= max_allowed_option:
                    return option
                self.print_invalid_option_message()
            except ValueError:
                self.print_invalid_number_message()
