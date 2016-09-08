def read_dict(file_name):
    input_file = open(file_name)
    go_dict = {}
    for line in input_file:
        key = line[0:10]
        value = line[11:-1]
        go_dict[key] = value
    return go_dict


def process_out_res(file_name, go_dict):
    input_file = open(file_name)
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        if list_line[0] in go_dict.keys():
            for i in range(1, len(list_line)):
                if list_line[i] in go_dict.keys():
                    if list_line[i] == "GO:0031109":
                        str_temp = get_two_string_jiaoji(go_dict[list_line[i]],
                                                         go_dict[list_line[0]])
                    else:
                        str_temp = get_two_string_jiaoji(go_dict[list_line[i]],
                                                         go_dict[list_line[0]])

                    go_dict[list_line[i]] = str_temp
                else:
                    go_dict[list_line[i]] = go_dict[list_line[0]]

    return go_dict


def get_two_string_jiaoji(str_i, str_0, flag=False):
    if flag:
        print "str_i:%r" % str_i
        print "str_0:%r" % str_0
    list_i = str_i.strip("\n").split("\t")
    list_0 = str_0.strip("\n").split("\t")
    str_ret = ""
    list_ret = list(set(list_i).union(set(list_0)))
    if flag:
        print list_ret
    for i in list_ret:
        if i != "":
            str_ret = str_ret + i + "\t"
    if flag:
        print "str_ret:%r" % str_ret
    return str_ret


def write_file(cat_dict, out_file_name):
    out_file = open(out_file_name, 'w')
    for key in cat_dict.keys():
        if key == "":
            continue
        if key == "GO:0031109":
            print cat_dict[key]
        if cat_dict[key].startswith("\t"):
            out_file.write(key + cat_dict[key] + "\n")
        else:
            out_file.write(key + "\t" + cat_dict[key] + "\n")

        # print "key:%r,value:%r" % (key, cat_dict[key])
        # break
    out_file.close()


if __name__ == "__main__":
    go_dict = read_dict("bp_to_pro_dict.txt")
    bp_dict = process_out_res("out_res_bp.txt", go_dict)
    write_file(bp_dict, "BP_FULL_PRO_jz.txt")
    go_dict = read_dict("mf_to_pro_dict.txt")
    mf_dict = process_out_res("out_res_mf.txt", go_dict)
    write_file(mf_dict, "MF_FULL_PRO_jz.txt")
    go_dict = read_dict("cc_to_pro_dict.txt")
    cc_dict = process_out_res("out_res_cc.txt", go_dict)
    write_file(cc_dict, "CC_FULL_PRO_jz.txt")
