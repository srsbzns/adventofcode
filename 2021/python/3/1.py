def format_diag(raw):
    diag = [i.rstrip() for i in raw]
    return diag

def create_array(formatted_diag):
    # Calculate number of bits in a diagnostic line for array width
    array_width = len(formatted_diag[0])
    # Create 2D array
    array = [[int(j[i]) for j in formatted_diag] for i in range(array_width)]
    return array

def calculate_commons(array):
    # Calculate incoming array measurements
    array_len = len(array)
    array_width = len(array[0])
    # Build summed array
    sum_array = [sum(array[i]) for i in range(array_len)]
    # Declare commons lists
    most_commons = []
    least_commons = []
    # Calculate commons lists
    for i in sum_array:    
        match i:
            case int(n) if n > array_width / 2:
                most_commons.append('1')
                least_commons.append('0')
            case int(n) if n < array_width / 2:
                most_commons.append('0')
                least_commons.append('1')
    # Create dict for return
    commons = {'most':most_commons,'least':least_commons}
    return commons

def flatten_list(list):
    flattened = ""
    for i in list:
        flattened += flattened.join(str(i))
    return int(flattened,base=2)

def main():
    with open('input.txt', 'r') as f:
        raw_diag = f.readlines()
    formatted_diag = format_diag(raw_diag)
    array = create_array(formatted_diag)
    commons = calculate_commons(array)
    gamma_rate = flatten_list(commons['most'])
    epsilon_rate = flatten_list(commons['least'])
    print(gamma_rate * epsilon_rate)

main()