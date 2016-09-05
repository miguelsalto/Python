'''
Created on Sep 4, 2016

@author: miguelsalto
'''
from tictactoe.board import Board

import unittest

class Test(unittest.TestCase):
    BOARD_CELLS = 9
    
    def setUp(self):
        self.returned_string = ''

    def print_function(self, string):
        self.returned_string += string
        
    def test_board_creation(self):
        board = Board(self.print_function)
        self.assertEqual(len(board.cells), 9)
        self.assertEqual(board.marked_cells, 0)
        for idx in range(0, 9):
            cell_number = str(idx + 1)
            self.assertEqual(board.cells[idx], cell_number)
    
    def test_clean_marks(self):
        board = Board(self.print_function)
        board.clean_marks()
        zero_elements = list(filter(lambda val : val == ' ', board.cells))
        self.assertEqual(len(zero_elements), 9)
         
    def test_print_simple_line(self):
        board = Board(self.print_function)
        board.print_simple_line()
        self.assertEqual(self.returned_string, '     |     |     \n')
        
    def test_print_divison_line(self):
        board = Board(self.print_function)
        board.print_divison_line()
        self.assertEqual(self.returned_string, '-----------------\n')
         
    def test_get_mark_label_for_cell(self):
        board = Board(self.print_function)
        for idx in range(0, 9):
            cell = board.cells[idx]
            self.assertEqual(Board.get_mark_label(cell), '  {mark}  '.format(mark=idx + 1))
    
    def test_print_row(self):
        board = Board(self.print_function)
        board.print_row(1)
        self.assertEqual(self.returned_string, '     |     |     \n  1  |  2  |  3  \n     |     |     \n')
        
    def test_print_board_for_instructions(self):
        board = Board(self.print_function)
        board.print_board()
        expected_string = '     |     |     \n  1  |  2  |  3  \n     |     |     \n'
        expected_string += '-----------------\n'
        expected_string += '     |     |     \n  4  |  5  |  6  \n     |     |     \n'
        expected_string += '-----------------\n'
        expected_string += '     |     |     \n  7  |  8  |  9  \n     |     |     \n'
        self.assertEqual(self.returned_string, expected_string)

    def test_print_board_for_cleaned_marks(self):
        board = Board(self.print_function)
        board.clean_marks()
        board.print_board()
        expected_string = '     |     |     \n     |     |     \n     |     |     \n'
        expected_string += '-----------------\n'
        expected_string += '     |     |     \n     |     |     \n     |     |     \n'
        expected_string += '-----------------\n'
        expected_string += '     |     |     \n     |     |     \n     |     |     \n'
        self.assertEqual(self.returned_string, expected_string)

    def test_print_board_for_marked_cell(self):
        board = Board(self.print_function)
        board.clean_marks()
        self.assertFalse(board.is_cell_marked(5))
        board.mark_cell(5, 1)
        self.assertTrue(board.is_cell_marked(5))
        board.print_board()
        expected_string = '     |     |     \n     |     |     \n     |     |     \n'
        expected_string += '-----------------\n'
        expected_string += '     |     |     \n     |  X  |     \n     |     |     \n'
        expected_string += '-----------------\n'
        expected_string += '     |     |     \n     |     |     \n     |     |     \n'
        self.assertEqual(self.returned_string, expected_string)
        self.assertEqual(board.marked_cells, 1)
        
if __name__ == "__main__":
    unittest.main()
