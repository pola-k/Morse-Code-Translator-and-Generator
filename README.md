# Morse Code Generator and Translator

This project is a simple web-based Morse Code Generator and Translator built using **Django**. It allows users to convert English text to Morse code or translate Morse code back to English text.

## Features

- **Morse Code Generator**: Converts plain text into Morse code.
- **Morse Code Translator**: Converts Morse code back into plain text.
- User-friendly interface with clear instructions.
- Supports upper and lower case English alphabets, digits, and common punctuation marks.

## Supported Characters

The application supports the following characters for both generating and translating Morse code:

- **Alphabets**: `A-Z` (both upper and lower case)
- **Numbers**: `0-9`
- **Punctuation**: `!`, `-`, `.`, `,`, `?`, `'`, `"`, `:`, `_`

## How to Use

1. **Translating to Morse Code**:
   - Enter any combination of supported characters.
   - Select the "Generate" option.
   - Click the "Submit" button to convert the text into Morse code.
   
2. **Translating from Morse Code**:
   - Enter the Morse code with a single space separating each character and three spaces separating each word.
   - Select the "Translate" option.
   - Click the "Submit" button to translate the Morse code back into plain text.

## Installation and Setup

To run this project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Morse-Code-Translator-and-Generator.git
    cd Morse-Code-Translator-and-Generator
    ```

2. **Install the required dependencies**:
    Make sure you have Python and Django installed. You can install Django using pip:
    ```bash
    pip install django
    ```

3. **Update the `TEMPLATES_DIR` path**:
    In your `settings.py` file, ensure that the path to the templates directory is correctly set. Locate the `DIRS` option under `TEMPLATES` and modify it as shown below:
    ```python
    import os

    TEMPLATES = [
        {
            # other settings...
            'DIRS': [os.path.join(BASE_DIR, 'path_to_your_templates')],
        },
    ]
    ```
    Replace `'path_to_your_templates'` with the correct path to where your `morse_code.html` template is located.

4. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000/` to use the Morse Code Generator and Translator.

## Project Structure

```bash
.
├── morse_code
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py              # Django view logic for generating and translating Morse code
├── morse_code.html            # HTML template for the web interface
├── static
│   └── css
│       └── styles.css         # CSS file for styling the web interface
├── manage.py
├── README.md
└── requirements.txt           # Python dependencies
```

## Usage

- Enter plain text or Morse code in the input field.
- Choose between generating or translating.
- View the result in the output box after submitting the form.

Enjoy converting and translating Morse code!
