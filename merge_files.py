import os


def merge_files(work_dir):
    example_dir = os.path.join(os.getcwd(), work_dir)
    content = os.listdir(example_dir)
    data = {}
    for file_name in content:
        full_name = os.path.join(example_dir, file_name)
        if (os.path.isfile(full_name) and
                os.path.splitext(full_name)[1] == '.txt'):
            with open(full_name, 'rt', encoding='utf-8') as file:
                data[file_name] = file.readlines()

    sorted_tuple = sorted(data.items(), key=lambda x: len(x[1]))

    with open(os.path.join(os.getcwd(), 'merged_file.txt'),
            'w', encoding='utf-8') as res_file:
        for i in range(len(sorted_tuple)):
            res_file.write(sorted_tuple[i][0] + '\n')
            res_file.write(str(len(sorted_tuple[i][1])) + '\n')
            res_file.writelines(sorted_tuple[i][1])
            res_file.write('\n')


merge_files('sorted')