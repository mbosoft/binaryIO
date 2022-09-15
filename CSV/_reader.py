import csv


def read_csv(filename):
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for record in csv_reader:
                print(record)
    except (IOError, OSError) as csv_file_error:
        print("unable to openthe csv file: {}".format(csv_file_error))


if __name__ == '__main__':
    csv_filename = 'user-info.csv'
    read_csv(csv_filename)
