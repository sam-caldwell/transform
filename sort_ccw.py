#!/usr/bin/env python3
#
# A program to sort ordered pairs counter-clockwise
#
import math


def sort_ccw(points:list[tuple[float]]):
    """
    Sorts a list of (x, y) tuples in counterclockwise order around their centroid.

    Args:
        points (list of tuple of float): List of (x, y) pairs.

    Returns:
        list of tuple of float: The same points sorted CCW.
    """
    # Compute centroid of the points
    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)

    # Compute angle of each point relative to centroid
    def angle_from_centroid(point):
        x, y = point
        return math.atan2(y - cy, x - cx)

    # Sort by angle
    return  sorted(points, key=angle_from_centroid)


if __name__ == "__main__":
    unsorted_points = []
    print("Enter ordered pairs as 'x,y'. Leave blank and press Enter to finish.")

    while True:
        s = input("Enter x,y (or blank to finish): ").strip()
        if s == "":
            break
        try:
            x_str, y_str = s.split(",")
            x = float(x_str)
            y = float(y_str)
            unsorted_points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter in the format x,y without spaces.")

    if unsorted_points:
        sorted_points = sort_ccw(unsorted_points)
        print("\nOriginal list of points:")
        for pt in unsorted_points:
            print(f"  {pt}")

        print("\nPoints sorted CCW around centroid:")
        for pt in sorted_points:
            print(f"  {pt}")
    else:
        print("No points were entered.")
