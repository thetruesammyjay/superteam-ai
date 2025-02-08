#!/bin/bash

# Preprocess member database
echo "Preprocessing member database..."
python -c "import json; from src.utils.json_utils import JSONUtils; data = JSONUtils.load_json('data/member_database.json'); JSONUtils.save_json(data, 'data/member_database_processed.json')"

# Preprocess uploaded documents
echo "Preprocessing uploaded documents..."
for file in data/documents/*; do
    python -c "from src.utils.document_parser import DocumentParser; text = DocumentParser.parse_file('$file'); print(f'Processed: $file')"
done

echo "Data preprocessing complete!"