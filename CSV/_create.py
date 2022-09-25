import csv


def create_csv(filename, header):
    try:
        with open(filename, 'w') as csv_file:
            csv_creater = csv.DictWriter(csv_file, fieldnames=header)
            csv_creater.writeheader()
    except (IOError, OSError) as csv_file_error:
        print("unable to create csv file {}".format(csv_file_error))


if __name__ == '__main__':
    filename = 'user-info.csv'
    header = ['id', 'name', 'age', 'gender']
    create_csv(filename, header)


    #d
