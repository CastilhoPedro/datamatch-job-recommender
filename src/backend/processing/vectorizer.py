from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.backend.processing.utils.model_persistence import save_model, load_model
from src.backend.database.database import Database

class Vectorizer:
    def __init__(self):
        
        try:
            self.vectorizer = load_model()
        except FileNotFoundError:
            tfidf = TfidfVectorizer(
                        max_features=2000,          
                        ngram_range=(1, 2),         
                        lowercase=True,             
                        min_df=2,                   
                        max_df=0.8,
                        sublinear_tf= True
                    )
            
            db = Database()
            self.vectorizer = tfidf.fit_transform(db.read_vaga_description_list())
            save_model(self.vectorizer)
    
    def vectorize_input(self, input: str):
        return self.vectorizer.transform([input])
    
    # falta função para fazer a similaridade de consseno

if __name__ == '__main__':
    vct = Vectorizer()
    