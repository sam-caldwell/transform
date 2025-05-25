# file: rotate_and_plot.py
import math
import matplotlib.pyplot as plt


def rotate_points(points:list, theta:float):
    """
    Rotate a list of 2D points by angle theta (radians).

    Parameters:
        points (list of tuple of float): List of (x, y) coordinates.
        theta (float): Rotation angle in radians.

    Returns:
        list of tuple of float: Rotated (x, y) coordinates.
    """
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    rotated = []
    for x, y in points:
        x_new = x * cos_t - y * sin_t
        y_new = x * sin_t + y * cos_t
        rotated.append((x_new, y_new))
    return rotated

def enter_points()->list:
    points = []
    while True:
        s = input("Enter x,y (empty to finish): ").strip()
        if s == "":
            break
        try:
            x_str, y_str = s.split(',')
            x = float(x_str)
            y = float(y_str)
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")
    return points


def main():
    """
    Prompt the user to enter ordered pairs until an empty input is given,
    then prompt for a rotation angle in degrees, and plot the original points
    in blue and the rotated points in red.
    """
    points = enter_points()

    if not points:
        print("No points entered. Exiting.")
        return

    # connect the last point to the first point
    points.append(points[0])

    angle_str = input("Enter rotation angle in degrees: ").strip()
    try:
        angle_deg = float(angle_str)
    except ValueError:
        print("Invalid angle. Exiting.")
        return

    angle = math.radians(angle_deg)
    rotated = rotate_points(points, angle)

    xs, ys = zip(*points)
    xs_r, ys_r = zip(*rotated)

    plt.figure()
    plt.plot(xs, ys, '-o', color='blue', label='Original')
    plt.plot(xs_r, ys_r, '-o', color='red', label='Rotated')
    plt.axis('equal')
    plt.title(f"Original (blue) and Rotated (red) by {angle_deg:.1f}°")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
