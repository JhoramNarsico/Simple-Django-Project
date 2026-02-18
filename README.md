# Django Text Analyzer (Stateless/No DB)

A lightweight Django application that performs text analysis operations (word count, uppercase conversion, punctuation removal). This project is configured to run entirely **without a database**.

## Features
*   **Remove Punctuation:** Strips special characters from the text.
*   **UPPERCASE:** Converts all text to capital letters.
*   **Word Count:** Calculates the total number of words.
*   **Stateless:** No database connection (SQLite/PostgreSQL) is required or used.

## Prerequisites
*   Python 3.x installed
*   Git

## Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/django-text-analyzer.git
cd django-text-analyzer
```

2. Create a Virtual Environment
It is recommended to run this in a virtual environment to keep dependencies isolated.

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies
 ```bash
   pip install -r requirements.txt
   ```
4. Run the Server
   ```bash
   python manage.py runserver
   ```
