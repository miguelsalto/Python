'''
Created on Sep 4, 2016

@author: miguelsalto
'''
class Board(object):
    ROW_LENGTH = 3
    CELL_WIDTH = 5
    NUMBER_OF_CELLS = 9    
    
    def __init__(self, print_function):
        self.marked_cells = 0
        self.print_function = print_function
        self.create_numeric_cells()
        
    def create_numeric_cells(self):
        self.cells = [str(idx + 1) for idx in range(0, Board.NUMBER_OF_CELLS)]
    
    def clean_marks(self):
        for idx in range(0, Board.NUMBER_OF_CELLS):
            self.cells[idx] = ' '
        self.marked_cells = 0
            
    def mark_cell(self, cell_number, player):
        self.cells[cell_number - 1] = 'X' if player == 1 else 'O'
        self.marked_cells += 1
        
    def is_cell_marked(self, cell_num):
        return self.cells[cell_num - 1] != ' '
        
    def print_simple_line(self):
        self.print_function('     |     |     \n')
        
    def print_divison_line(self):
        self.print_function('-----------------\n')
    
    @staticmethod
    def get_mark_label(mark):
        return mark.center(Board.CELL_WIDTH, ' ')
        
    def get_cells_of_row(self, row):
        cell_index = Board.get_start_index_for_row(row) 
        return [self.cells[idx] for idx in range(cell_index, cell_index + Board.ROW_LENGTH)]
    
    @staticmethod
    def get_start_index_for_row(row):
        return  (row - 1) * Board.ROW_LENGTH
    
    def print_line_with_marks(self, cells):        
        self.print_function('{mark1}|{mark2}|{mark3}\n'
                         .format(
                                 mark1=Board.get_mark_label(cells[0]),
                                 mark2=Board.get_mark_label(cells[1]),
                                 mark3=Board.get_mark_label(cells[2])))
    
    def print_row(self, row):
        cells = self.get_cells_of_row(row)
        self.print_simple_line()
        self.print_line_with_marks(cells)
        self.print_simple_line()
            
    def print_board(self):
        self.print_row(1)
        self.print_divison_line()
        self.print_row(2)
        self.print_divison_line()
        self.print_row(3)
        
