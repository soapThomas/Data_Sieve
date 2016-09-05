
def get_pro_go_dict(file_name):
    input_file = open(file_name)
    pro_30 = {}
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        pro_30[list_line[0]] = 0

    return pro_30


def remove_no_seq(filename, pro_30):
    """

    :param filename:
    :param pro_30:
    :return:
    """
    input_file = open(filename)
    out_file_name = "id_go_norm.txt"
    out_file = open(out_file_name, 'w')
    for line in input_file:
        list_line = line.strip("\n").split('\t')
        if list_line[0] in pro_30.keys():
            for i in list_line:
                out_file.write(i + "\t")
            out_file.write("\n")


def get_go_to_pro_dic(filename, pro_bp, pro_mf, pro_cc):
    input_file = open(filename)
    for line in input_file:
        list_line = line.strip("\n").split('\t')
        for i in range(1, len(list_line)):
            pass
            # check(list_line[i], pro_bp)


if __name__ == "__main__":
    # pro_30 = get_pro_go_dict("temp.out")
    # print len(pro_30)
    # remove_no_seq("id_map_go_norm.txt", pro_30)
    pro_bp = get_pro_go_dict("out_res_bp.txt")
    pro_cc = get_pro_go_dict("out_res_cc.txt")
    pro_mf = get_pro_go_dict("out_res_mf.txt")
    get_go_to_pro_dic("id_go_norm.txt", pro_bp, pro_mf, pro_cc)
