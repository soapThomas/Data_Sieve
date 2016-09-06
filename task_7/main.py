def format_process(file_name):
    input_file = open(file_name)
    for line in input_file:
        if "GO:0031109" == line[0:10]:
            print "line:%r" % line
            break

if __name__ == "__main__":
    format_process("BP_FULL_PRO.txt")