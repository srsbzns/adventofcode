class Monkey():
    items_inspected = 0
    
    def __init__(self, starting_inventory, operation, test, test_results):
        self.inventory = starting_inventory
        self.operation = operation
        self.test = test
        self.test_results = test_results
    
    def process_turn(self, my_worry):
        for item in self.inventory:

            # 1. Monkey inspects the item, raising my worry level
            print("Monkey inspects item with worry level of " + item + ".")
            # validate the input in case the operation declares "old" as the operator value
            if self.operation[1] == "old":
                operator_value = my_worry
            else:
                operator_value = self.operation[1]
                
            match self.operation[0]:
                case "+":
                    my_worry += operator_value
                case "-":
                    my_worry -= operator_value
                case "*":
                    my_worry *= operator_value
                case "/":
                    my_worry /= operator_value
            print("Worry level " + self.operation[0] + " " + operator_value + " = " + my_worry)
            self.items_inspected += 1
            print("Total items monkey has inspected: " + self.items_inspected ".")

            # 2. Monkey stops inspecting the item, lowering my worry level
            my_worry /= 3
            print("Monkey gets bored with item. Worry level is divided by 3 to " + my_worry + ".")

            # 3. monkey tests item and throws accordingly to the _end_ of the receiving monkey's inventory
            return self.test_item(item, my_worry)

    def test_item(self, item, my_worry):

        # Test the item's worry level and throw to a different monkey based on pass or fail
        if item % self.test[0]:
            print("Test passed. Throwing to Monkey " + self.test_results[0] + ".")
            monkey_#self.test_results[0].inventory.append(item)
        else:
            print("Test failed. Throwing to Monkey " + self.test_results[1] + ".")
            monkey_#self.test_results[0].inventory.append(item)

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
            if line[0] == " ":
                monkeys_list.append(monkey_lines)
                monkey_lines = []
            else:
                monkey_lines += line

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
                inventory = [i.strip(',') for i in line[2:]]
            case "Operation:":
                operation = [i for i in line[4:]]
            case "Test:":
                test = line[3]
            case "If":
                test_results.append(line[5])

    return Monkey(inventory, operation, test, test_results)

# goal here is to identify total monkey_business, which is 
# how many times the two most active monkeys inspected items over 20 rounds, multiplied.
def calculate_monkey_business():
    pass

def main():

    my_worry = 0

    monkeys_list = format_input('input.txt')

    # I _want_ to dynamically generate a Monkey class object named monkey_x for every monkey in the input,
    # but I can't currently find a "blessed" way to accomplish this.
    for monkey in monkeys_list:
        monkey_x = create_monkey(monkey)
    # now I have a Monkey class object for each monkey and can start doing things.
     
    # each monkey processes all items before moving onto next monkey. a round is when all monkeys have gone.
    for round in range(20):
        # iterate through every monkey
        for monkey in range(len(monkeys_list)):
            my_worry = monkey_x.process_turn(my_worry)
                       

    # now that all rounds have been processed, we need to find the two busiest monkeys and calculate total monkey_business

    return calculate_monkey_business()

print(main())

                