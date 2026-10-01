def paint_board(holst, start_x, start_y, cell_size, screen_height, screen_width):
    for delta_iy in range(8):
        delta_y = cell_size * delta_iy

        for delta_ix in range(8):
            delta_x = cell_size * delta_ix
            holst.create_rectangle(start_x + delta_x, start_y + delta_y, start_x + cell_size
             + delta_x, start_y + cell_size + delta_y, fill="orange" if (delta_ix + delta_iy) % 2 == 0 else "red")


def gran(holst, start_x, start_y, board_size, screen_height, screen_width):
    holst.create_rectangle(start_x - 25, start_y - 25, start_x + board_size + 25,
    start_y + board_size + 25, fill="orange", width=5)
    holst.create_line(start_x - 25, start_y - 25, start_x + board_size + 25, start_y + board_size + 25, width=3)
    holst.create_line(start_x - 25, start_y + board_size + 25, start_x + board_size + 25, start_y - 25, width=3)
    holst.create_rectangle(start_x, start_y, start_x + board_size, start_y + board_size, width=4)


def facets(holst, start_y, board_size, cell_size, start_x, screen_height, screen_width):
    letters = "ABCDEFGH"
    movement_x = start_x + cell_size / 2
    for bukwa in range(8):
        holst.create_text(movement_x, start_y + board_size + 12, text=letters[bukwa])
        movement_x += cell_size
        numbers = "87654321"
        movement_y = start_y + cell_size / 2
    for chisla in range(8):
            holst.create_text(start_x - 12, movement_y, text=numbers[chisla])
            movement_y += cell_size