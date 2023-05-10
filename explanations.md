## solve_equation.py

### implementation

This code is implementing a differential equation solver using the method of finite differences. The main function is the entry point of the program, and it takes a list of chemical equations as input. The equations are represented as strings in the form of "reactants => products", where reactants and products are separated by "=>" and individual chemicals within each side are separated by "+".

The main function then goes on to extract the chemicals and coefficients from the equations and creates a system of differential equations based on the Law of Mass Action, which relates the rate of a chemical reaction to the concentrations of the reactants. The differential equations are solved using the method of finite differences, which approximates the derivatives by finite differences between neighboring points.

The output of the program includes a list of the chemical elements and their corresponding symbols, the differential equations in the form of finite difference equations, and the final output is saved in a file named output.txt.

Overall, the program takes a list of chemical equations, creates a system of differential equations, solves them using the method of finite differences, and outputs the solution to a file.

### Usage

The program is useful for simulating chemical reactions and predicting their behavior over time.
Here are some examples of how this program could be used:

Predicting the behavior of a chemical reaction over time: Suppose you have a chemical reaction that you want to simulate and predict the behavior of over time. You can provide the reaction equation as input to the program and it will generate a system of differential equations that can be solved using the method of finite differences. The output of the program will show you how the concentrations of each chemical in the reaction change over time.
Optimizing a chemical reaction: Suppose you have a chemical reaction that you want to optimize to maximize the yield of a particular product. You can use the program to simulate the reaction and predict the behavior of different reaction conditions. By analyzing the output, you can determine which reaction conditions will result in the highest yield.
Designing new chemical reactions: Suppose you are trying to design a new chemical reaction and want to predict its behavior before conducting experiments. You can use the program to simulate the reaction and analyze the output to determine the feasibility of the reaction and the expected behavior of each chemical involved.
Overall, the program is useful for anyone working with chemical reactions who wants to simulate and predict their behavior over time. It can help with optimization, design, and analysis of chemical reactions.
input

### input / output

```
equations = [
    "H2 + O2 => H2O",
]
output

elements = {'H2': 'f1', 'O2': 'f2', 'H2O': 'f3'}
diffs_1 = {'R1': 'K1*f1*f2'}
diffs_2 = {'F1': [['R1'], []], 'F2': [['R1'], []], 'F3': [[], ['R1']]}
diffs_3 = {'F1': [['K1*f2'], []], 'F2': [['K1*f1'], []], 'F3': [[], ['K1*f1*f2']]}
output = """Equations given
H2 + O2 => H2O

############################################
f1 = H2
f2 = O2
f3 = H2O

############################################
R1 = K1*f1*f2

############################################
F1 = - R1

F2 = - R1

F3 = + R1

############################################
F1 = - K1\*f2

F2 = - K1\*f1

F3 = + K1*f1*f2
"""
```

## Graphing -

### explanation of code

This code seems to define a function named equation_to_graph that takes in five arguments params, elements, diffs_1, diffs_2, and diffs_3.

The function manipulates the inputs in order to obtain a system of differential equations involving the variables x, y, and z, which it then solves using the Euler method. The specific steps the function takes are as follows:

Store the keys in the elements dictionary in a list elem, and reverse the elements dictionary so that the keys and values can be accessed in both directions.
Manipulate the diffs_1 dictionary to create a new dictionary r_d where the keys are strings of the form "x_y" and the values are strings representing the corresponding differential equation. Each differential equation is constructed by parsing the original string in diffs_1 and extracting the variables and coefficients, then formatting them into a string that can be evaluated using eval().
Manipulate the diffs_2 dictionary to create a new dictionary r_d where the keys are the lowercase strings in elements and the values are strings representing the corresponding differential equation. Each differential equation is constructed by parsing the original string in diffs_2 and extracting the variables and coefficients, then formatting them into a string that can be evaluated using eval().
Manipulate the diffs_3 dictionary to create a new dictionary diffs_4 where the keys are the lowercase strings in elements and the values are strings representing the corresponding differential equation. Each differential equation is constructed by parsing the original string in diffs_3 and extracting the variables and coefficients, then formatting them into a string that can be evaluated using eval().
Extract the differential equations for x, y, and z from diffs_3.
Set the initial values for x, y, and z based on the values in params.
Define the time step h, the number of iterations num_iterations, and an array ts of time values.
Initialize an array array_of_values to store the values of x, y, z, and others at each time step.
Define a dictionary parameters_dict to store the values of the parameters in the differential equations.
Define the constants in the differential equations as 1.
Apply the Euler method to solve the differential equations.
Append the new values of x, y, and z to the array_of_values array.
Repeat steps 11 and 12 for num_iterations iterations.
Return the arrays x_array, y_array, and z_array containing the values of x, y, and z at each time step.

### explnation of program in general

The function takes in five arguments: params, elements, diffs_1, diffs_2, and diffs_3. These arguments are used to define the initial conditions, the equations governing the system, and the parameters of the system.

The equation_to_graph function uses the Euler method to solve the system of differential equations and store the solution in arrays. Finally, it uses the Matplotlib library to create a 3D plot of the solution.

Overall, the purpose of the equation_to_graph function is to numerically solve a system of differential equations and plot the solution.

### input / output

The input to this code would be the params, elements, diffs_1, diffs_2, and diffs_3 variables. These variables contain information necessary to define a system of differential equations to be graphed.

The output of this code is a graph of the system of differential equations defined by the input variables. Specifically, the graph shows how the values of x, y, and z change over time as they evolve according to the differential equations. The x axis of the graph represents time, while the y axis represents the values of x, y, and z.
