import numpy as np
from numpy.linalg import eig


def main(equation_example):
    left_side = []
    right_side = []

    elements = {}
    equations = []
    output = "Equations given \n"

    for i in equation_example:
        output += i + "\n"
        left, right = i.split("=>")
        left_elements = left.split("+")
        right_elements = right.split("+")
        equations.append([left_elements, right_elements])

        left_side.append(left_elements)
        right_side.append(right_elements)
        all_elements = left_elements + right_elements
        for j in all_elements:
            if j not in elements:
                elements[j] = "f" + str(len(elements) + 1)
    diffs_1 = differentials_1(elements=elements, equations=equations)
    diffs_2, diffs_3 = differentials_2(
        elements=elements, equations=equations, diffs_1=diffs_1
    )
    output += "\n\n############################################\n"
    for e in elements:
        output += elements[e] + " = " + e + "\n"
        # print(elements[e] + " = " + e)

    output += "\n\n############################################\n"
    for i in diffs_1:
        output += i + " = " + diffs_1[i] + "\n"
        # print(i + " = " + diffs_1[i])

    output += "\n\n############################################\n"

    output += print_differentials(diffs_2)
    output += "\n\n############################################\n"
    output += print_differentials(diffs_3)
    with open("output.txt", "w") as f:
        f.write(output)
    return (elements, diffs_1, diffs_2, diffs_3, output)


def print_differentials(diffs):
    output = ""
    for i in diffs:
        statement = i + " = "
        for j in diffs[i][0]:
            statement += " - " + j
        for j in diffs[i][1]:
            statement += " + " + j
        # print(statement)
        output += statement + "\n"
    return output


def differentials_1(elements, equations):
    output = {}
    for i in range(len(equations)):
        n = i + 1
        o = "K" + str(n) + "*"
        for j in equations[i][0]:
            o += elements[j] + "*"
        o = o[:-1]
        output["R" + str(n)] = o
    # print(output)
    return output


def differentials_2(elements, equations, diffs_1):
    diffs_2 = {}
    turn = 1
    for e in elements:
        k = "F" + str(turn)
        lefts = []
        rights = []
        for i in range(len(equations)):
            for element in equations[i][0]:
                if len(element) == 1 and element == e:
                    lefts.append("R" + str(i + 1))
            for element in equations[i][1]:
                if len(element) == 1 and element == e:
                    rights.append("R" + str(i + 1))
        v = [lefts, rights]
        diffs_2[k] = v
        turn += 1
    diffs_3 = {}
    for i in diffs_2:
        k = i
        lefts = []
        rights = []
        for j in diffs_2[i][0]:
            lefts.append(diffs_1[j])
        for j in diffs_2[i][1]:
            rights.append(diffs_1[j])

        v = [lefts, rights]
        diffs_3[k] = v

    return (diffs_2, diffs_3)


def solve_for_graph(elements, diffs_1, diffs_2, diffs_3, output):
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    vac, val = eig(mat)
    # print(mat)


# if __name__ == "__main__":
#     # a==x
#     # x+y==x
#     # b+x==y+c
#     # x==d
#     equation_example = ["a=>x", "x+y=>x", "b+x=>y+c", "x=>d"]
#     # a+b==c
#     # c+a==d+a
#     # b+d==a
#     equation_example = ["a+b=>c", "c+a=>d+a", "b+d=>a"]
#     # a+s==>b+c+d
#     # s+a+b==>f+e+g+h
#     equation_example = ["a+s=>b+c+d", "s+a+b=>f+e+g+h"]
#     output = main(equation_example=equation_example)

#     with open("output.txt", "w") as f:
#         f.write(output)
