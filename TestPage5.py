def longest_slide_down(pyramid):
    deep = 4
    total = 0
    start = 0
    stop = 1
    for level in range(0, len(pyramid), deep):
        variants = []
        # print("level =", level)
        curr = pyramid[level: level + deep]

        if len(curr) < deep:
            for i in range(1, deep + 1 - len(curr)):
                curr.append([0] * (len(curr[len(curr)-1])+1))

        # print("curr = ", curr)
        for a in range(start, stop):
            for b in range(a, a + 2):
                for c in range(b, b + 2):
                    for d in range(c, c + 2):
                        sum = curr[0][a] + curr[1][b] + curr[2][c] + curr[3][d]
                        variant = {"a": a, "b": b, "c": c, "d": d, "sum": sum}
                        variants.append(variant)
        # print(variants)
        max_path = max(variants, key=lambda k: k["sum"])
        # print(max_path)
        start = max_path["d"]
        stop = start + 2
        total += max_path["sum"]
        # print("a =", curr[0][max_path["a"]], "b =", curr[1][max_path["b"]], "c =", curr[2][max_path["c"]],
        #       "d =", curr[3][max_path["d"]], "sum=", max_path["sum"])
        # print("d =", max_path["d"], "sum=", max_path["sum"])

    return total


print(longest_slide_down([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]))
