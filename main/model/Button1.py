class Button:
    def __init__(self, font_size, font_color, back_color, msg, pos, rect):
        self.font_size = font_size
        self.color = font_color
        self.back_color = back_color
        self.msg = msg
        self.pos = pos
        self.width, self.height = rect
        self._reversed = False
        self._onclick = False

    def reverse_color(self):
        self.color, self.back_color = self.back_color, self.color

    @property
    def onclick(self):
        if self._onclick:
            self._onclick = False
            return True
        else:
            return False

    def update(self, mouse_pos, keys):
        if 0 < mouse_pos.x - self.pos.x < self.width and 0 < mouse_pos.y - self.pos.y < self.height:
            if not self._reversed:
                self.reverse_color()
                self._reversed = True
            if keys.click:
                self._onclick = True
        else:
            if self._reversed:
                self.reverse_color()
                self._reversed = False
