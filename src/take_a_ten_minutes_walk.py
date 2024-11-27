# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early
# to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens
# with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter
# strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each
# letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will
# return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
# and will, of course, return you to your starting point.
# Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters
# ('n', 's', 'e', or 'w' only).
# It will never give you an empty array (that's not a walk, that's standing still!).


def is_valid_walk(walk) -> bool:
    walk_duration = 10
    cur_walk_step = 0
    pos_x = 0
    pos_y = 0
    ret_val = False

    if len(walk) != walk_duration:
        return ret_val

    while cur_walk_step < walk_duration:
        if walk[cur_walk_step] == "n":
            pos_x += 1
        elif walk[cur_walk_step] == "e":
            pos_y += 1
        elif walk[cur_walk_step] == "s":
            pos_x -= 1
        elif walk[cur_walk_step] == "w":
            pos_y -= 1
        cur_walk_step += 1

    ret_val = pos_x == 0 and pos_y == 0
    return ret_val
