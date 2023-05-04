from django.shortcuts import render
import math

# import redirect
from django.shortcuts import redirect

# Create your views here.
# import model Chemical_Reaction
from .models import Chemical_Reaction
import chemical.solve_equation as solve_equation

# from .utils import equation_to_graph


def contact_view(request):
    return render(request, "contact.html", {})


def home(request):
    all_reactions = Chemical_Reaction.objects.all()
    context = {"reactions": all_reactions}

    return render(request, "home.html", context)


import numpy as np
import matplotlib.pyplot as plt


def equation_to_graph(params, elements, diffs_1, diffs_2, diffs_3):
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

    # equations
    x_eqation = diffs_3["x"]
    y_eqation = diffs_3["y"]
    z_eqation = diffs_3["z"]

    # initial values
    x_init = float(params["x"])
    y_init = float(params["y"])
    z_init = float(params["z"])

    print(x_eqation, y_eqation, z_eqation)
    parameters_dict = {}
    # Define the time step and the number of iterations
    h = 0.1
    num_iterations = 100

    # Initialize the arrays to store the values of x, y, z, and others at each interval
    array_of_values = []
    for v in range(len(diffs_3)):
        array_of_values.append([])
    # print(array_of_values)
    coefficients = []
    parameters_dict = {}
    for i in params.keys():
        if i != "csrfmiddlewaretoken":
            parameters_dict[i] = float(params[i])
    initial_values = []

    # define constants in the equation as 1
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
        #     dzdt = k1 * c[i]
        new_values = []
        # x_new = x + h * (-K1 * x * y + K2 * c)
        # y_new = y + h * (-K1 * x * y)
        # c_new = c + h * (-K2 * c + K1 * x * y)
        # z_new = z + h * (K2 * c)
        x_new_val = x_init + eval(x_eqation, parameters_dict) * h
        y_new_val = y_init + eval(y_eqation, parameters_dict) * h
        z_new_val = z_init + eval(z_eqation, parameters_dict) * h

        # update initial values
        x_init = x_new_val
        y_init = y_new_val
        z_init = z_new_val
        # update parameters_dict
        parameters_dict["x"] = x_init
        parameters_dict["y"] = y_init
        parameters_dict["z"] = z_init

        # Append the values to the arrays
        array_of_values[0].append(x_new_val)
        array_of_values[1].append(y_new_val)
        array_of_values[2].append(z_new_val)
        h += 0.1

    print("dict of params", parameters_dict)
    x_array = array_of_values[0]
    print(x_array)
    y_array = array_of_values[1]
    print(y_array)
    z_array = array_of_values[2]
    print(z_array)
    # Plot the results
    # import matplotlib.pyplot as plt

    # plt.style.use("seaborn-v0_8-poster")
    # fig = plt.figure(figsize=(10, 10))
    # ax = plt.axes(projection="3d")
    # ax.grid()
    # ax.plot3D(x_array, y_array, z_array)
    # ax.set_title("3D Parametric Plot")

    # # Set axes label
    # ax.set_xlabel("x", labelpad=20)
    # ax.set_ylabel("y", labelpad=20)
    # ax.set_zlabel("z", labelpad=20)

    # igure, exaes = plt.subplots(3, 1)
    # ts = np.arange(0, 1000, 0.1)
    # exaes[0].plot(ts, x_array[:100])
    # # set the axes labels
    # exaes[0].set_xlabel("t")
    # exaes[0].set_ylabel("x")
    # exaes[1].plot(ts, y_array)
    # # set the axes labels
    # exaes[1].set_xlabel("t")
    # exaes[1].set_ylabel("y")
    # exaes[2].plot(ts, z_array[:100])
    # # set the axes labels
    # exaes[2].set_xlabel("t")
    # exaes[2].set_ylabel("z")

    # plt.plot(x_array, y_array, z_array)
    # plt.show()
    # plt.savefig("3d_plot.png")
    # plt.subplot(211)
    # plt.plot(
    #     x_array,
    #     np.arange(0, 10, 0.1),
    # )
    # plt.savefig("2d_plot_x.png")
    # plt.subplot(211)
    # plt.plot(
    #     y_array,
    #     np.arange(0, 10, 0.1),
    # )
    # plt.savefig("2d_plot_y.png")
    # plt.subplot(211)
    # plt.plot(
    #     z_array,
    #     np.arange(0, 10, 0.1),
    # )
    # plt.savefig("2d_plot_z.png")

    # ax.savefig("templates/plot.png")


def show_reaction_description_view(request, reaction_id):
    reaction_equation = Chemical_Reaction.objects.get(id=reaction_id)
    context = {}

    context["equation"] = reaction_equation.reactants
    equations = reaction_equation.reactants.split(" ")
    elements, diffs_1, diffs_2, diffs_3, output = solve_equation.main(equations)
    f_to_elements = {}
    for k, v in elements.items():
        f_to_elements[v] = k

    print(f_to_elements)
    print(diffs_1)
    print(diffs_2)
    print(diffs_3)
    print(output)

    if request.method == "POST":
        coefficients = {}
        elems = request.POST
        print(elems)
        elems = elems.dict()

        equation_to_graph(
            elems,
            elements,
            diffs_1,
            diffs_2,
            diffs_3,
        )
        # reverse the elements dict
        print("elements", elements)

    context["elements"] = elements
    context["output"] = output
    elements_2 = {}
    for k, v in elements.items():
        elements_2[v] = k
    print(elements_2)
    for k, v in elements_2.items():
        elements[k] = v

    print("ELEMENETS", elements)
    # diffs_1 manipulation
    r_d = {}
    for i in diffs_1:
        l = i.lower()
        all = ""
        elems = diffs_1[i].split("*")
        for a in elems:
            all += a[0] + "_" + a[1] + " * "

        r_d[i[0] + "_" + i[1]] = all[:-2]

    context["diffs_1"] = r_d

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
    context["diffs_2"] = r_d

    # diffs_3 manipulation
    for i in diffs_3:
        row = diffs_3[i]
        for j in range(len(row[0])):
            s = row[0][j].split("*")
            m = s[1:]
            for k in range(len(m)):
                m[k] = "[" + elements[m[k]] + "]"
            a = [s[0][0] + "_" + s[0][1]] + m
            a = "*".join(a)
            row[0][j] = a
        for j in range(len(row[1])):
            s = row[1][j].split("*")
            m = s[1:]
            for k in range(len(m)):
                m[k] = "[" + elements[m[k]] + "]"
            a = [s[0][0] + "_" + s[0][1]] + m
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

    print("diffs 3 ", diffs_3)
    context["diffs_3"] = diffs_3
    context["reaction_id"] = reaction_id
    return render(request, "show_reaction.html", context)


def create_reactions_view(request):
    if request.method == "POST":
        data = request.POST
        # reactions = data["reaction"].split(" ")
        # print(reactions)
        # diffs = solve_equation.main(reactions)
        reaction = Chemical_Reaction.objects.create(reactants=data["reaction"])
        reaction.save()
        return redirect("show_reaction", reaction.id)

    return render(request, "create_reactions.html", {})
