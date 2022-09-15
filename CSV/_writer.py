import csv


def create_csv(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_creater = csv.DictWriter(csv_file, fieldnames=header)
            csv_creater.writeheader()
            csv_creater.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print("unable to create csv file {}".format(csv_file_error))


if __name__ == '__main__':
    filename = 'user-info.csv'
    header = ['id', 'name', 'age', 'gender']
    data = [{'id': 4545, 'name': 'Mehdi', 'age': 32, 'gender': 'M'}, ]
    # data=[[],[]]
    create_csv(filename, header,data)
