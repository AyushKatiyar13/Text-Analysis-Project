# Text Analysis Project 📊

## Overview

This project focuses on extracting and analyzing textual data from specified URLs. The primary objective is to compute various readability and sentiment metrics and present the results in a structured CSV format. The project utilizes several Python libraries for web scraping, text processing, and data handling.

## Technologies and Tools Used

**Programming Language:**
- Python

**Libraries:**
- **Requests**: For fetching web page content from URLs.
- **BeautifulSoup**: For parsing HTML and extracting relevant article text.
- **TextBlob**: For performing sentiment analysis, including polarity and subjectivity scores.
- **NLTK (Natural Language Toolkit)**: For tokenizing text into sentences and words.
- **Textstat**: For calculating readability metrics like the FOG Index, percentage of complex words, and syllable count.
- **Pandas**: For handling data and saving results to CSV.

**Tools:**
- **Google Drive**: For sharing project files.
- **Google Forms**: For submitting the final project.

## Project Description

### Data Extraction
- Utilized the `requests` library to fetch HTML content from the provided URLs.
- Parsed HTML using `BeautifulSoup` to isolate and extract article text.

### Text Analysis
- Analyzed sentiment using `TextBlob` to obtain polarity and subjectivity scores.
- Computed readability metrics using `Textstat`, including:
  - Average sentence length
  - Percentage of complex words
  - FOG Index
  - Syllables per word
- Performed additional text processing tasks with `NLTK`, such as tokenizing sentences and words.

### Results
- Compiled metrics into a CSV file using `pandas`, which includes various textual metrics for each article.

## Instructions

### Running the Script
1. **Ensure all dependencies are installed**:
   ```bash
   pip install requests beautifulsoup4 textblob nltk textstat pandas
   ```

2. **Run the script**:
   ```bash
   python analyze_text.py
   ```

### Dependencies
- Install required libraries using pip:
   ```bash
   pip install requests beautifulsoup4 textblob nltk textstat pandas
   ```

## Contribution

Feel free to contribute by reporting issues, suggesting improvements, or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Thankyou 😊⭐
