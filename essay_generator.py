import os
from fpdf import FPDF

# Custom FPDF class to handle the top-right page numbers
class EssayPDF(FPDF):
    def header(self):
        # Set font to Times New Roman, size 12
        self.set_font("Times", size=12)
        # Position the page number at the top right
        self.cell(0, 10, txt=str(self.page_no()), align="R")
        self.ln(10)

def parse_text_file(filepath):
    """Reads the input text file and extracts the essay components."""
    data = {"NAME": "", "DATE": "", "PROFESSOR": "", "CLASS": "", "TITLE": "", "TEXT": ""}
    current_section = None
    
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # Identify which section of the file we are currently reading
            if line.startswith("NAME:"):
                data["NAME"] = line.replace("NAME:", "").strip()
                current_section = None
            elif line.startswith("DATE:"):
                data["DATE"] = line.replace("DATE:", "").strip()
                current_section = None
            elif line.startswith("PROFESSOR:"):
                data["PROFESSOR"] = line.replace("PROFESSOR:", "").strip()
                current_section = None
            elif line.startswith("CLASS:"):
                data["CLASS"] = line.replace("CLASS:", "").strip()
                current_section = None
            elif line.startswith("TITLE:"):
                data["TITLE"] = line.replace("TITLE:", "").strip()
                current_section = None
            elif line.startswith("TEXT:"):
                data["TEXT"] = line.replace("TEXT:", "").lstrip()
                current_section = "TEXT"
            elif current_section == "TEXT":
                # Keep appending lines to the text body
                data["TEXT"] += line
                
    return data

def generate_pdf(data, output_filename):
    """Generates the formatted PDF using the parsed data."""
    pdf = EssayPDF()
    
    # Standard college essay margins (1 inch = 25.4 mm)
    pdf.set_margins(left=25.4, top=25.4, right=25.4)
    # Add the first page (this automatically triggers the header for page 1)
    pdf.add_page()
    
    # Standard college essay font
    pdf.set_font("Times", size=12)
    
    # Line height for double spacing (12pt font * ~2 = 8.5mm)
    line_height = 8.5 
    
    # Standard Header Block (Left Aligned)
    pdf.cell(0, line_height, txt=data["NAME"], ln=True)
    pdf.cell(0, line_height, txt=data["PROFESSOR"], ln=True)
    pdf.cell(0, line_height, txt=data["CLASS"], ln=True)
    pdf.cell(0, line_height, txt=data["DATE"], ln=True)
    
    # Title (Centered)
    pdf.cell(0, line_height, txt=data["TITLE"], align="C", ln=True)
    
    # Essay Body Text
    # multi_cell automatically handles line breaks and pagination
    pdf.multi_cell(0, line_height, txt=data["TEXT"].strip(), align="L")
    
    # Save the file
    pdf.output(output_filename)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "final_essay.pdf"
    
    if not os.path.exists(input_file):
        print(f"Error: Could not find {input_file}. Please create it and run the script again.")
    else:
        print(f"Parsing '{input_file}'...")
        parsed_data = parse_text_file(input_file)
        
        print(f"Generating PDF...")
        generate_pdf(parsed_data, output_file)
        
        print(f"Success! Your essay has been saved as '{output_file}'.")
