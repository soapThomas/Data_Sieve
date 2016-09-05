def process_id_go_norm(file_name):
    input_file = open(file_name)
    go_dict = {}
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        for i in range(1, len(list_line)):
            if list_line[i] in go_dict.keys():
                go_dict[list_line[i]] = go_dict[list_line[i]] + "\t" + list_line[0]
            else:
                go_dict[list_line[i]] = list_line[0]

    out_file = open("go_protein_full.txt", "w")
    for i in go_dict.keys():
        if i != "":
            out_file.write(i + "\t" + go_dict[i] + "\n")

    out_file.close()
    input_file.close()

if __name__ == "__main__":
    process_id_go_norm("id_go_norm.txt")