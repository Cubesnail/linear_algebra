pAffected = {

    # pieces affected (val of dict) are the pieces that are affected when a move (key of dict) is made.
    # It is set up so that for list [x1, x2, x3, x4]:
    #     x1 -> x2 -> x3 -> x4 -> x1
    # Observe closely that it is also set up such that the rotation of the corners follow:
    #     x1:CCW || x2:CW || x3:CCW || x4:CW
    # after the permutation has occured (that is, permutations should be made then cubies oriented).


    "R": [3, 4, 8, 7],
    "L": [2, 1, 5, 6],
    "U": [1, 2, 4, 3],
    "D": [5, 7, 8, 6],
    "F": [1, 3, 7, 5],
    "B": [4, 2, 6, 8],
    "R'": [3, 7, 8, 4],
    "L'": [2, 6, 5, 1],
    "U'": [1, 3, 4, 2],
    "D'": [5, 6, 8, 7],
    "F'": [1, 5, 7, 3],
    "B'": [4, 8, 6, 2],
}
pAffected = {

    # pieces affected (val of dict) are the pieces that are affected when a move (key of dict) is made.
    # It is set up so that for list [x1, x2, x3, x4]:
    #     x1 -> x2 -> x3 -> x4 -> x1
    # Observe closely that it is also set up such that the rotation of the corners follow:
    #     x1:CCW || x2:CW || x3:CCW || x4:CW
    # after the permutation has occured (that is, permutations should be made then cubies oriented).


    "R": [3, 4, 8, 7],
    "L": [2, 1, 5, 6],
    "U": [1, 2, 4, 3],
    "D": [5, 7, 8, 6],
    "F": [1, 3, 7, 5],
    "B": [4, 2, 6, 8],
    "R'": [3, 7, 8, 4],
    "L'": [2, 6, 5, 1],
    "U'": [1, 3, 4, 2],
    "D'": [5, 6, 8, 7],
    "F'": [1, 5, 7, 3],
    "B'": [4, 8, 6, 2],
}