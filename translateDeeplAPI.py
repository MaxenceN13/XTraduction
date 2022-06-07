import deepl
import config

auth_key = config.DEEPL_AUTH_KEY
translator = deepl.Translator(auth_key)

def translate(SourceText, lang = "FR"):
	result = translator.translate_text(SourceText, target_lang=lang)
	print(f"Tweet Traduit de '{SourceText}' à '{result.text}'") 
	return result.text