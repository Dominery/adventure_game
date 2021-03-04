class InterfaceState:
    def __init__(self,buttons):
        self.buttons = buttons

    @classmethod
    def start(cls,buttons):
        return cls(buttons)

    def update(self,pos,keys):
        for button in self.buttons:
            button.update(pos,keys)