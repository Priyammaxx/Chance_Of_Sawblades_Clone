class Player:
    def __init__(self, sprite, move_speed, jump_height):
        self.sprite = sprite
        self.move_speed = move_speed
        self.jump_height = jump_height
        self.current_height = 0

    def move_left(self):
        self.sprite.x -= self.move_speed
    
    def move_right(self):
        self.sprite.x += self.move_speed
    
    def jump(self, jump_speed):
        if self.current_height < self.jump_height:
            self.sprite.y -= jump_speed
            self.current_height += jump_speed

    def fall(self, gravity):
        self.sprite.y += gravity