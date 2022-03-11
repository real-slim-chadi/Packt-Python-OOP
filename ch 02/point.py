import math # to be able to use the math functionality within the object

class Point:
    """Generates a point in a Eucledian plane
    """
    def __init__(self, x: float=0, y: float=0) -> None:
        """Initializes the point to the coordinates (x,y)

        Args:
            x (float, optional): Defaults to 0.
            y (float, optional): Defaults to 0.
        """
        self.x=x 
        self.y=y
    def move (self, x: float, y: float) -> None:
        """move the point to coordinates (x,,y)

        Args:
            x (float): new x
            y (float): new y
        """
        self.x=x
        self.y=y 
    def reset(self) -> None:
        """resets point to (0,0)
        """
        self.x=0
        self.y=0
    def calculate_distance(self, p: "Point") -> float:
        """calculates distance between this Point and p

        Args:
            p (Point): second point to compare with

        Returns:
            float: Eucledian distance to p Point
        """
        return math.hypot(self.x-p.x,self.y-p.y) 

if (__name__=="__main__"):
    p= Point()
    p.reset()

    print (p.x,p.y) # 0 0
    print ("__name__:",__name__)