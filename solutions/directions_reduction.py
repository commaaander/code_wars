# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
# Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the
# wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you
# might die of thirst!

# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
# So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

# ["WEST"]
# or
# { "WEST" }
# or
# [West]
# Other examples:
# In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is []
# (nil in Clojure).

# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become
# directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

# Task
# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless
# directions removed (W<->E or S<->N side by side).

# The Haskell version takes a list of directions with data Direction = North | East | West | South.
# The Clojure version returns nil when the path is reduced to nothing.
# The Rust version takes a slice of enum Direction {North, East, West, South}.
# See more examples in "Sample Tests:"
# Notes
# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST",
# "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the
# result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
# if you want to translate, please ask before translating.


from typing import List

import codewars_test as test  # type: ignore


def dir_reduc(arr: List[str]) -> List[str]:
    result: List[str] = []
    needless_directions: List[List[str]] = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["WEST", "EAST"], ["EAST", "WEST"]]

    return result


def valid_braces(string: str) -> bool:
    while True:
        new_string = string
        for brace_pair in ["()", "[]", "{}"]:
            new_string = new_string.replace(brace_pair, "")
        if new_string == string:
            break
        string = new_string
    return string == ""


if __name__ == "__main__":
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    test.assert_equals(dir_reduc(a), ["WEST"])
    a = ["NORTH", "WEST", "SOUTH", "EAST"]
    test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # ['WEST']
    test.assert_equals(dir_reduc(a), ["WEST"])
    a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST", "EAST"]  # ['NORTH', 'NORTH']
    test.assert_equals(dir_reduc(a), ["NORTH", "NORTH"])
    a = []  # []
    test.assert_equals(dir_reduc(a), [])
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]  # []
    test.assert_equals(dir_reduc(a), [])
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"]  # ["NORTH"]
    test.assert_equals(dir_reduc(a), ["NORTH"])
    a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"]  # ["EAST", "NORTH"]
    test.assert_equals(dir_reduc(a), ["EAST", "NORTH"])
    a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"]  # ["NORTH", "EAST"])
    test.assert_equals(dir_reduc(a), ["NORTH", "EAST"])
    a = ["NORTH", "WEST", "SOUTH", "EAST"]  # ["NORTH", "WEST", "SOUTH", "EAST"])
    test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
    a = ["NORTH", "NORTH", "EAST", "SOUTH", "EAST", "EAST", "SOUTH", "SOUTH", "SOUTH", "NORTH"]
    test.assert_equals(dir_reduc(a), ["NORTH", "NORTH", "EAST", "SOUTH", "EAST", "EAST", "SOUTH", "SOUTH"])
