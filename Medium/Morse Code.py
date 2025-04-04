#morse code dictionary containing the morse code for each character
morse ={
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

#decode fn to convert morse code to readable form
def decode(m_code) :
    m_word = m_code.strip().split(' / ')  #Splitting into words
    decoded_text = []
    for i in m_word :
        m_letter = i.split() #Splitting into characters/letters
        decoded_word = ""
        for j in m_letter :
            for letter, morse_code in morse.items(): #Searching for the corresponding character from the dictionary
                if morse_code == j:
                    decoded_word += letter
                    break
                else:
                    continue
        decoded_text.append(decoded_word)
    return " ".join(decoded_text)

code = input("Enter morse code: ")
f = decode(code)
print("Decoded Message : ",f)