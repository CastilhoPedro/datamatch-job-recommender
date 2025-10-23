import spacy
from spacy.symbols import ORTH
from src.utils.helper import skills_list, ufs_dict


class NLP:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_sm")
        
        for terms in [skills_list, ufs_dict.values()]:
            for term in terms:
                self.nlp.tokenizer.add_special_case(term.lower(), [{ORTH: term.lower()}])
    
    def preprocess_text_spacy(self, text):
        doc = self.nlp(text)

        lemmas = [
            token.lemma_.lower()
            for token in doc
            if not token.is_stop and not token.is_punct
        ]

        # Reverte "_" para espaços, se quiser manter legibilidade
        lemmas = [lemma.replace("_", " ") for lemma in lemmas]

        return " ".join(lemmas)

