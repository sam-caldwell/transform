# file: rotate_and_plot_int.py
import numpy as np
import matplotlib.pyplot as plt

def rotation_matrix_int(angle: int) -> np.ndarray:
    """
    Return a 2×2 integer rotation matrix for angle ∈ {0, 90, 180, 270} degrees.

    Parameters:
        angle (int): Rotation angle in degrees (must be multiple of 90).

    Returns:
        np.ndarray: 2×2 integer rotation matrix.
    """
    angle_mod = angle % 360
    if angle_mod == 0:
        R = np.array([[1, 0],
                      [0, 1]], dtype=int)
    elif angle_mod == 90:
        R = np.array([[0, -1],
                      [1,  0]], dtype=int)
    elif angle_mod == 180:
        R = np.array([[-1,  0],
                      [ 0, -1]], dtype=int)
    elif angle_mod == 270:
        R = np.array([[ 0, 1],
                      [-1, 0]], dtype=int)
    else:
        raise ValueError("Angle must be 0, 90, 180, or 270")
    print("Rotation matrix R (integers):")
    print(R)
    return R

def apply_transformation_int(points: np.ndarray, transform: np.ndarray) -> np.ndarray:
    """
    Apply an integer linear transformation to integer points.

    Parameters:
        points (np.ndarray): N×2 integer array of (x, y).
        transform (np.ndarray): 2×2 integer matrix.

    Returns:
        np.ndarray: N×2 integer array of transformed points.
    """
    P = points.T  # shape 2×N
    print("Original points matrix P:")
    print(P)
    P_rot = transform @ P
    print("Transformed points matrix P_rot:")
    print(P_rot)
    return P_rot.T

def enter_points_int() -> np.ndarray:
    """
    Prompt for integer points until empty input.

    Returns:
        np.ndarray: N×2 integer array.
    """
    pts = []
    while True:
        s = input("Enter integer x,y (empty to finish): ").strip()
        if not s:
            break
        try:
            x_str, y_str = s.split(',')
            x = int(x_str)
            y = int(y_str)
            pts.append((x, y))
        except ValueError:
            print("Invalid input. Enter two whole numbers separated by a comma.")
    return np.array(pts, dtype=int)

def main():
    """
    Read integer points and 90°-multiple rotation angle, transform, and plot.
    """
    pts = enter_points_int()
    if pts.size == 0:
        print("No points entered. Exiting.")
        return

    # close shape
    pts = np.vstack([pts, pts[0]])

    angle_str = input("Enter rotation angle (0, 90, 180, 270): ").strip()
    try:
        angle = int(angle_str)
    except ValueError:
        print("Invalid angle. Exiting.")
        return

    R = rotation_matrix_int(angle)
    rotated_pts = apply_transformation_int(pts, R)

    xs, ys = pts[:,0], pts[:,1]
    xs_r, ys_r = rotated_pts[:,0], rotated_pts[:,1]

    plt.figure()
    plt.plot(xs, ys, '-o', label='Original')
    plt.plot(xs_r, ys_r, '-o', label=f'Rotated by {angle}°')
    plt.axis('equal')
    plt.title("Integer Rotation by multiples of 90°")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
