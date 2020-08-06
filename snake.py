class Snake:

    def __init__(self, screen, size_node, direction):
        self.body = [(screen[0]//2, screen[1]//2), ]
        self.size_node = size_node
        self.direction = direction
        self.screen = screen

    def move(self):
        """
            Return True if the snake move successfully
            Return False if get out of screen of collision him
        """
        head = self.body[0]
        self.body.insert(0, (head[0]+self.direction[0], head[1]+self.direction[1]))
        return self.on_screen() and not self.collision()

    def change_direction(self, new_direction):
        if (self.direction[0] != -new_direction[0] or
                self.direction[1] != -new_direction[1]):
            self.direction = new_direction

    def on_screen(self):
       if not 0 <= self.body[0][0] < self.screen[0]:
          return False 
       return 0 <= self.body[0][1] < self.screen[1]

    def collision(self):
        head = self.body[0]
        for node in self.body[1:]:
            if head == node:
                return True
        return False

