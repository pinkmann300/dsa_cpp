from enum import Enum 

class TrafficLight(Enum):
    RED = 30
    YELLOW = 5
    GREEN = 25

    def __init__(self, duration): 
        self.duration = duration

    def next(self): 
        if self == TrafficLight.RED: 
            self = TrafficLight.GREEN 
        elif self == TrafficLight.GREEN: 
            self = TrafficLight.YELLOW 
        elif self == TrafficLight.YELLOW: 
            self = TrafficLight.RED



class HttpStatusCode(Enum): 
    OK = (200, "OK") 
    BAD_REQUEST = (400, "Bad Request") 
    NOT_FOUND = (404, "Not Found") 
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error") 

    def __init__(self, code, message): 
        self.code = code 
        self.message = message 

    def is_success(self): 
        if self.code < 400: 
            return True 
        else:
            return False 
    
    def display(self): 
        print(f"{self.code} {self.message}")  

    @staticmethod
    def from_code(code): 
        for k in HttpStatusCode: 
            if k.code == code: 
                return k  

        return None