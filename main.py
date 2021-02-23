from pizza import Pizza


def read_data(filename):
    """Read data from the specified file"""
    with open(filename, 'r') as f:
        content = f.read().splitlines()
    n_pizzas, teams_of2, teams_of3, teams_of4 = map(int, content[0].split(' '))

    menu = []

    for i in range(n_pizzas):
        menu.append(Pizza(i, content[i + 1].split(' ')[1:]))

    return menu, teams_of2, teams_of3, teams_of4


def calculate_score(order, pizza):
    """Calculate the score for the chosen pizzas"""
    unique_ingredients = set(pizza.ingredients)
    for p in order:
        unique_ingredients = unique_ingredients.union(p.ingredients)
    return len(unique_ingredients)


def process_order(team_of, teams_number, menu):
    """Process the order for the specified number of teams """
    orders = []
    while menu != [] and len(orders) < teams_number:
        score_max = 0
        team_order = []
        for _ in range(team_of):
            selected = None
            for pizza in menu:
                score = calculate_score(team_order, pizza)
                if score > score_max:
                    score_max = score
                    selected = pizza
            if selected is not None:
                team_order.append(selected)
                menu.remove(selected)
        if len(team_order) == team_of:
            orders.append((team_of, team_order))
    return orders


def write_data(outfile, orders):
    """Write results to the output file"""
    with open(outfile, 'w') as out:
        out.write(str(len(orders)) + '\n')
        for order in orders:
            indexes = ' '.join(str(pizza.index) for pizza in order[1])
            out.write(str(order[0]) + ' ' + indexes + '\n')


def deliver(filename, outfile):
    """Complete delivery for all teams"""
    menu, teams_of2, teams_of3, teams_of4 = read_data(filename)
    orders = []
    orders.extend(process_order(2, teams_of2, menu))
    orders.extend(process_order(3, teams_of3, menu))
    orders.extend(process_order(4, teams_of4, menu))
    write_data(outfile, orders)


if __name__ == '__main__':

    INPUT_PATH = './input'
    OUTPUT_PATH = './output'

    INPUT_SUFFIX = '.in'
    OUTPUT_SUFFIX = '.out'

    files = [
        'a_example',
        'b_little_bit_of_everything',
        'c_many_ingredients',
        'd_many_pizzas',
        'e_many_teams'
    ]

    for file in files:
        deliver(f'{INPUT_PATH}/{file + INPUT_SUFFIX}',
                f'{OUTPUT_PATH}/{file + OUTPUT_SUFFIX}')
