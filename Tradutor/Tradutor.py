from translate import Translator

# Configurar a tradução
s = Translator(from_lang='english', to_lang='pt-br')

# Traduz o texto desejado
res = s.translate('Hello world.')

print(res)
