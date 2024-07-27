import pandas as pd

def validate_csv(file_path):
    df = pd.read_csv(file_path)

    # Check if all columns are present
    expected_columns = ['File Name', 'Polarity Score', 'Subjectivity Score', 'Avg Sentence Length',
                        'Percentage of Complex Words', 'Fog Index', 'Avg Words per Sentence',
                        'Complex Word Count', 'Word Count', 'Syllables per Word', 'Personal Pronouns',
                        'Avg Word Length']
    assert all(col in df.columns for col in expected_columns), "Missing columns in CSV file."

    # Example validation: Check for non-negative values in specific columns
    assert (df['Polarity Score'] >= -1).all() and (df['Polarity Score'] <= 1).all(), "Invalid Polarity Score values."
    assert (df['Subjectivity Score'] >= 0).all() and (df['Subjectivity Score'] <= 1).all(), "Invalid Subjectivity Score values."
    
    # Add more validation checks as needed
    print("CSV validation passed.")

# Validate your CSV file
validate_csv('output.csv')
