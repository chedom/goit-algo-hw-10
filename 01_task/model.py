import pulp


def find_maximum_resources():
    # initialize model
    model = pulp.LpProblem("Maximize Resources", pulp.LpMaximize)
    # initialize variables
    lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Integer')
    # Maximize total number of products
    model += lemonade + fruit_juice, "Count"
    # add constraint for water
    model += 2*lemonade + fruit_juice <= 100
    # add constraint for sugar
    model += lemonade <= 50
    # add constraint for lemin juice
    model += lemonade <= 30
    # add constraint for fruit puree
    model += 2*fruit_juice <= 40

    model.solve()

    # Print result
    print(pulp.LpStatus[model.status])

    for variable in model.variables():
        print(f"{variable.name} = {variable.varValue}")

    # Вартість цільової функції
    print(f"Total cost = {pulp.value(model.objective)}")
