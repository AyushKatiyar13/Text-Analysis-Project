Project Overview
This project involves extracting textual data from web pages, analyzing the text for various readability and sentiment metrics, and presenting the results in a structured CSV file. The project demonstrates proficiency in web scraping, text processing, and data analysis using Python.

Technologies Used
Programming Language:

Python: Core language used for scripting and data analysis.
Libraries and Tools:

Requests: For sending HTTP requests to fetch web page content.
BeautifulSoup: For parsing HTML and extracting article content.
TextBlob: For performing sentiment analysis, including polarity and subjectivity scores.
NLTK (Natural Language Toolkit): For tokenizing text into sentences and words, essential for various text metrics.
Textstat: For calculating readability metrics such as the FOG Index, percentage of complex words, syllable count, and more.
Pandas: For organizing and saving the analysis results into a CSV file.
Openpyxl: For reading input data from Excel files.
Features
Data Extraction:

Fetches and parses HTML content from specified URLs.
Extracts relevant text from articles, excluding unnecessary parts.
Text Analysis:

Computes sentiment scores (polarity and subjectivity) using TextBlob.
Analyzes readability with metrics like the FOG Index and percentage of complex words.
Evaluates text complexity with average words per sentence, syllables per word, and word count.
Measures personal pronoun usage and average word length.
Output:

Results are compiled and saved in a CSV file for easy interpretation and review.
How to Run
Install Dependencies:

Ensure you have Python installed.
Install required libraries using pip:
bash
Copy code
pip install requests beautifulsoup4 textblob nltk textstat pandas openpyxl
Prepare Input:

Place your input Excel file (Input.xlsx) containing URLs in the project directory.
Run the Script:

Execute the main script to perform data extraction and analysis:
bash
Copy code
python analyze_text.py
Review Results:

Check the generated output.csv file for the analysis results.
Contribution
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!
