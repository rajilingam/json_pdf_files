from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(json_data, output_filename, signature_image):
    # Parse JSON data
    # Assuming json_data is a list of sublists containing dictionaries
    # Each sublist represents one semester, and each dictionary represents a subject
    # Modify this according to your actual JSON structure

    # Create PDF document
    pdf = SimpleDocTemplate(output_filename, pagesize=letter)
    
    # Table data for PDF
    table_data = []
    for semester_data in json_data:
        for subject_data in semester_data:
            table_data.append(list(subject_data.values()))
    
    # Create table
    table = Table(table_data)
    
    # Add style to table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Add table to PDF document
    elements = [table]

    # Add signature or stamp image
    elements.append(Paragraph("<br/><br/><br/><br/>", getSampleStyleSheet()["Normal"]))  # Add some space
    elements.append(signature_image)  # Assuming signature_image is a ReportLab Image object

    # Build PDF
    pdf.build(elements)

# Example JSON data
json_data = [
    [{"Subject": "Math", "Grade": 90}, {"Subject": "Science", "Grade": 85}, {"Subject": "physics", "Grade": 95}],
    [{"Subject": "Math", "Grade": 80}, {"Subject": "Science", "Grade": 75}, {"Subject": "physics", "Grade": 85}]
]

# Example signature image (replace with your own image)
from reportlab.platypus import Image
signature_image = Image("c:\\Users\\admin\\Pictures\\signature.png.jpg", width=100, height=50)

# Generate PDF with signature
output_filename = "stamp1.pdf"
generate_pdf(json_data, output_filename, signature_image)
#signature_image = Image("c:\\Users\\admin\\Pictures\\signature.png.jpg", width=100, height=50)
