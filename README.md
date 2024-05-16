# Web Link Extractor

Web Link Extractor is a simple Python application that extracts hyperlinks from web pages and outputs them to CSV files. It consists of a producer-consumer architecture where the producer fetches HTML content from URLs and places it onto a queue, and the consumer parses the HTML to extract hyperlinks and writes them to CSV files.

## Installation

1. Clone the repository
```bash
git clone
```

2. Create and activate a new Pyhton virtual environment
```bash
python3 -m venv env
source env/bin/activate
```


3. Navigate to the project directory:

```bash
cd web-link-extractor
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

To run the web link extractor, execute the main script:

```bash
python main.py
```

By default, the application will extract links from a predefined list of URLs. You can modify this list in the main.py file or provide a file containing a list of URLs.

## Output

The extracted links will be saved as CSV files in the output directory. Each CSV file corresponds to a URL, and it contains two columns: "URL" and "Link".





