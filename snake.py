class Snake:

    def __init__(self, screen, size_node, direction):
        self.body = [(screen[0]//2, screen[1]//2), ]
        self.size_node = size_node
        self.direction = direction

    def move(self):
        head = self.body[0]
        new_head = (head[0]+self.direction[0], head[1]+self.direction[1])
        self.body.insert(0, new_head)

    def change_direction(self, new_direction):
        if (self.direction[0] != -new_direction[0] or
                self.direction[1] != -new_direction[1]):
            self.direction = new_direction

