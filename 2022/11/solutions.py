class Monkey():
    items_inspected = 0
    
    def __init__(self, starting_inventory, operation, test, test_results):
        self.inventory = starting_inventory
        self.operation = operation
        self.test = test
        self.test_results = test_results
    
    def process_turn(self, supermodulo):

        # we'll use these later to provide a list of every throw calculated for later application
        throw_list = []

        if len(self.inventory) == 0:
            pass
        else:
            for item in self.inventory:

                worry_value = item % supermodulo

                # 1. Monkey inspects the item, raising my worry level
                print("Monkey inspects item with worry level of " + str(item) + ".")
                # validate the input in case the operation declares "old" as the operator value
                if self.operation[1] == "old":
                    operator_value = worry_value
                else:
                    operator_value = int(self.operation[1])
                    
                match self.operation[0]:
                    case "+":
                        worry_value = int(worry_value + operator_value) 
                    case "-":
                        worry_value = int(worry_value - operator_value) 
                    case "*":
                        worry_value = int(worry_value * operator_value) 
                    case "/":
                        worry_value = int(worry_value / operator_value) 
                print("Worry level " + str(self.operation[0]) + " " + str(operator_value) + " = " + str(worry_value))
                self.items_inspected += 1
                print("Total items monkey has inspected: " + str(self.items_inspected) + ".")

                # 2. Monkey stops inspecting the item, lowering my worry level
                # DISABLED FOR P2
                # worry_value = int(worry_value / 3)
                # print("Monkey gets bored with item. Worry level is divided by 3 to " + str(worry_value) + ".")

                # 3. monkey tests item with it's new worry value 
                # and throws accordingly to the _end_ of the receiving monkey's inventory
                throw_list.append(self.test_item(worry_value))

            return throw_list

    def test_item(self, item):

        # Test the item's worry level and throw to a different monkey based on pass or fail
        if item % self.test == 0:
            print("Test passed. Throwing to Monkey " + str(self.test_results[0]) + ".")
            return [item, self.test_results[0]]
        else:
            print("Test failed. Throwing to Monkey " + str(self.test_results[1]) + ".")
            return [item, self.test_results[1]]
        # need to remove this item from the monkey's inventory without fucking up the for loop;
        # maybe keep like a running "new_inventory" that gets applied after all items have been processed?
        

# open input file and return formatted output (batched by individual monkey)
def format_input(input_filename):
    with open(input_filename, 'r') as file:
        unformatted_input = file.read().splitlines()
        formatted_input = [i.split() for i in unformatted_input]

        # batch the lists for each line into lists representing each monkey
        # this holds the list of all monkey's line lists
        monkeys_list = []
        # this holds all line lists for a single monkey
        monkey_lines = []
        for line in formatted_input:
            if len(line) == 0:
                monkeys_list.append(monkey_lines)
                monkey_lines = []
            else:
                monkey_lines += [line]
        # final append
        monkeys_list.append(monkey_lines)

        return monkeys_list

# Given a list object containing all relevant lines for a single monkey, return a new Monkey class object
def create_monkey(monkey_lines):

    # initialize creation vars
    inventory = []
    operation = []
    test = 0
    test_results = []

    for line in monkey_lines:
        match line[0]:
            case "Monkey":
                pass
            case "Starting":
                inventory = [int(i.strip(',')) for i in line[2:]]
            case "Operation:":
                operation = [i for i in line[4:]]
            case "Test:":
                test = int(line[3])
            case "If":
                test_results.append(int(line[5]))

    return Monkey(inventory, operation, test, test_results)

# goal here is to identify total monkey_business, which is 
# how many times the two most active monkeys inspected items over 20 rounds, multiplied.
def calculate_monkey_business(monkeys):
    rankings = [i.items_inspected for i in monkeys]
    rankings.sort(reverse=True)
    return rankings[0] * rankings[1]

def main():

    monkeys_list = format_input('input.txt')

    monkeys = []

    for monkey in monkeys_list:
        monkeys.append(create_monkey(monkey))
     
    # figure out supermodulo stuff
    supermodulo = 1
    for monkey in monkeys:
        for item in monkey.inventory:
            supermodulo *= item
    
    # each monkey processes all items before moving onto next monkey. a round is when all monkeys have gone.
    for round in range(10000):
        print("ROUND " + str(round))
        print(" ")
        print(" ")
        # iterate through every monkey
        for monkey in monkeys:
            throw_list = monkey.process_turn(supermodulo)

            if throw_list != None:
                for throw in throw_list:
                    monkeys[throw[1]].inventory.append(throw[0])
                    monkey.inventory.pop(0)

            print(" ")

    # now that all rounds have been processed, we need to find the two busiest monkeys and calculate total monkey_business
    return calculate_monkey_business(monkeys)

print(main())

                