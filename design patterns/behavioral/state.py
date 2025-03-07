from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass
    
class OpenState(State):
    def handle(self):
        return "Opening the door"
    
class CloseState(State):
    def handle(self):
        return "Closing the door"
    
class HalfOpenState(State):
    def handle(self):
        return "Half opening the door"

class Door:
    def __init__(self):
        self.state = CloseState()
        
    def change_state(self, state: State):
        self.state = state
        
    def handle(self):
        return self.state.handle()

door = Door()
print(door.handle())
door.change_state(OpenState())  
print(door.handle())
door.change_state(HalfOpenState())
print(door.handle())