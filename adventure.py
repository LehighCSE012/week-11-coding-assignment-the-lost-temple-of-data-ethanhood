# Your code goes here
"""Assignment 11: The Lost Temple of Data"""
import pandas as pd
import re

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
    return df

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    df = pd.read_csv(tsv_filepath, sep='\t')
    return df

def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    possible_dates = re.findall(pattern, journal_text)
    valid_dates = []

    for date_str in possible_dates:
        try:
            # Try to parse it to validate it's a real date
            datetime.strptime(date_str, "%m/%d/%Y")
            valid_dates.append(date_str)
        except ValueError:
            pass  # Invalid date (like 99/99/9999), skip it

    return valid_dates

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    pattern = r"AZMAR-\d{3}"
    codes = re.findall(pattern, journal_text)
    return codes

# --- Optional: Main execution block for your own testing ---
if __name__ == '__main__':
    # Define file paths (adjust if your files are located elsewhere)
    excel_file = 'artifacts.xlsx'
    tsv_file = 'locations.tsv'
    journal_file = 'journal.txt'

    print(f"--- Loading Artifact Data from {excel_file} ---")
    try:
        artifacts_df = load_artifact_data(excel_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
        print("\nDataFrame Info:")
        artifacts_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {excel_file}")

    print(f"\n--- Loading Location Notes from {tsv_file} ---")
    try:
        locations_df = load_location_notes(tsv_file)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
        print("\nDataFrame Info:")
        locations_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {tsv_file}")

    print(f"\n--- Processing Journal from {journal_file} ---")
    try:
        with open(journal_file, 'r', encoding='utf-8') as f:
            journal_content = f.read()

        print("\nExtracting Dates...")
        dates = extract_journal_dates(journal_content)
        print(f"Found dates: {dates}")

        print("\nExtracting Secret Codes...")
        codes = extract_secret_codes(journal_content)
        print(f"Found codes: {codes}")

    except FileNotFoundError:
        print(f"Error: File not found at {journal_file}")
