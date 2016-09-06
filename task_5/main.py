def process_id_go_norm(file_name, out_file_nmae):
    input_file = open(file_name)
    go_dict = {}
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        for i in range(1, len(list_line)):
            if list_line[i] in go_dict.keys():
                go_dict[list_line[i]] = go_dict[list_line[i]] + "\t" + list_line[0]
            else:
                go_dict[list_line[i]] = list_line[0]

    out_file = open(out_file_nmae, "w")
    for i in go_dict.keys():
        if i != "":
            out_file.write(i + "\t" + go_dict[i] + "\n")

    out_file.close()
    input_file.close()


def get_go_dict(file_name):
    input_file = open(file_name)
    pro_30 = {}
    for line in input_file:
        list_line = line.strip("\n")
        pro_30[list_line] = 0

    input_file.close()
    return pro_30


def write_to_three_catgory(file_name, bp_dict, mf_dict, cc_dict):
    input_file = open(file_name)
    out_bp_file = open("bp_to_pro_dict.txt", "w")
    out_mf_file = open("mf_to_pro_dict.txt", "w")
    out_cc_file = open("cc_to_pro_dict.txt", "w")
    for line in input_file:
        go_name = line[0:10]
        if go_name in bp_dict.keys():
            out_bp_file.write(line)
        elif go_name in mf_dict.keys():
            out_mf_file.write(line)
        elif go_name in cc_dict.keys():
            out_cc_file.write(line)
        else:
            print "wrongLine: %s" % line

    input_file.close()
    out_bp_file.close()
    out_cc_file.close()
    out_mf_file.close()


if __name__ == "__main__":
    # process_id_go_norm("id_go_norm.txt", "go_protein_full.txt")
    bp_dict = get_go_dict("biological_process.txt")
    mf_dict = get_go_dict("molecular_function.txt")
    cc_dict = get_go_dict("cellular_component.txt")
    write_to_three_catgory("go_protein_full.txt", bp_dict, mf_dict, cc_dict)
