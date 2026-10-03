# Task 26 – Text Cleaning Basics

## Objective
Clean and standardize customer text data by removing unwanted whitespace, fixing capitalization, and making text values consistent.

## Tools
- Microsoft Excel
- Python
- Pandas

## Files
- `customer_dataset.csv` – raw customer dataset containing common text-quality issues.
- `cleaned_customer_dataset.csv` – cleaned and standardized dataset.
- `before_after_examples.csv` – examples showing the changes before and after cleaning.
- `text_cleaning.py` – Python/Pandas script used for cleaning.
- `README.md` – project documentation.

## Cleaning Operations

### Python / Pandas
- `str.strip()` removes leading and trailing whitespace.
- `str.replace()` with a whitespace pattern normalizes repeated spaces.
- `str.title()` converts names and city values to proper case.
- `str.lower()` standardizes email addresses.
- Status values are standardized to consistent capitalization.

### Excel equivalents
- `TRIM()` – removes unnecessary spaces.
- `PROPER()` – converts text to proper case.
- `LOWER()` – converts text to lowercase.
- `UPPER()` – converts text to uppercase.
- `SUBSTITUTE()` – replaces unwanted text or characters.

## Before / After Example

| Field | Before | After |
|---|---|---|
| Customer Name | `  sahil kumar  ` | `Sahil Kumar` |
| Email | `SAHIL.KUMAR@GMAIL.COM ` | `sahil.kumar@gmail.com` |
| City | `GHAZIABAD ` | `Ghaziabad` |
| Status | ` ACTIVE ` | `Active` |

## Outcome
The customer dataset was standardized so that names, emails, cities, and status values follow consistent formatting. This improves readability and reduces common text-quality issues during analysis.

## Interview Questions

### Why is whitespace a data-quality issue?
Unwanted spaces can create duplicate-looking values, cause matching/filtering problems, and make grouping or analysis inconsistent.

### What does TRIM do?
TRIM removes extra spaces from text, including leading and trailing spaces and repeated spaces between words in common spreadsheet workflows.

## Conclusion
Text cleaning is an important data-preparation step because consistent text values make filtering, grouping, matching, and analysis more reliable.
