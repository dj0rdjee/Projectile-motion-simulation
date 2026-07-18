import numpy as np
import matplotlib.pyplot as plt
from obstacles import Wall, Ceiling, H_Target, V_Target


class Projectile():
    """Represents a projectile and stores its initial conditions and trajectory."""
    def __init__(self, x, y, v0, angle_deg, mass, k):
        self.x = x
        self.y = y
        self.v0 = v0
        self.angle_rad = np.radians(angle_deg)

        self.mass = mass
        self.dragCoefficient = k #for now a simplified version of dragCoefficient
    
        self.vx = v0*np.cos(self.angle_rad)
        self.vy = v0*np.sin(self.angle_rad)

        self.v = np.sqrt(self.vx**2 + self.vy**2)
        #lists to store the whole trajectory for plotting
        self.x_points = [self.x]
        self.y_points = [self.y]

class Environment():
    """Stores global physical constants and specific boundaries."""
    def __init__(self):
        self.g = 9.81
        self.dt = 0.001 #timestop for integration (seconds)
        self.obstacles = [] #list of all obstacles

def initialize():
    """Prompts user for projectile parameters and returns a projectile instance"""
    x = float(input("Enter starting X coordinate: "))
    y = float(input("Enter starting Y coordinate: "))
    v0 = float(input("Enter initial velocity (m/s): "))
    angle = float(input("Enter launch angle (degrees): "))
    mass = float(input("Enter the mass of the projectile (default is 1): "))
    k = float(input("Enter the dragCoefficient (0 to disable): "))

    projectile = Projectile(x,y,v0,angle,mass,k)

    return projectile

def initialize_environment():
    """Prompts user for optional obstacles"""
    env = Environment()
    print("===Chose obstacles if present===")
    print("Available options: [wall], [ceiling], [h_target], [v_target], [done] ")
    while True:
        choice = input("what would you like to add? ").strip().lower()
        if choice == "done":
            break
        elif choice == "wall":
            x = float(input("X"))
            h = float(input("H"))
            env.obstacles.append(Wall(x, h))
        elif choice == "ceiling":
            y = float(input("y"))
            env.obstacles.append(Ceiling(y))
        elif choice == "h_target":
            x = float(input("x"))
            top = float(input("top"))
            bottom = float(input("bottom"))
            env.obstacles.append(H_Target(x, top, bottom))
        elif choice == "v_target":
            y = float(input("y"))
            left = float(input("left"))
            right = float(input("right"))
            env.obstacles.append(V_Target(y, left, right))
        
    return env

def simulate(bullet, env):
    """Runs simulation loop using Euler integration until the projectile hits the ground or an obstacle"""

    while bullet.y>=0:

        ax=0
        ay=-env.g

        bullet.v = np.sqrt(bullet.vx**2 + bullet.vy**2)

        if bullet.dragCoefficient > 0 and  bullet.v> 0:
            drag_x = -bullet.dragCoefficient * bullet.v * bullet.vx
            drag_y = -bullet.dragCoefficient * bullet.v * bullet.vy

            ax = drag_x / bullet.mass
            ay = -env.g + (drag_y / bullet.mass)

        bullet.vx += ax*env.dt
        bullet.vy += ay*env.dt

        bullet.x += bullet.vx*env.dt
        bullet.y += bullet.vy*env.dt
        
        bullet.x_points.append(bullet.x)
        bullet.y_points.append(bullet.y)

        hit_obstacle = False
        collision_msg = ""

        for obstacle in env.obstacles:
            if obstacle.check_collision(bullet):
                collision_msg = f"(colided with {type(obstacle).__name__}at X: {bullet.x:.2f}m, Y: {bullet.y:.2f}m)"
                hit_obstacle =  True

        if hit_obstacle:
            break
    print(f"time of flight was {len(bullet.x_points)*env.dt:.2f}s")
    print(f"maximal height reached was {max(bullet.y_points):.2f}m")
    print(f"distance travelled is {bullet.x_points[-1]-bullet.x_points[0]:.2f}m")

    if hit_obstacle:
        print(collision_msg)

    return 0

def plot(bullet,env):
    plt.plot(bullet.x_points, bullet.y_points, color="green", linewidth=2,)

    plt.grid(True)

    plt.xlim(left=0, right=None)
    plt.ylim(bottom=0, top=None)

    for obstacle in env.obstacles:
        obstacle.draw(plt)

    plt.show()

if __name__ == "__main__":
    env = initialize_environment()
    bullet = initialize()
    simulate(bullet, env)
    plot(bullet,env)