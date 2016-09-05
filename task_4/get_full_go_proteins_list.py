def get_parent_list(go_name, go_file_name):
    input_file = open(go_file_name)
    res_list = []
    for line in input_file:
        if line.startswith(go_name):
            res_list = line.strip("\n").split("\t")

    input_file.close()
    return res_list


def process_lines(file_name, go_file_name, out_file_name):
    input_file = open(file_name)
    out_file = open(out_file_name, "w")
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        go_list = get_parent_list(list_line[0], go_file_name)
        for i in range(1, len(go_list)):
            if go_list[i] not in list_line:
                list_line.append(go_list[i])
        for i in list_line:
            out_file.write(i + "\t")
        out_file.write("\n")

    input_file.close()
    out_file.close()


def read_dict(file_name):
    input_file = open(file_name)
    go_dict = {}
    for line in input_file:
        key = line[0:10]
        value = line[11:-1]
        go_dict[key] = value
    return go_dict


def find_tab(file_name):
    input_file = open(file_name)
    for line in input_file:
        key = line[0:10]
        value = line[11:-1]
        print "key:%r,value:%r" % (key, value)
        break

    input_file.close()


def process_out_res(file_name, go_dict):
    input_file = open(file_name)
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        if list_line[0] in go_dict.keys():
            for i in range(1, len(list_line)):
                if list_line[i] in go_dict.keys():
                    str_temp = get_two_string_jiaoji(go_dict[list_line[i]], go_dict[list_line[0]])
                    go_dict[list_line[i]] = str_temp
                else:
                    go_dict[list_line[i]] = go_dict[list_line[0]]

    return go_dict


def get_two_string_jiaoji(str_i, str_0):
    list_i = str_i.strip("\n").split("\t")
    list_0 = str_0.strip("\n").split("\t")
    str_ret = ""
    list_ret = list(set(list_i).union(set(list_i)))
    for i in list_ret:
        str_ret = str_ret + i + "\t"
    return str_ret


def write_file(cat_dict, out_file_name):
    out_file = open(out_file_name, 'w')
    for key in cat_dict.keys():
        if key == "":
            continue
        if cat_dict[key].startswith("\t"):
            out_file.write(key + cat_dict[key] + "\n")
        else:
            out_file.write(key + "\t" + cat_dict[key] + "\n")
        # print "key:%r,value:%r" % (key, cat_dict[key])
        # break
    out_file.close()


if __name__ == "__main__":
    # process_lines("go_bp_dict.txt", "out_res_bp.txt", "GO_FULL_PRO.txt")
    # find_tab("go_bp_dict.txt")
    go_dict = read_dict("go_bp_dict.txt")
    bp_dict = process_out_res("out_res_bp.txt", go_dict)
    write_file(bp_dict, "BP_FULL_PRO.txt")
    go_dict = read_dict("go_mf_dict.txt")
    mf_dict = process_out_res("out_res_mf.txt", go_dict)
    write_file(mf_dict, "MF_FULL_PRO.txt")
    go_dict = read_dict("go_cc_dict.txt")
    cc_dict = process_out_res("out_res_cc.txt", go_dict)
    write_file(cc_dict, "CC_FULL_PRO.txt")
