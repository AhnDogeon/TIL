import turtle as t






class MagicBrush:
    t.color('red')
    def draw_square(self):
        for i in range(4):
            t.forward(100)
            t.right(90)


    def draw_triangle(self):
        for i in range(3):
            t.forward(100)
            t.right(120)
    
    def go(self):
        t.forward(200)

    def turn(self):
        t.right(90)


m1= MagicBrush()
m2=MagicBrush()

brad = t.Turtle()
brad.shape('turtle')
brad.speed(2)
brad.forward(100)


t.mainloop()