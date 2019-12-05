import numpy as np 
import matplotlib.pyplot as plt

def minimum_jerk_trajectory(init_pos, target_pos, total_time=0.5, dt=0.01):
    xi = init_pos
    xf = target_pos
    d = total_time
    list_t = []
    list_x = []
    t = 0
    while t < d:
        x = xi + (xf-xi) * (10*(t/d)**3 - 15*(t/d)**4 + 6*(t/d)**5)
        list_t.append(t)
        list_x.append(x)
        t += dt
    return np.array(list_t), np.array(list_x)

def main():
    print("Minimum Jerk Trajectory Generator")
    # This is initial position of servo motor
    init_pos = np.array([np.radians(0), np.radians(30), np.radians(20), np.radians(50)])
    # This is target position of servo motor
    target_pos = np.array([np.radians(50), np.radians(0), np.radians(50), np.radians(-20)])
    # We want to move all joint from initial to target position in 1 seconds
    t, x = minimum_jerk_trajectory(init_pos, target_pos, total_time=1.0)
    # Show the result
    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set_title("Minimum Jerk Trajectory")
    ax.set_xlabel("Time")
    ax.set_ylabel("Position")
    plt.show()
    
if __name__ == "__main__":
    main()