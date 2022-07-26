import math

lines: list = [[[1, -1], [1, 1]], [[2, -1], [2, 1]], [[-1, 4], [1, 4]]]
x_point: int = int(input("Enter the x-coordinate of your point : "))
y_point: int = int(input("Enter the y-coordinate of your point : "))
print(f'The starting point given is ({x_point}, {y_point}).')
angle: int = int(input("Please enter the angle of your line : "))

distance: list = []


def distance_between_point_and_line(st_point, en_point) -> tuple[list, float] | None:
    try:
        a = en_point[1] - st_point[1]  # y2-y1
        b = en_point[0] - st_point[0]  # x2-x1
        if (a == 0 and angle == 0) or (angle == 90 and b == 0):
            return
        elif b != 0:
            slope = a / b
            c = st_point[1] - (slope * st_point[0])
            slope_origin = math.tan(math.radians(angle))
            x_intercept = round(c / (slope_origin - slope), 2)
            y_intercept = round(slope * x_intercept + c, 2)
        else:
            x_intercept = st_point[0]  # x1
            slope_origin = (math.tan(math.radians(angle)))
            y_intercept = slope_origin * x_intercept
    except Exception:
        print("Some Exception Occurred !!!")
    if min(st_point[0], en_point[0]) <= x_intercept <= max(st_point[0], en_point[0]) and min(st_point[1], en_point[1]) <= \
            y_intercept <= max(st_point[1], en_point[1]):
        return [st_point, en_point], round(math.dist((x_point, y_point), (x_intercept, y_intercept)), 2)


for l in lines:
    P, Q = l
    val = distance_between_point_and_line(P, Q)
    distance.append(val)

distance_array = list(filter(None, distance))

if len(distance_array) != 0:
    nearest_line = min(distance_array, key=lambda t: t[0])
    print(f'The nearest line segment from ({x_point},{y_point}) at the angle of {angle} degree is'
          f' {nearest_line[0]}.')
else:
    print(f'There are no line segment found from ({x_point},{y_point}) at the angle of {angle} degree.')
