from main.vec import Vec


class Player:
    size = Vec(0.8,1.5)
    player_x_speed = 7
    gravity = 30
    jump_speed = 17

    def __init__(self,pos,speed):
        self._pos = pos
        self._speed = speed

    @classmethod
    def create(cls,pos,char=None):
        return cls(pos.plus(Vec(0,-0.5)),Vec(0,0))

    @property
    def type(self):
        return "player"

    @property
    def pos(self):
        return self._pos

    def update(self,time,state,keys):
        x_speed = 0
        if keys.ArrowLeft:
            x_speed -= self.player_x_speed
        if keys.ArrowRight:
            x_speed += self.player_x_speed
        pos = self._pos
        moved_x = pos.plus(Vec(x_speed*time,0))
        if not state.level.touches(moved_x, self.size, "wall"):
            pos = moved_x

        y_speed = self._speed.y + time*self.gravity
        moved_y = pos.plus(Vec(0,y_speed*time))
        if not state.level.touches(moved_y,self.size,"wall"):
            pos = moved_y
        elif keys.ArrowUp and y_speed>0:
            y_speed = -self.jump_speed
        else:
            y_speed = 0
        return Player(pos,Vec(x_speed,y_speed))


