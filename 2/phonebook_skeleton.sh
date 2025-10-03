#!/usr/bin/env bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
    # YOUR CODE HERE #
    echo "$2 $3" >> "$PHONEBOOK_ENTRIES"

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
        # YOUR CODE HERE #
        cat "$PHONEBOOK_ENTRIES"
    fi

elif [ "$1" = "lookup" ]; then
    # YOUR CODE HERE #
    grep -F "$2" "$PHONEBOOK_ENTRIES" | awk '{print $NF}'

elif [ "$1" = "remove" ]; then
    # YOUR CODE HERE #
    # grep -v -F "$name" "$PHONEBOOK_ENTRIES" > "$PHONEBOOK_ENTRIES.tmp" && mv "$PHONEBOOK_ENTRIES.tmp" "$PHONEBOOK_ENTRIES"
    sed -i "/$2/d" "$PHONEBOOK_ENTRIES"

elif [ "$1" = "clear" ]; then
    # YOUR CODE HERE #
    > "$PHONEBOOK_ENTRIES"

else
     # YOUR CODE HERE #
    echo "Invalid command: $1"
    echo "Usage: $0 {new|list|lookup|remove|clear} [arguments]"
    exit 1
fi
