#!/bin/bash

# List all files in Google Drive and retrieve their IDs
FILE_IDS=$(gdrive list --no-header --max 100000 | awk '{print $1}')

# Check if we have files to delete
if [ -z "$FILE_IDS" ]; then
    echo "No files found in Google Drive."
    exit 0
fi

# Loop through each file ID and delete
for ID in $FILE_IDS; do
    echo "Deleting file with ID: $ID"
    gdrive delete "$ID"
done

echo "All files have been deleted from Google Drive."
