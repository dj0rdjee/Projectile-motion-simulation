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
        #wall
        self.wall_x = None
        self.wall_height = None
        #target
        self.target_x = None
        self.target_top = None
        self.target_bottom = None
        #ceiling
        self.ceiling_y = None

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
    print("===Chose obstacles if present===")
    print("Available options: [wall], [target], [ceiling], [done] ")
    while True:
        choice = input("what would you like to add? ").strip().lower()
        if choice == "done":
            break
        elif choice == "wall":
            env.wall_x = float(input("Enter the x coordinate of the wall: "))
            env.wall_height = float(input("enter the height of the wall: "))
        elif choice == "target":
            env.target_x = float(input("Enter the x coordinate of the target: "))
            env.target_top = float(input("enter the top of the target: "))
            env.target_bottom = float(input("enter the bottom of the target: "))
        elif choice == "ceiling":
            env.ceiling_y = float(input("enther the height of a ceiling: "))
        
    return env

def simulate(bullet, env):
    """Runs simulation loop using Euler integration until the projectile hits the ground or an obstacle"""
    hit_wall = False
    hit_target = False
    hit_ceiling = False
    while bullet.y>=0:
  
        ax=0
        ay=-env.g

        bullet.x += bullet.vx*env.dt
        bullet.y += bullet.vy*env.dt

        bullet.vx += ax*env.dt
        bullet.vy += ay*env.dt
        
        bullet.x_points.append(bullet.x)
        bullet.y_points.append(bullet.y)

        if env.wall_x is not None:
            if bullet.x >= env.wall_x:
                if bullet.y <= env.wall_height:
                    hit_wall = True
                    break
        if env.target_x is not None:
            if bullet.x >= env.target_x:
                if bullet.y <= env.target_top and bullet.y >= env.target_bottom:
                    hit_target = True
                    break
        if env.ceiling_y is not None:
            if bullet.y >= env.ceiling_y:
                hit_ceiling = True
                break

    print(f"time of flight was {len(bullet.x_points)*env.dt:.2f}s")
    print(f"maximal height reached was {max(bullet.y_points):.2f}m")
    print(f"distance travelled is {bullet.x_points[-1]-bullet.x_points[0]:.2f}m")

    if hit_wall:
        print(f"colided with a wall at X: {env.wall_x:.2f}m Y: {bullet.y:.2f}m")
    if hit_target:
        print(f"colided with a target at X: {env.target_x:.2f}m Y: {bullet.y:.2f}m")
    if hit_ceiling:
        print(f"colided with a ceiling at X: {bullet.x:.2f}m Y: {env.ceiling_y}")
    return 0

def plot(bullet,env):
    plt.plot(bullet.x_points, bullet.y_points, color="green", linewidth=2,)

    plt.grid(True)

    plt.xlim(left=0, right=None)
    plt.ylim(bottom=0, top=None)

    if env.wall_x is not None:
        wall_x = [env.wall_x, env.wall_x]
        wall_y = [0, env.wall_height]
        plt.plot(wall_x, wall_y, color="red", linewidth=3)

    if env.target_x is not None:
        target_x = [env.target_x, env.target_x]
        target_y = [env.target_bottom, env.target_top]
        plt.plot(target_x, target_y, color="red", linewidth=3)

    if env.ceiling_y is not None:
        ceiling_x = [0, bullet.x_points[-1]+3]
        ceiling_y = [env.ceiling_y,env.ceiling_y]
        plt.plot(ceiling_x, ceiling_y, color="red", linewidth=3)
    #plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    env = initialize_environment()
    bullet = initialize()
    simulate(bullet, env)
    plot(bullet,env)