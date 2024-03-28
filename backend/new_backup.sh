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
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -U $DB_USER -d $DB_NAME -f "$BACKUP_DIR/$BACKUP_FILE"

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
else
    echo "Backup failed. Exiting."
    exit 1
fi

# Try to delete existing backup in Google Drive
# Fetch list of file IDs for existing backups (assuming `gdrive list` outputs ID in first column)
EXISTING_FILES=$(gdrive list --query "name contains '$BACKUP_FILE'" --no-header | awk '{print $1}')

if [ -n "$EXISTING_FILES" ]; then
  echo "Existing backup files found. Attempting to delete..."
  for FILE_ID in $EXISTING_FILES; do
    gdrive delete "$FILE_ID"
    if [ $? -eq 0 ]; then
      echo "Successfully deleted file ID: $FILE_ID"
    else
      echo "Failed to delete file ID: $FILE_ID. Manual cleanup might be required."
    fi
  done
else
  echo "No existing backup files found to delete."
fi

# Upload the backup file to Google Drive using gdrive
gdrive upload "$BACKUP_DIR/$BACKUP_FILE"

# Check if the upload was successful
if [ $? -eq 0 ]; then
    echo "Upload to Google Drive completed successfully."
else
    echo "Upload to Google Drive failed. Exiting."
    exit 1
fi

