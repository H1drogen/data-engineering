def mini_pager(file_path):
    # implement me
    with open(file_path, 'r') as data:
        lines = ''
        while True:
            for x in range(1, 10):
                lines += data.readline()
            yield lines

        
def get_secret_message(file_path):
    # implement me
    pass

if __name__ == '__main__':
    print(get_secret_message('data.txt'))