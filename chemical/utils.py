import numpy as np
import matplotlib.pyplot as plt


def equation_to_graph(elements, diffs_1, diffs_2, diffs_3):
    elem = []

    # store keys in elements
    print()
    for k, v in elements.items():
        elem.append(k)
    # reverse elements
    elements = {v: k for k, v in elements.items()}

    # diffs_1 manipulation
    r_d = {}
    for i in diffs_1:
        l = i.lower()
        all = ""
        elems = diffs_1[i].split("*")
        for a in elems:
            all += a[0] + "_" + a[1] + " * "

        r_d[i[0] + "_" + i[1]] = all[:-2]

    # diffs_2 manipulation
    r_d = {}
    for i in diffs_2:
        row = diffs_2[i]
        all = ""
        for a in row[0]:
            all += " - " + a[0] + "_" + a[1]
        for a in row[1]:
            all += " + " + a[0] + "_" + a[1]

        r_d[elements[i.lower()]] = all

    # diffs_3 manipulation
    for i in diffs_3:
        row = diffs_3[i]
        for j in range(len(row[0])):
            s = row[0][j].split("*")
            m = s[1:]
            for k in range(len(m)):
                m[k] = elements[m[k]]
            a = [s[0][0] + s[0][1]] + m
            a = "*".join(a)
            row[0][j] = a
        for j in range(len(row[1])):
            s = row[1][j].split("*")
            m = s[1:]
            for k in range(len(m)):
                m[k] = elements[m[k]]
            a = [s[0][0] + s[0][1]] + m
            a = "*".join(a)
            row[1][j] = a

    diffs_4 = {}
    for i in diffs_3:
        row = diffs_3[i]
        all = ""
        for a in row[0]:
            all += " - " + a
        for a in row[1]:
            all += " + " + a

        diffs_4[elements[i.lower()]] = all
    diffs_3 = diffs_4

    print(elem)
    print(diffs_3)

    # Define the parameters
    parameters_dict = {}
    starting = 1
    for i in range(len(diffs_3)):
        parameters_dict["K" + str(starting)] = starting * 0.1
        starting += 1
    print(parameters_dict)
    # Define the initial values
    initial_values = []
    for i in range(len(diffs_3)):
        initial_values.append(0.25)
        parameters_dict[elem[i]] = 0.25

    # Define the time step and the number of iterations
    h = 0.1
    num_iterations = 10000

    # Initialize the arrays to store the values of x, y, z, and others at each interval
    array_of_values = []
    for v in range(len(diffs_3)):
        array_of_values.append([])
    print(array_of_values)
    coefficients = []

    # Apply the Euler method
    for i in range(num_iterations):
        new_values = []
        # x_new = x + h * (-K1 * x * y + K2 * c)
        # y_new = y + h * (-K1 * x * y)
        # c_new = c + h * (-K2 * c + K1 * x * y)
        # z_new = z + h * (K2 * c)
        for v in range(len(diffs_3)):
            new_val = initial_values[v] + eval(diffs_3[elem[v]], parameters_dict) * h

            new_values.append(new_val)

        # x = x_new
        # y = y_new
        # c = c_new
        # z = z_new
        for i in range(len(initial_values)):
            initial_values[i] = new_values[i]
            parameters_dict[elem[i]] = new_values[i]
            array_of_values[i].append(new_values[i])

    x_array = array_of_values[elem.index("x")]
    # print(x_array)
    y_array = array_of_values[elem.index("y")]
    # print(y_array)

    z_array = array_of_values[elem.index("z")]
    # print(z_array)
    # Plot the results
    import matplotlib.pyplot as plt

    plt.style.use("seaborn-v0_8-poster")
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection="3d")
    ax.grid()
    ax.plot3D(x_array, y_array, z_array)
    ax.set_title("3D Parametric Plot")

    # Set axes label
    ax.set_xlabel("x", labelpad=20)
    ax.set_ylabel("y", labelpad=20)
    ax.set_zlabel("z", labelpad=20)
    ax.show()
    # ax.savefig("templates/plot.png")
