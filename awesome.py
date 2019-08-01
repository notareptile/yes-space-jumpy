from block import Block

class Ground(Block):
    def __init__(self, xleft, yup, yvelocity, width, color):
        super().__init__(xleft, yup, 0, yvelocity, width, self.height, color)
    def checkdestroy(self):
        if self.yup > 700:
            self.shoulddestroy = True