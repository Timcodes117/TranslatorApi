from googletrans import LANGUAGES
from deep_translator import GoogleTranslator


lang_list = [str(lang) for lang in LANGUAGES]
char_limit = 10000


def language_is_verified(lang):
    if lang in lang_list:
        return True
    else:
        return False


def verify_source(target):
    if target != "" and target != "auto":
        return target
    else:
        return "auto"


def get_translations(sentence: str, language: str, target: str):
    try:
        if language_is_verified(language):
            print("language is available")
            if len(sentence) < char_limit:
                print("sentence is okay")
                translated_text = GoogleTranslator(source=verify_source(target), target=language).translate(sentence)
                return {"message": translated_text, "status": "200"}
            else:
                raise ValueError(f"sentence should contain less than less than 10000 characters. this contains {len(sentence)}")
        else:
            raise ValueError("language is not available")
    except Exception as err:
        return {"message": "failed to get result", "error": err, "status": "400"}


# print(lang_list)


# result = get_translation("good evening", "af")
#
# # if str(result).__contains__("error"):
# print("translation: ", result)
# # else:
# #     print("failed to get result")

