from itertools import permutations

solution = [0, 1, 2, 3, 4, 5, 6, 7, 8]

with open("wordlist.txt", "w") as file:
    file.write("[")
    for r in range(1, len(solution) + 1):  # from 1 to 9
        for payload in permutations(solution, r):
            file.write(",".join(map(str, payload)) + " ")
    file.write("]")



