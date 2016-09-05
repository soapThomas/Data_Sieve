def get_pro_go_dict(file_name):
    input_file = open(file_name)
    pro_30 = {}
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        pro_30[list_line[0]] = 0

    input_file.close()
    return pro_30


def examine(go_30, exam_file_name):
    exam_input_file = open(exam_file_name)
    i = 0
    for line in exam_input_file:
        if i == 0:
            print "line:%r" % line
        i += 1
        go_name = line[0:10]
        if go_name not in go_30.keys():
            print go_name

    exam_input_file.close()

if __name__ == "__main__":
    bp_30 = get_pro_go_dict("biological_process.txt")
    examine(bp_30, "go_bp_dict.txt")
