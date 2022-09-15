from fileinput import filename
from msilib.schema import Error
from weasyprint import HTML


def generate_PDF(url, filename):
    HTML(url).write_pdf(filename)


if __name__ == '__main__':
    url = 'https://pypi.org/project/xlrd/'
    filename = 'xlrd_installation.pdf'
    generate_PDF(url, filename)
