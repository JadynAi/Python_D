import helper
import random

env_data = helper.fetch_maze()

loc_map = {}
key_start = 'start'
key_des = 'destination'
for index, value in enumerate(env_data, 1):
    if key_start not in loc_map or key_des not in loc_map:
        if 1 in value:
            loc_map[key_start] = (index, value.index(1) + 1)
        if 3 in value:
            loc_map[key_des] = (index, value.index(3) + 1)
    else:
        break

robot_current_loc = loc_map[key_start]

# 上下左右四个移动命令
orders = ['u', 'd', 'l', 'r']


def is_move_valid(loc, act):
    """
    判断当前点，是否可使用此移动命令
    """
    x = loc[0] - 1
    y = loc[1] - 1
    if act not in orders:
        return false
    else:
        if act == orders[0]:
            return x != 0 and env_data[x - 1][y] != 2
        elif act == orders[1]:
            return x != len(env_data) - 1 and env_data[x + 1][y] != 2
        elif act == orders[2]:
            return y != 0 and env_data[x][y - 1] != 2
        else:
            return y != len(env_data[0]) - 1 and env_data[x][y + 1] != 2


def valid_actions(loc):
    """
    :param loc:
    :return: 当前位置所有可用的命令
    """
    loc_actions = []
    for order in orders:
        if is_move_valid(loc, order):
            loc_actions.append(order)
    return loc_actions


def move_robot(loc, act):
    """
    移动机器人，返回新位置
    :param loc:
    :param act:
    :return:
    """
    if is_move_valid(loc, act):
        if act == orders[0]:
            return loc[0] - 1, loc[1]
        elif act == orders[1]:
            return loc[0] + 1, loc[1]
        elif act == orders[2]:
            return loc[0], loc[1] - 1
        else:
            return loc[0], loc[1] + 1
    else:
        return loc


def random_choose_actions(loc):
    for i in range(300):
        valid_acts = valid_actions(loc)
        act = random.choice(valid_acts)
        loc = move_robot(loc, act)
        if loc == loc_map[key_des]:
            print('在第{}个回合找到宝藏!'.format(i + 1))
            break


random_choose_actions(robot_current_loc)
