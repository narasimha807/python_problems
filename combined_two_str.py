def convert_str_int(str_num_list):
    num_list = []
    for i in str_num_list:
        integer = int(i)
        num_list.append(integer)
    return num_list
def convert_key_value_pairs(key_list, value_list):
    dict_a = {}
    number_of_keys = len(key_list)
    for item in range(number_of_keys):
        key = key_list[item]
        value = value_list[item]
        dict_a[key] = value
    return(dict_a)


dict_str_1 = input().split()
dict_values_1 = input().split()
dict_str_2 = input().split()
dict_values_2 = input().split()
dict_values_1 = convert_str_int(dict_values_1)
dict_values_2 = convert_str_int(dict_values_2)

student_details_1 = convert_key_value_pairs(dict_str_1, dict_values_1)
student_details_2 = convert_key_value_pairs(dict_str_2,dict_values_2)
student_details_1.update(student_details_2)
student_details = student_details_1.items()
student_details = sorted(student_details)
print(student_details)

