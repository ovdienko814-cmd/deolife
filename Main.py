import tkinter

from gui import paint_board, facets, draw_frame, draw_board_frame


okno = tkinter.Tk()

okno.config(width = 400, height = 400, bg = "pink")

okno.title("tkinter, okno")


holst = tkinter.Canvas(background = "beige")

holst.pack(fill = tkinter.BOTH, expand = True)


draw_frame(holst)
draw_board_frame(holst)
facets(holst)
paint_board(holst)


okno.mainloop()