from django.shortcuts import render
from django.http import HttpResponse

# Morse code dictionary
pairs = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.', ',': '--..--', ':': '---...', '?': '..--..',
    "'": '.----.', '-': '-....-', '_': '-..-.', '"': '.-..-.', ' ': '   '
}

def translate_to_morse(text, lookup):
    morse = ""
    text = text.lower()
    valid = True

    for letter in text:
        try:
            morse += lookup[letter]
            if letter != ' ':
                morse += ' '
        except KeyError:
            return "Invalid Input"
    return morse

def translate_from_morse(morse, lookup):
    text = ""
    words = morse.split(sep='   ')
    table = {v: k for k, v in lookup.items()}

    try:
        for word in words:
            w = word.split()
            for letter in w:
                text += table[letter]
            text += ' '
    except KeyError:
        return "Invalid Input"

    return text.capitalize()

def morse_code_view(request):
    result = None
    if request.method == 'POST':
        mode = request.POST.get('mode')
        user_input = request.POST.get('user_input')

        if mode == '1':
            result = translate_to_morse(user_input, pairs)
        elif mode == '2':
            result = translate_from_morse(user_input, pairs)
        else:
            result = "Invalid Mode Selected"

    return render(request, 'morse_code.html', {'result': result})
