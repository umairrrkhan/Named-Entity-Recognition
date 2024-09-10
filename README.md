# Spacy Entity Recognition Example
==============================

## Filename: `spacy_example.py`

### Description
This script uses the Spacy library to perform entity recognition on a sample text.

### Usage
#### Step 1: Install Spacy
```bash
pip install spacy
```
#### Step 2: Download Spacy Model
```bash
python -m spacy download en_core_web_sm
```
#### Step 3: Run the Script
```bash
python spacy_example.py
```

### Code Explanation
#### Load Spacy Model
Load the Spacy model and process the sample text.
#### Entity Recognition
Loop through identified entities and print out their text, label, start and end positions, root text, and other information.
#### Organization Extraction
Print out only the organizations (label "ORG") mentioned in the text.
#### Highlight Entities
Highlight entities in the original text by surrounding them with square brackets and their labels.
