def format_diag(raw):
    diag = [i.rstrip() for i in raw]
    return diag

def create_array(input):
    # Calculate number of bits in a diagnostic line for array width
    array_width = len(input[0])
    # Create 2D array
    array = [[int(j[i]) for j in input] for i in range(array_width)]
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
            case int(n) if n >= array_width / 2:
                most_commons.append('1')
                least_commons.append('0')
            case int(n) if n <= array_width / 2:
                most_commons.append('0')
                least_commons.append('1')
    # Create dict for return
    commons = {'most':most_commons,'least':least_commons}
    return commons

def calculate_o_rating(ext_o_diag):
    o_diag = list(ext_o_diag)
    for x in range(len(o_diag[0])):
        match len(o_diag):
            case int(n) if n <= 1:
                return o_diag
                break
            case int(n) if n > 1:
                o_diag_array = create_array(o_diag)
                commons = calculate_commons(o_diag_array)
                o_diag_len = len(o_diag)
                for y in range(o_diag_len):
                    match o_diag[y]:
                        case str(n) if n[x] != commons['most'][x]:
                            o_diag[y] = 'bzzt'
        o_diag = [i for i in o_diag if i != 'bzzt']
        if len(o_diag) <= 1:
            return int(o_diag[0],base=2)

def calculate_co2_rating(ext_co2_diag):
    co2_diag = list(ext_co2_diag)
    for x in range(len(co2_diag[0])):
        match len(co2_diag):
            case int(n) if n <= 1:
                return co2_diag
                break
            case int(n) if n > 1:
                co2_diag_array = create_array(co2_diag)
                commons = calculate_commons(co2_diag_array)
                co2_diag_len = len(co2_diag)
                for y in range(co2_diag_len):
                    match co2_diag[y]:
                        case str(n) if n[x] != commons['least'][x]:
                            co2_diag[y] = 'bzzt'
        co2_diag = [i for i in co2_diag if i != 'bzzt']
        if len(co2_diag) <= 1:
            return int(co2_diag[0],base=2)

def flatten_list(list):
    flattened = ""
    for i in list:
        flattened += flattened.join(str(i))
    return int(flattened,base=2)

def main():
    with open('input.txt', 'r') as f:
        raw_diag = f.readlines()
    o_input = format_diag(raw_diag)
    co2_input = format_diag(raw_diag)
    o_rating = calculate_o_rating(o_input)
    co2_rating = calculate_co2_rating(co2_input)
    print(o_rating * co2_rating)

main()