#!/bin/bash

# PostgreSQL database credentials and backup settings
DB_USER="django"
DB_NAME="django"
DB_PASSWORD="django"
DB_HOST="localhost"
BACKUP_DIR="backup"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_FILE="all_pg_dbs_hour.sql"
mkdir -p "$BACKUP_DIR"


# Backup the PostgreSQL database
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -U $DB_USER -d $DB_NAME -f $BACKUP_DIR/$BACKUP_FILE

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
else
    echo "Backup failed. Exiting."
    exit 1
fi


# List files and filter by name using grep, then delete
FILE_ID=$(gdrive list | grep "$BACKUP_FILE" | awk '{print $1}')

if [ -n "$FILE_ID" ]; then
  gdrive delete "$FILE_ID"
else
  echo "File not found: $FILE_NAME"
fi


# Upload the backup file to Google Drive using gdrive
gdrive upload $BACKUP_DIR/$BACKUP_FILE

# Check if the upload was successful
if [ $? -eq 0 ]; then
    echo "Upload to Google Drive completed successfully."
else
    echo "Upload to Google Drive failed. Exiting."
    exit 1
fi
