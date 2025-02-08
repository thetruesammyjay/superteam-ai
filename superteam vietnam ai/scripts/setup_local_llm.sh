#!/bin/bash

# Download LLaMA 2 model files
echo "Downloading LLaMA 2 model files..."
wget -P models/llama2/ https://example.com/path/to/llama2/model.bin
wget -P models/llama2/ https://example.com/path/to/llama2/tokenizer.json
wget -P models/llama2/ https://example.com/path/to/llama2/config.json

# Download pre-trained embeddings
echo "Downloading pre-trained embeddings..."
python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); model.save('models/embeddings/')"

echo "Setup complete!"