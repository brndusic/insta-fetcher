
lines_seen = set() # holds lines already seen
with open("cleaned-file.txt", "w") as output_file:

    for each_line in open("usernames.txt", "r"):

        last_char = each_line[-2:]
        if last_char != ",\n":
            continue

        if each_line not in lines_seen: # check if line is not duplicate
            output_file.write(each_line)
            lines_seen.add(each_line)
