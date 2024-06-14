def max_path_sum(num_list):

    n = len(num_list) - 1

    for list_idx in range(n-1,-1,-1):
        for i in range(len(num_list[list_idx])):
            num_list[list_idx][i] += max(num_list[list_idx+1][i],num_list[list_idx+1][i+1])

    return num_list[0][0]

def get_input_list(inp_str):
    ans_list = []
    for i in inp_str:
        ans_list.append([int(ele) for ele in i.split(' ')])
    return max_path_sum(ans_list)



with open('data/triangle.txt') as fp:
    content = fp.readlines()
    print(get_input_list(content))
