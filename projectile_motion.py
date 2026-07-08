import numpy as np
import matplotlib.pyplot as plt

class Projectile():
    """Represents a projectile and stores its initial conditions and trajectory."""
    def __init__(self, x, y, v0, angle_deg):
        self.x = x
        self.y = y
        self.v0 = v0
        self.angle_rad = np.radians(angle_deg)
        self.vx = v0*np.cos(self.angle_rad)
        self.vy = v0*np.sin(self.angle_rad)
        #lists to store the whole trajectory for plotting
        self.x_points = [self.x]
        self.y_points = [self.y]

class Environment():
    """Stores global physical constants and specific boundaries."""
    def __init__(self):
        self.g = 9.81
        self.dt = 0.001 #timestop for integration (seconds)

        self.wall_x = None
        self.wall_height = None

def initialize():
    """Prompts user for projectile parameters and returns a projectile instance"""
    x = float(input("Enter starting X coordinate: "))
    y = float(input("Enter starting Y coordinate: "))
    v0 = float(input("Enter initial velocity (m/s): "))
    angle = float(input("Enter launch angle (degrees): "))

    projectile = Projectile(x,y,v0,angle)

    return projectile

def initialize_environment():
    """Prompts user for optional obstacles"""
    env = Environment()

    choice = input("Do you want to add a wall? (yes/no)").strip().lower()
    if choice == "yes":
        env.wall_x = float(input("Enter the x coordinate of the wall: "))
        env.wall_height = float(input("enter the height of the wall: "))
    else:
        pass

    return env

def simulate(bullet, env):
    """Runs simulation loop using Euler integration until the projectile hits the ground or an obstacle"""
    hit_wall=False

    while bullet.y>=0:
  
        ax=0
        ay=-env.g

        bullet.x += bullet.vx*env.dt
        bullet.y += bullet.vy*env.dt

        bullet.vx += ax*env.dt
        bullet.vy += ay*env.dt
        
        bullet.x_points.append(bullet.x)
        bullet.y_points.append(bullet.y)

        if env.wall_x is not None and env.wall_height is not None:
            if bullet.x >= env.wall_x:
                if bullet.y <= env.wall_height:
                    hit_wall = True
                    break

    print(f"time of flight was {len(bullet.x_points)*env.dt:.2f}s")
    print(f"maximal height reached was {max(bullet.y_points):.2f}m")
    print(f"distance travelled is {bullet.x_points[-1]-bullet.x_points[0]:.2f}m")

    if hit_wall:
        print(f"colided with a wall at X: {env.wall_x:.2f}m Height: {bullet.y:.2f}m")
    return 0

def plot(bullet,env):
    plt.plot(bullet.x_points, bullet.y_points, color="green", linewidth=2,)

    plt.grid(True)

    plt.xlim(left=0, right=None)
    plt.ylim(bottom=0, top=None)

    if env.wall_x is not None and env.wall_height is not None:
        wall_x = [env.wall_x, env.wall_x]
        wall_y = [0, env.wall_height]
        plt.plot(wall_x, wall_y, color="red", linewidth=3)
    #plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    env = initialize_environment()
    bullet = initialize()
    simulate(bullet, env)
    plot(bullet,env)