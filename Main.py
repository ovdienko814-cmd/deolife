from chess_initializations import init_size
from gui import paint_board, facets, gran


tkinter, holst, start_x, start_y, cell_size, board_size, screen_height, screen_width = init_size()
gran(holst, start_x, start_y, board_size, screen_height, screen_width)
paint_board(holst, start_x, start_y, cell_size, screen_height, screen_width)
facets(holst, start_y, board_size, cell_size, start_x, screen_height, screen_width)

tkinter.mainloop()
