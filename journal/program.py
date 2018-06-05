import journal


def print_header():
    print('----------------------------')
    print('----------JOURNAL-----------')
    print('----------------------------')
    print()


def run_event_loop():
    cmd = ''
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd.upper().strip() != 'X':
        cmd = input('Do you want to List, Add entries or eXit?')

        if cmd.upper().strip() == 'L':
            list_entries(journal_data)
        elif cmd.upper().strip() == 'A':
            add_entry(journal_data)
        elif cmd.upper().strip() != 'X':
            print('Incorrect input')

    print('Saving...')
    journal.save(journal_name, journal_data)


def list_entries(journal_data):
    print('Your entries:')
    entries = reversed(journal_data)
    for idx, entry in enumerate(entries):
        print('{}. {}'.format(idx+1, entry))


def add_entry(journal_data):
    text = input('Add your entry, <Enter> to exit:')
    journal.add_entry(text, journal_data)


def main():
    print_header()
    run_event_loop()


main()