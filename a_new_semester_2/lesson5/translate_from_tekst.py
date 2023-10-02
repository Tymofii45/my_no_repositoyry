import pandas as pd
from googletrans import Translator

translator = Translator()
a = "Hello World!"



b =translator.translate(a, src="en", dest="fr")
print(b)