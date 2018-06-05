import os


def load(name):
    data = []
    filename = get_absolute_filename(name)
    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_absolute_filename(name)
    print('Saving to: {}'.format(filename))
    # fout = open(filename, 'w')

    # for entry in journal_data:
    #     fout.write(entry)
    with open(filename, 'w') as fout:
        entries = journal_data
        for idx, entry in enumerate(entries):
            fout.write('{}'.format(entry) + '\n')

    # fout.close()


def get_absolute_filename(name):
    filename = os.path.abspath(os.path.join('.', 'journals_folder', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
