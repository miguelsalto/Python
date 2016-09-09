'''
Created on Sep 5, 2016

@author: miguelsalto
'''
from tictactoe.board import Board
from tictactoe.menu import Menu

class Game(object):
    EXIT_OPTION = 2
    UPPER_LEFT_CELL = 0
    UPPER_RIGHT_CELL = 2
    FROM_LEFT_TO_RIGHT_DIAGONAL_STEP = 4
    FROM_RIGHT_TO_LEFT_DIAGONAL_STEP = 2

    def __init__(self, read_function, print_function):
        self.player = 1
        self.board = Board(print_function)
        self.menu = Menu(read_function, print_function)
        self.print_function = print_function

    def start(self):
        while True:            
            option = self.menu.ask_menu_option()
            if option == self.EXIT_OPTION:
                break
            else:
                self.start_new_game()
                
    def start_new_game(self):
        self.board.create_numeric_cells()
        self.print_game_instructions()
        self.board.clean_marks()
        self.ask_cells()
    
    def print_game_instructions(self):
        self.print_function('Select the number of the cell that you want to mark\n')
        self.board.print_board()
        
    def ask_cells(self):
        while True:
            cell_number = self.get_selected_cell()
            self.board.mark_cell(cell_number, self.player)
            self.board.print_board()
            if self.is_won():
                self.print_winner_message()
                break
            elif self.board.marked_cells == Board.NUMBER_OF_CELLS:
                self.print_tied_game_message()
                break
            else:
                self.switch_player()
            
    
    def print_winner_message(self):
        self.print_function(' Player {p} wins the game!!\n'.format(p=self.player))
        
    def print_tied_game_message(self):
        self.print_function(' The game is over and this is a tie!!\n')
        
    def switch_player(self):
        self.player = 2 if self.player == 1 else 1
    
    def get_selected_cell(self):
        while True:
            cell_num = self.menu.ask_cell(self.player)
            if self.board.is_cell_marked(cell_num):
                self.print_function('The cell is already marked, please select another one\n')
            else:
                return cell_num 
    
    @staticmethod
    def is_trio_equal(mark1, mark2, mark3):
        return mark1 == mark2 == mark3 and mark1 != ' '
    
    def is_won_in_row(self, row):
        cells = self.board.cells
        idx = Board.get_start_index_for_row(row)
        return self.is_trio_equal(cells[idx], cells[idx + 1], cells[idx + 2])
    
    def is_won_in_column(self, col):
        cells = self.board.cells
        step_for_next_row = Board.ROW_LENGTH
        idx = col - 1
        return self.is_trio_equal(cells[idx], cells[idx + step_for_next_row], cells[idx + 2 * step_for_next_row])
    
    def is_won_in_rows(self):        
        return self.is_won_in_row(1) or self.is_won_in_row(2) or self.is_won_in_row(3)
    
    def is_won_in_columns(self):
        return self.is_won_in_column(1) or self.is_won_in_column(2) or self.is_won_in_column(3)
    
    def is_won_in_diagonal(self, start_index, step):
        cells = self.board.cells
        return self.is_trio_equal(cells[start_index], cells[start_index + step], cells[start_index + step * 2])
    
    def is_won_in_diagonals(self):
        return self.is_won_in_diagonal(self.UPPER_LEFT_CELL, self.FROM_LEFT_TO_RIGHT_DIAGONAL_STEP) \
            or self.is_won_in_diagonal(self.UPPER_RIGHT_CELL, self.FROM_RIGHT_TO_LEFT_DIAGONAL_STEP)
    
    def is_won(self):
        return self.is_won_in_columns() or self.is_won_in_rows() or self.is_won_in_diagonals()
        
