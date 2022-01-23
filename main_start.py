from tkinter import *
import pygame

pygame.mixer.init()
def play():
    pygame.mixer.music.load("C:\\Users\\Ram Reddy\\Desktop\\Space-Invaders-Pygame-master\\background.wav")
    pygame.mixer.music.set_volume(0.008)
    pygame.mixer.music.play(loops=-1)
##C:\\Users\\Ram Reddy\\Desktop\\Space-Invaders-Pygame-master

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options1 import easy
            easy.root.mainloop()
        elif args == 2:
            from Options1 import medium
            medium.root.mainloop()
        elif args == 3:
            from Options1 import hard
            hard.root.mainloop()

    def option():

        sel_btn1 = Button(text="Easy",width=18,borderwidth=8,font=("", 18),fg="#000000",bg="#99ffd6",cursor="hand2",command=lambda: start_game(1),)
        sel_btn2 = Button(text="Medium",width=18,borderwidth=8,font=("", 18),fg="#000000",bg="#99ffd6",cursor="hand2",command=lambda: start_game(2),)
        sel_btn3 = Button(text="Hard",width=18,borderwidth=8,font=("", 18),fg="#000000",bg="#99ffd6",cursor="hand2",command=lambda: start_game(3),)
        ##lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(50, 0), padx=50, )
        sel_btn2.grid(row=6, column=4, pady=(100, 0), padx=70, )
        sel_btn3.grid(row=12, column=4, pady=(130, 0), padx=90, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()

        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Catch Ball")
    main_window.configure(background="#000000")
    img0 = PhotoImage(file="catch.png")
    lab_img = Label(main_window,image=img0,bg='#e6fff5',)
    lab_img.pack(pady=(50, 0))
    start_btn = Button(main_window,text="Start",width=18,borderwidth=8,fg="#000000",bg="#78cc0a",font=("", 13),cursor="hand2",command=show_option,)
    start_btn.pack(pady=(50, 20))
    main_window.mainloop()


start_main_page()
