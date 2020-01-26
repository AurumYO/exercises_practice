# Ex 132. Postal Codes. solved in 24 lines.


# This function reads the Canadian post code, defines if its valid, the province of the code and tells if its urban or
# rural. Function takes poct code in string format, removes spaces
def post_code_reader(postcode):
    postcode = postcode.replace(' ', '')

    # valid postal code has letter in  first, third and sixth position and digit in second, fifth and seventh character
    if len(postcode) == 6 and postcode[0].isalpha() and postcode[2].isalpha() and postcode[4].isalpha() \
            and postcode[1].isdigit() and postcode[3].isdigit() and postcode[5].isdigit():
        # create dictionary with all valid letter code as key and province name in value. One code valid for 2 provinces
        post_codes = {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick',
                      'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario',
                      'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta',
                      'V': 'British Columbia', 'X': ['Nunavut', 'Northwest Territories'], 'Y': 'Yukon'}
        # variables province is empty string at the beginning and address in None
        province, address = '', None
        # if first digit in valid postal code is 0 than it is rural address else it is urban address
        if postcode[1] == '0':
            address = 'rural'
        else:
            address = 'urban'
        # search in dictionary with letter codes and names, if key is found the provinces defines as value of the key
        for k in post_codes.keys():
            if postcode[0] == k and k != 'X':
                province = post_codes[k]
            elif postcode[0] == k and k == 'X':
                province = post_codes[k][0] + ' or ' + post_codes[k][1]
        # function returns tuple with name of the province and address area
        return province, address
    # if postal code is not of the valid format function returns message "Not valid postal code!!!"
    return False


# main function demonstrates function performance.
def main():
    # Test of the function performance
    assert(post_code_reader('T2N 1N4')) == ('Alberta', 'urban')
    assert(post_code_reader('X0A 1B2')) == ('Nunavut or Northwest Territories', 'rural')
    user_postcode = input("Please enter Canadian postal code here: ")
    postal_code_info = post_code_reader(user_postcode)
    if not postal_code_info:
        print("Not valid postal code!!!")
    else:
        print("This postal code corresponds to {} province {} address.".format(postal_code_info[0], postal_code_info[1]))


if __name__ == '__main__':
    main()
