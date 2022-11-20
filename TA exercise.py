class point :
    def __init__ (self,x,y):
        self.x = x
        self.y = y

def get_json_str(p):
    return {"__class__":'point','x':p.x,"y":p.y}

def read_json_str(s):
    return point(s.x,s.y) 


p = point(1,2)
z = (get_json_str(p))
print(z)