import math
    
def solution(dimensions, your_position, trainer_position, distance):
    x_dim = dimensions[0]
    y_dim = dimensions[1]
    x_src = your_position[0]
    y_src = your_position[1]
    x_dst = trainer_position[0]
    y_dst = trainer_position[1]

    self_mirrors = []
    guard_mirrors = []
    dist = lambda x0, y0, x1, y1 : math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    for y_room in range((distance // y_dim) + 2):
        if y_room % 2:
            your_y = y_room * y_dim + y_dim - y_src
            guard_y = y_room * y_dim + y_dim - y_dst
        else:
            your_y = y_room * y_dim + y_src
            guard_y = y_room * y_dim + y_dst
        for x_room in range((distance // x_dim) + 2):
            if x_room % 2:
                your_x = x_room * x_dim + x_dim - x_src
                guard_x = x_room * x_dim + x_dim - x_dst
            else:
                your_x = x_room * x_dim + x_src
                guard_x = x_room * x_dim + x_dst
            for x, y in ((your_x, your_y), (-your_x, your_y), (your_x, -your_y), (-your_x, -your_y)):
                if 0 < dist(x_src, y_src, x, y) <= distance:
                    self_mirrors.append((x, y))
            for x, y in ((guard_x, guard_y), (-guard_x, guard_y), (guard_x, -guard_y), (-guard_x, -guard_y)):
                if 0 < dist(x_src, y_src, x, y) <= distance:
                    guard_mirrors.append((x, y))

    self_mirrors.sort(key=lambda self_mirror: dist(x_src, y_src, self_mirror[0], self_mirror[1]))
    guard_mirrors.sort(key=lambda guard_mirror: dist(x_src, y_src, guard_mirror[0], guard_mirror[1]))

    self_angles = {}
    for x, y in self_mirrors:
        angle = math.atan2(y - y_src, x - x_src)
        if angle not in self_angles:
            self_angles[angle] = (x, y)

    result = 0
    shot_angles = set()

    for x, y in guard_mirrors:
        angle = math.atan2(y - y_src, x - x_src)
        if angle in shot_angles:
            continue
        if angle not in self_angles or dist(x_src, y_src, x, y) < dist(x_src, y_src, self_angles[angle][0], self_angles[angle][1]):
            shot_angles.add(angle)
            result += 1
    return result
