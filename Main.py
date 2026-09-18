import tkinter


okno = tkinter.Tk()
okno.title("tkinter, okno")

# Размер доски = 80% от высоты экрана
board_size = int(okno.winfo_screenheight() * 0.8)

# Размер одной клетки
cell_size = board_size // 8

# Размер окна
okno.geometry(f"{board_size}x{board_size}")

holst = tkinter.Canvas(
    okno,
    width=board_size,
    height=board_size,
    background="lightyellow"
)
holst.pack(fill=tkinter.BOTH, expand=True)


def paint_board():
    for delta_iy in range(8):
        delta_y = cell_size * delta_iy

        for delta_ix in range(8):
            delta_x = cell_size * delta_ix

            holst.create_rectangle(
                delta_x,
                board_size - delta_y - cell_size,
                delta_x + cell_size,
                board_size - delta_y,
                fill="black" if (delta_ix + delta_iy) % 2 == 0 else "white"
            )


paint_board()

okno.mainloop()
