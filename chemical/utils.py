import numpy as np
import matplotlib.pyplot as plt
import random
from solve_equation import main


def equation_to_graph(elements, diffs_1, diffs_2, diffs_3):
    elem = []

    # store keys in elements
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

    # print(elem)
    # print(diffs_3)

    # Define the parameters
    parameters_dict = {}

    # print(parameters_dict)
    # Define the initial values

    # Define the time step and the number of iterations
    h = 0.1
    num_iterations = 100

    # Initialize the arrays to store the values of x, y, z, and others at each interval
    array_of_values = []
    for v in range(len(diffs_3)):
        array_of_values.append([])
    # print(array_of_values)
    coefficients = []
    vv = 0.01
    for i in range(100):
        parameters_dict = {}
        initial_values = []
        for i in range(len(diffs_3)):
            initial_values.append(vv)
            parameters_dict[elem[i]] = vv

        starting = 1
        for i in range(len(diffs_3)):
            parameters_dict["K" + str(starting)] = 1
            starting += 1
        print(parameters_dict)
        # Apply the Euler method
        for i in range(num_iterations):
            # Calculate the derivatives
            #     dxdt = -k1 * x[i] * y[i] + k2 * c[i]
            #     dydt = -k1 * x[i] * y[i]
            #     dcdt = -k2 * c[i] + k1 * x[i] * y[i]
            #     dzdt = k1 * c[i]
            # derivetives = []
            # for v in range(len(diffs_3)):

            new_values = []
            # x_new = x + h * (-K1 * x * y + K2 * c)
            # y_new = y + h * (-K1 * x * y)
            # c_new = c + h * (-K2 * c + K1 * x * y)
            # z_new = z + h * (K2 * c)
            for v in range(len(diffs_3)):
                new_val = (
                    initial_values[v] + eval(diffs_3[elem[v]], parameters_dict) * h
                )

                new_values.append(new_val)

            # x = x_new
            # y = y_new
            # c = c_new
            # z = z_new
            for i in range(len(initial_values)):
                initial_values[i] = new_values[i]
                parameters_dict[elem[i]] = new_values[i]
                array_of_values[i].append(new_values[i])
        vv += 0.1

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

    # plt.plot(x_array, y_array, z_array)
    plt.show()
    # ax.savefig("templates/plot.png")
    return (x_array, y_array, z_array)


# euqation = a=>x x+y=>x b+x=>y+c x=>d
elements, diffs_1, diffs_2, diffs_3, output = main(
    equation_example=["a=>x", "x+y=>x", "b+x=>z+c", "x=>d"]
)
equation_to_graph(elements, diffs_1, diffs_2, diffs_3)


def range_kutta(elements, diffs_1, diffs_2, diffs_3):
    pass


def rk4(f, t0, x0, h, t_end):
    """
    Solve the initial value problem x' = f(t,x) using the fourth-order Runge-Kutta method.

    Parameters:
        f: the derivative function f(t,x), which takes a scalar time t and a vector x of length n
           and returns a vector of length n
        t0: the initial time
        x0: the initial state, which is a vector of length n
        h: the time step size
        t_end: the end time

    Returns:
        t: a 1D NumPy array of times at which the solution was evaluated
        x: a 2D NumPy array of states, where the ith row is the state at time t[i]
    """
    n = len(x0)
    t = np.arange(t0, t_end + h, h)
    x = np.zeros((len(t), n))
    x[0] = x0

    for i in range(len(t) - 1):
        k1 = f(t[i], x[i])
        k2 = f(t[i] + h / 2, x[i] + h / 2 * k1)
        k3 = f(t[i] + h / 2, x[i] + h / 2 * k2)
        k4 = f(t[i] + h, x[i] + h * k3)
        x[i + 1] = x[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return t, x


# # Set the initial values and time step
# x0 = y0 = z0 = c0 = 0.25
# dt = 0.01

# # Set the values of k1 and k2
# k1 = k2 = 1

# # Initialize the arrays to store the values of x, y, c, and z
# x = [x0]
# y = [y0]
# c = [c0]
# z = [z0]

# # Loop over the time steps
# for i in range(1000):
#     # Calculate the derivatives
#     dxdt = -k1 * x[i] * y[i] + k2 * c[i]
#     dydt = -k1 * x[i] * y[i]
#     dcdt = -k2 * c[i] + k1 * x[i] * y[i]
#     dzdt = k1 * c[i]

#     # Calculate the new values of x, y, c, and z using Euler's method
#     x_new = x[i] + dxdt * dt
#     y_new = y[i] + dydt * dt
#     c_new = c[i] + dcdt * dt
#     z_new = z[i] + dzdt * dt

#     # Append the new values to the arrays
#     x.append(x_new)
#     y.append(y_new)
#     c.append(c_new)
#     z.append(z_new)
