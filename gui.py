def paint_board(holst):

    for delta_iy in range(8):
        delta_y = 40 * delta_iy

        for delta_ix in range(8):
            delta_x = 40 * delta_ix

            holst.create_rectangle(500 + delta_x,500 - delta_y,540 + delta_x,540 - delta_y, fill="orange" if (delta_ix + delta_iy) % 2 == 0 else "red")


def facets(holst):

    movement_x = 520

    for bukwa in range(8):
        letters = "ABCDEFGH"
        holst.create_text(movement_x, 551 , text=letters[bukwa], width = 4)
        movement_x += 40
        movement_y = 520

        for chisla in range(8):
            numbers = "12345678"
            holst.create_text(490, movement_y, text=numbers[chisla], width = 4)
            movement_y -= 40


def draw_frame(holst):

    holst.create_rectangle(475, 195, 845, 565, fill = "orange", width = 5)
    holst.create_line(475, 195, 845, 565, width = 3)
    holst.create_line(475, 565, 845, 195, width = 3)

def draw_board_frame(holst):

    holst.create_rectangle(500, 540, 821, 220, width = 4)