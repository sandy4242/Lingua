def code_in_hindGlish(code):
    """
    Converts Hindi's English code to executable Python code.
    Example: "chhapo('Namaste Duniya')" → print('Namaste Duniya')
    """
    translations = {
        "bolo": "print", 
        "yeh_jodho": "+",         
        "yeh_ghatao": "-",   
        "chota": "<",
        "bada": ">",
        "barabar": "==",
        "yeh_hai": "=",
        "sach": "true",  
        "jhoot": "false",  
        "chhapo": "print",
        "agar": "if", 
        "not": "not", 
    }

    lines = code.split("\n")
    translated_lines = []
    
    for line in lines:
        
        for hindi_word, english_word in translations.items():
            line = line.replace(hindi_word, english_word)
        translated_lines.append(line.strip())
    
   
    executable_code = "\n".join(translated_lines)
    return executable_code

def execute_hindi_code(code):
    """
    Executes the translated Hindi's English code.
    """
    try:
        translated_code = code_in_hindGlish(code)
        exec(translated_code)
    except Exception as e:
        print(f"Error executing code: {e}")
