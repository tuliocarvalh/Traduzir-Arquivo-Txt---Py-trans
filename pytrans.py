from py_trans import PyTranslator

text_trans = open("text_to_translate.txt", "a")

frase = text_trans

py_t = PyTranslator()

py_t = PyTranslator(provider="google")

print(py_t.translate(frase, "pt"))