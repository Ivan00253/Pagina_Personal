from googletrans import Translator

traductor = Translator()

texto = "Algo, no lo sé"

traduccion = traductor.translate(texto, src="es", dest="en")

print(traduccion.text)