def max_value(resourceh_path):
    max_range = (0, 30000)
    values = []
    with open(resourceh_path, 'r') as txt_file:
        a = txt_file.readlines()
        data = [x for x in a if '/' not in x]
        data = [x.split() for x in data]
        for x in data:
            try:
                if int(x[2]) > max_range[0] and int(x[2]) < max_range[1]:
                    values.append(int(x[2]))
            except:
                continue
    max_value = max(values)

    return max_value


def index_last_comment(resourceh_path):
    with open(resourceh_path, 'r') as txt_file:
        a = txt_file.readlines()
        index = 0
        for i, row in enumerate(a):
            if '/' in row:
                index = i
    return index


def resourceh_script(resourceh_path, source: str, destination: str):
    with open(resourceh_path, 'r') as txt_file:
        a = txt_file.readlines()

        data = [x.split() for x in a]
        new_machine = []
        for x in data:
            try:
                if source in x[1]:
                    new_machine.append(x)
            except:
                continue
        new_machine = [[x[0], x[1].replace(source, destination)]
                       for x in new_machine]
        max_value_element = max_value(resourceh_path)
        for x in new_machine:
            max_value_element += 1
            x.append(str(max_value_element))

        new_machine = [" ".join(x) for x in new_machine]
        last_index = index_last_comment(resourceh_path)
        a.insert(last_index-1, "\n".join(new_machine)+'\n')

    with open(resourceh_path, 'w') as txt_file:
        txt_file.writelines(a)


# resourceh_script('D:\\mark\\resource.h', 'LFI174', 'LFI176')
