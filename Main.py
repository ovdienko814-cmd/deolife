import tkinter

from gui import paint_board, facets,gran

okno = tkinter.Tk()
okno.state("zoomed")
okno.title("tkinter, okno")

holst = tkinter.Canvas(background="beige")
holst.pack(fill=tkinter.BOTH, expand=True)

screen_height = okno.winfo_screenheight()
screen_width = okno.winfo_screenwidth()
board_size = screen_height * 0.8
cell_size = board_size / 8

start_x = (screen_width - board_size) / 2
start_y = (screen_height - board_size) / 2 - 20
gran(holst, start_x, start_y, board_size)
facets(holst, start_y, board_size, cell_size, start_x)
paint_board(holst, start_x, start_y, cell_size)


okno.mainloop()