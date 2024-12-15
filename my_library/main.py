def code_in_hindGlish(code):
    """
    Converts Hindi's English code to executable Python code.
    Example: "chhapo('Namaste Duniya')" → print('Namaste Duniya')
    """
    translations = {
        "bolo": "print",  # Example keyword mapping
        "yeh_jodho": "+",         # Arithmetic operations
        "yeh_ghatao": "-",      # More can be added here
        "chota": "<",
        "bada": ">",
        "barabar": "==",
        "yeh_hai": "=",
        "sach": "true",  # Correct capitalization
        "jhoot": "false",  # Correct capitalization
        "chhapo": "print",
        "agar": "if",  # Mapping "agar" to Python's if
        "not": "not",  # Mapping "not" to Python's not
    }

    # Simple line-by-line transliteration
    lines = code.split("\n")
    translated_lines = []
    
    for line in lines:
        # Replace each Hindi word with the corresponding English translation
        for hindi_word, english_word in translations.items():
            line = line.replace(hindi_word, english_word)
        translated_lines.append(line.strip())  # Remove leading/trailing spaces
    
    # Join the translated lines into one block of code
    executable_code = "\n".join(translated_lines)
    return executable_code

def execute_hindi_code(code):
    """
    Executes the translated Hindi's English code.
    """
    try:
        # Translate and execute the code
        translated_code = code_in_hindGlish(code)
        exec(translated_code)
    except Exception as e:
        print(f"Error executing code: {e}")
