# json_pdf_files
# Generate PDF with Signature

This Python script generates a PDF document containing tabular data from JSON input, along with a signature or stamp image at the end.


## Clone Repository

To clone the repository to your local machine, execute the following command in your terminal or command prompt:

```bash

git clone https://github.com/rajilingam/json_pdf_files.git
```
## Installation

Before running the script, make sure you have the required dependencies installed:

```bash
pip install reportlab
```
## Running the script
To generate a PDF with signature, run the script with the following command

```bash
python generate_pdf.py
```

You can provide JSON data as input using the json_data variable in the script.

# Example JSON data
json_data = [
    [{"Subject": "Math", "Grade": 90}, {"Subject": "Science", "Grade": 85}, {"Subject": "physics", "Grade": 95}],
    [{"Subject": "Math", "Grade": 80}, {"Subject": "Science", "Grade": 75}, {"Subject": "physics", "Grade": 85}]
]

# Generate PDF with signature
output_filename = "stamp1.pdf"
generate_pdf(json_data, output_filename, signature_image)

