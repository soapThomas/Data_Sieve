def count_number(file_name, out_name):
    input_file = open(file_name)
    out_file = open(out_name, "w")
    i = 0
    max = 0
    for line in input_file:
        line_list = line.strip("\n").split("\t")
        if len(line_list) - 1 > 3000:
            if len(line_list) > max:
                max = len(line_list) - 1
            i += 1
            out_file.write(line)
    print "%d" % max
    input_file.close()


def count_pro(file_name):
    input_file = open(file_name)
    list_res = []
    for line in input_file:
        line_list = line.strip("\n").split("\t")
        for i in range(1, len(line_list)):
            if line_list[i] not in list_res:
                list_res.append(line_list[i])

    print "length:%d" % len(list_res)
    return list_res


def exam(file_name, list_go):
    input_file = open(file_name)
    list_file = []
    for line in input_file:
        list_file.append(line.strip("\n"))

    for i in list_go:
        if i not in list_file:
            print i

    input_file.close()


if __name__ == "__main__":
    count_number("BP_FULL_PRO.txt", "BP_GO.txt")
    count_number("CC_FULL_PRO.txt", "CC_GO.txt")
    count_number("MF_FULL_PRO.txt", "MF_GO.txt")

    list_bp = count_pro("BP_GO.txt")
    list_cc = count_pro("CC_GO.txt")
    list_mf = count_pro("MF_GO.txt")

    exam("temp.out", list_bp)
    exam("temp.out", list_cc)
    exam("temp.out", list_mf)
