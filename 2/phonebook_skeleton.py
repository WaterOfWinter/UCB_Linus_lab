#!/usr/bin/env python3

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'a') as f:
            f.write(f"{sys.argv[2]} {sys.argv[3]}\n")

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            with open(PHONEBOOK_ENTRIES, 'r') as f:
                all_lines = f.readlines()
                for line in all_lines:
                    print(line, end="")

    elif sys.argv[1] == "lookup":
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            for line in f:
                if name in line:
                    phone = line.strip().split()[-1]
                    print(phone)
    
    # alterative->display entire info
        '''
    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'r') as f:
                all_lines = f.readlines()
                for line in all_lines:
                    if sys.argv[2] in line:
                        print(line, end="")
         '''
                        
    elif sys.argv[1] == "remove":
        name = sys.argv[2]
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lines = f.readlines()
        with open(PHONEBOOK_ENTRIES, 'w') as f:
            for line in lines:
                if name not in line:
                    f.write(line)
                        

    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #
        with open(PHONEBOOK_ENTRIES, 'w') as f:
                pass

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
            # YOUR CODE HERE #
            print(lookup, ends="")


if __name__ == "__main__":
    main()
