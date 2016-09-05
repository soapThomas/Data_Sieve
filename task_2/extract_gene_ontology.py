import pandas as pd

COL_NAMES = ['DB', 'DB_ID', 'DB_SYM', 'QUA', 'GO_ID', 'DB_REF', 'EVI_CODE', 'WITH_FROM',
             'ASP', 'DB_NAME', 'DB_SYN', 'DB_TYPE', 'TAXON', 'DATE', 'ASS', 'ANE', 'GENE_PRO']

FILE_NAME = "evidence_code.txt"


def process_file(file_name):
    out_file_name = "id_to_go.txt"
    data = pd.read_table(file_name, names=COL_NAMES, low_memory=False)
    data.to_csv(out_file_name, index=False, header=False, sep="\t", columns=['DB_ID', 'GO_ID'])


def get_pro_go_list(file_name):
    input_file = open(file_name)
    pro_to_go = {}
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        if list_line[0] not in pro_to_go.keys():
            pro_to_go[list_line[0]] = list_line[1]
        else:
            pro_to_go[list_line[0]] = pro_to_go[list_line[0]] + "\t" + list_line[1]

    print len(pro_to_go)

    out_file_name = "id_map_go.txt"
    out_file = open(out_file_name, 'w')
    for key in pro_to_go:
        out_file.write(key + "\t" + pro_to_go[key] + "\n")

    input_file.close()
    out_file.close()


def remove_dup(filename):
    input_file = open(filename)
    out_file_name = "id_map_go_norm.txt"
    out_file = open(out_file_name, 'w')
    for line in input_file:
        list_line = line.strip("\n").split("\t")
        new_list_line = []
        for i in list_line:
            if i not in new_list_line:
                new_list_line.append(i)
        for j in new_list_line:
            out_file.write(j + '\t')
        out_file.write('\n')


if __name__ == "__main__":
    # process_file(FILE_NAME)
    # get_pro_go_list("id_to_go.txt")
    remove_dup("id_map_go.txt")
