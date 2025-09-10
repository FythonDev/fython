keywords = {
    "چاپ": "print",
    "گرفتن": "input",
    "اگر": "if",
    "برای": "for",
    "درون": "in",
    "تابع": "def",
    "بازگرداندن": "return"
}

def translate(code):
    for fa, en in keywords.items():
        code = code.replace(fa, en)
    return code

def run(code):
    exec(translate(code))
