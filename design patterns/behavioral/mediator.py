from typing import Dict

class Airplane:
    def take_off(self):
        print("Airplane is taking off")

    def land(self):
        print("Airplane is landing")

class Runway:
    def __init__(self):
        self.clear = True

class Tower:
    def __init__(self, runways: Dict[str, Runway]):
        self.runways = runways

    def request_runway(self, runway: Runway, airplane: Airplane):
        if runway.clear:
            self.allocate_runway(runway)
            airplane.take_off()
            return True
        return False

    def allocate_runway(self, runway: Runway):
        runway.clear = False

    def release_runway(self, runway: Runway):
        runway.clear = True
    
runway25A = Runway()
runway25B = Runway()
runway31 = Runway()

tower = Tower({"25A": runway25A, "25B": runway25B, "31": runway31})


airplane1 = Airplane()
airplane2 = Airplane()

tower.request_runway(runway25A, airplane1)
# tower.request_runway(runway25A) 
tower.request_runway(runway25A, airplane1)