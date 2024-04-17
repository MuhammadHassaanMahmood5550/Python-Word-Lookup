# Define the dictionary with English words and their translations in multiple languages
words_dict = {
    "time": {"urdu": "وقت", "french": "temps", "german": "zeit"},
    "day": {"urdu": "دن", "french": "jour", "german": "tag"},
    "water": {"urdu": "پانی", "french": "eau", "german": "wasser"},
    "life": {"urdu": "زندگی", "french": "vie", "german": "leben"},
    "world": {"urdu": "دنیا", "french": "monde", "german": "welt"},
    "man": {"urdu": "آدمی", "french": "homme", "german": "mann"},
    "woman": {"urdu": "عورت", "french": "femme", "german": "frau"},
    "child": {"urdu": "بچہ", "french": "enfant", "german": "kind"},
    "home": {"urdu": "گھر", "french": "maison", "german": "haus"},
    "family": {"urdu": "خاندان", "french": "famille", "german": "familie"},
    "father": {"urdu": "والد", "french": "père", "german": "vater"},
    "mother": {"urdu": "والدہ", "french": "mère", "german": "mutter"},
    "brother": {"urdu": "بھائی", "french": "frère", "german": "bruder"},
    "sister": {"urdu": "بہن", "french": "sœur", "german": "schwester"},
    "friend": {"urdu": "دوست", "french": "ami", "german": "freund"},
    "love": {"urdu": "محبت", "french": "amour", "german": "liebe"},
    "heart": {"urdu": "دل", "french": "cœur", "german": "herz"},
    "mind": {"urdu": "ذہن", "french": "esprit", "german": "verstand"},
    "body": {"urdu": "جسم", "french": "corps", "german": "körper"},
    "food": {"urdu": "کھانا", "french": "nourriture", "german": "essen"},
    "drink": {"urdu": "پینا", "french": "boire", "german": "trinken"},
    "sleep": {"urdu": "نیند", "french": "sommeil", "german": "schlaf"},
    "dream": {"urdu": "خواب", "french": "rêve", "german": "traum"},
    "work": {"urdu": "کام", "french": "travail", "german": "arbeit"},
    "money": {"urdu": "پیسے", "french": "argent", "german": "geld"},
    "job": {"urdu": "نوکری", "french": "travail", "german": "job"},
    "education": {"urdu": "تعلیم", "french": "éducation", "german": "bildung"},
    "school": {"urdu": "اسکول", "french": "école", "german": "schule"},
    "college": {"urdu": "کالج", "french": "collège", "german": "college"},
    "university": {"urdu": "یونیورسٹی", "french": "université", "german": "universität"},
    "teacher": {"urdu": "استاد", "french": "enseignant", "german": "lehrer"},
    "student": {"urdu": "طالب علم", "french": "étudiant", "german": "schüler"},
    "book": {"urdu": "کتاب", "french": "livre", "german": "buch"},
    "pen": {"urdu": "قلم", "french": "stylo", "german": "stift"},
    "paper": {"urdu": "کاغذ", "french": "papier", "german": "papier"},
    "computer": {"urdu": "کمپیوٹر", "french": "ordinateur", "german": "computer"},
    "internet": {"urdu": "انٹرنیٹ", "french": "internet", "german": "internet"},
    "phone": {"urdu": "فون", "french": "téléphone", "german": "telefon"},
    "music": {"urdu": "موسیقی", "french": "musique", "german": "musik"},
    "song": {"urdu": "گانا", "french": "chanson", "german": "lied"},
    "movie": {"urdu": "فلم", "french": "film", "german": "film"},
    "watch": {"urdu": "دیکھنا", "french": "regarder", "german": "schauen"},
    "listen": {"urdu": "سننا", "french": "écouter", "german": "hören"},
    "read": {"urdu": "پڑھنا", "french": "lire", "german": "lesen"},
    "write": {"urdu": "لکھنا", "french": "écrire", "german": "schreiben"},
    "talk": {"urdu": "بات چیت", "french": "parler", "german": "sprechen"},
}

def translate_to_language(word, language):
    word = word.lower()
    if word in words_dict:
        translations = words_dict[word]
        if language in translations:
            return translations[language]
    return "Translation not found"

# Example usage:
# user_input = "movie"
# target_language = "urdu"  # Change this to "urdu", "french", etc. for different languages
user_input = input("Enter word to translate");
target_language = input("Enter target language")
translation = translate_to_language(user_input, target_language)
print(translation)
