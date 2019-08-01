class Block():
    def __init__(self, xleft, yup, xvelocity, yvelocity, width, height, color):
        self.xleft = xleft
        self.yup = yup
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.width = width
        self.height = height
        self.color = color
    def move(self):
        self.xleft += self.xvelocity
        self.yup += self.yvelocity