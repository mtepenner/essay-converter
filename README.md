# Essay Converter 📄✍️

A streamlined Python utility designed to automate the conversion of plain text drafts into academic-standard PDF documents. This tool handles essential formatting requirements such as 1-inch margins, Times New Roman font, double spacing, and automatic page numbering.

## 📋 Table of Contents

  - [Features](https://www.google.com/search?q=%23features)
  - [Technologies Used](https://www.google.com/search?q=%23technologies-used)
  - [Installation](https://www.google.com/search?q=%23installation)
  - [Usage](https://www.google.com/search?q=%23usage)
  - [Input File Format](https://www.google.com/search?q=%23input-file-format)
  - [License](https://www.google.com/search?q=%23license)

## 🚀 Features

  - **Automatic Formatting**: Automatically sets 1-inch (25.4mm) margins and Times New Roman 12pt font.
  - **Header Generation**: Creates a standard left-aligned academic header including Name, Professor, Class, and Date.
  - **Double Spacing**: Maintains consistent 8.5mm line height for double-spaced readability.
  - **Dynamic Pagination**: Includes top-right page numbering and handles multi-page text wrapping automatically.
  - **Simple Input**: Uses a straightforward keyword-based text file to populate the essay components.

## 🛠️ Technologies Used

  - **Python 3.x**
  - **fpdf**: For PDF generation and layout management.

## 📥 Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/mtepenner/essay-converter.git
    cd essay-converter
    ```

2.  **Install dependencies**:

    ```bash
    pip install fpdf
    ```

## 📖 Usage

1.  Prepare your essay content in a file named `input.txt` following the required format.
2.  Run the generator script:
    ```bash
    python essay_generator.py
    ```
3.  Your formatted PDF will be saved as `final_essay.pdf`.

## 📄 Input File Format

The `input.txt` file must use the following structure to ensure the parser correctly identifies each component:

```text
NAME: Jane Doe
DATE: October 14, 2026
PROFESSOR: Dr. Smith
CLASS: English 101
TITLE: The Impact of Automation on Modern Society
TEXT:
Your essay content goes here. Paragraphs are automatically wrapped.
Skipping a line creates a paragraph break in the PDF.
```

## 🤝 Contributing

Contributions are welcome\! Please feel free to submit a Pull Request or open an issue to suggest improvements.

## ⚖️ License

This project is licensed under the [MIT License](https://www.google.com/search?q=https://opensource.org/licenses/MIT).
