from django.shortcuts import render
import math

# Create your views here.
# import model Chemical_Reaction
from .models import Chemical_Reaction
import solve_equation


def home(request):

    all_reactions = Chemical_Reaction.objects.all()
    context = {"reactions": all_reactions}

    return render(request, "base.html", context)


def show_reaction_description_view(request, reaction_id):
    reaction_equation = Chemical_Reaction.objects.get(id=reaction_id)
    context = {}

    context["equation"] = reaction_equation.reactants
    equations = reaction_equation.reactants.split(" ")
    elements, diffs_1, diffs_2, diffs_3, output = solve_equation.main(equations)
    context["elements"] = elements
    context["output"] = output
    elements_2 = {}
    for i in elements:
        elements_2[elements[i]] = i
    elements = elements_2

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
    context["diffs_3"] = diffs_3

    return render(request, "show_reaction.html", context)


def create_reactions_view(request):
    if request.method == "POST":
        data = request.POST
        # reactions = data["reaction"].split(" ")
        # print(reactions)
        # diffs = solve_equation.main(reactions)
        reaction = Chemical_Reaction.objects.create(reactants=data["reaction"])
        reaction.save()

    return render(request, "create_reactions.html", {})
