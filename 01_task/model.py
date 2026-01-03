import pulp


def find_maximum_resources():
    # initialize model
    model = pulp.LpProblem("Maximize Resources", pulp.LpMaximize)
    # initialize variables
    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')
    # Maximize total number of products
    model += lemonade + fruit_juice, "Product_Count"
    
    # add constrints
    # add constraint for water
    model += 2*lemonade + fruit_juice <= 100, "Water_Constraint"
    # add constraint for sugar
    model += lemonade <= 50, "Sugar_Constraint"
    # add constraint for lemon juice
    model += lemonade <= 30, "Lemon_Juice_Constraint"
    # add constraint for fruit puree
    model += 2*fruit_juice <= 40, "Fruit_Puree_Constrint"

    model.solve()

    # Print result
    print(pulp.LpStatus[model.status])

    for variable in model.variables():
        print(f"{variable.name} = {variable.varValue}")


    print(f"Total products count = {pulp.value(model.objective)}")
