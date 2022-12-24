from paddle import Paddle


STARTING_POSITIONS = [(-350, 0), (-350, -20), (-350, -40), (-350, -60)]

class SecondPaddle(Paddle):

    def __init__(self):
        super().__init__()
