from abc import ABC, abstractmethod
import numpy as np

class DifferentialEquation(ABC):
    @abstractmethod
    def __call__(self,t,state):
        pass

class OrbitalMotion(DifferentialEquation):
    
    def __init__(self,G,M):
        self.G = G
        self.M = M

    def __call__(self,t,state):

        """Return the derivatives of the state vector.
        The state represents the position and velocity of the planet in
        2D space, so state = [x, y, vx, vy]
        Parameters:
        t (float): Time
        state (list): State vector [x, y, vx, vy]
        Returns:
        list: Derivatives [vx, vy, ax, ay]
        """
        assert isinstance(state, (list, np.ndarray))
        assert isinstance(t, (float,int))
        #unpack state vector
        x, y, vx, vy = state

        # find distance to central body
        r = np.sqrt(x**2 + y**2)
        if r ==0:
            raise ValueError("x and y cannot be 0")

        #compute acceleration vector
        ax = -((self.G * self.M)/(r**3))*(x)
        ay = -((self.G * self.M)/(r**3))*(y)

        return [vx,vy,ax,ay]