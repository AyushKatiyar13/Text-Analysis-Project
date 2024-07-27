Text Analysis Project
Overview
This project involves extracting and analyzing textual data from specified URLs. The goal was to compute various readability and sentiment metrics and present the results in a structured CSV format.

Technologies and Tools Used
Programming Language: Python

Libraries:

Requests: For fetching web page content from URLs.
BeautifulSoup: For parsing HTML and extracting relevant article text.
TextBlob: For performing sentiment analysis, including polarity and subjectivity scores.
NLTK (Natural Language Toolkit): For tokenizing text into sentences and words.
Textstat: For calculating readability metrics like the FOG Index, percentage of complex words, and syllable count.
Pandas: For handling data and saving results to CSV.
Tools:

Google Drive: For sharing project files.
Google Forms: For submitting the final project.
Project Description
Data Extraction:

Utilized the requests library to fetch HTML content from the provided URLs.
Parsed HTML using BeautifulSoup to isolate and extract article text.
Text Analysis:

Analyzed sentiment using TextBlob to obtain polarity and subjectivity scores.
Computed readability metrics, including average sentence length, percentage of complex words, FOG Index, and syllables per word using Textstat.
Performed additional text processing tasks with NLTK, such as tokenizing sentences and words.
Results:

Compiled metrics into a CSV file using pandas, which includes various textual metrics for each article.
Instructions
Running the Script:

Ensure all dependencies are installed.
Run the analyze_text.py script to process the URLs and generate the output CSV.
Dependencies:

Install required libraries using pip:
bash
Copy code
pip install requests beautifulsoup4 textblob nltk textstat pandas
Contribution
Feel free to contribute by reporting issues, suggesting improvements, or submitting pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
