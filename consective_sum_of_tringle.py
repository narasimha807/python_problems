def get_con_sum_list(int_list):
    con_sum_list = []
    for i in range(len(int_list)-1):

        con_sum = int_list[i] + int_list[i+1]
        con_sum_list.append(con_sum)
    return con_sum_list
def print_sum_triange(int_list):
    while len(int_list) > 1:
        con_list = get_con_sum_list(int_list)
        print(con_list)
        int_list = con_list
def convert_str_to_int(str_num_list):
    int_list = []
    for i in str_num_list:
        integer = int(i)
        int_list.append(integer)
    return int_list
str_num_list = input().split(",")
int_list = convert_str_to_int(str_num_list)
print(int_list)
print_sum_triange(int_list)

