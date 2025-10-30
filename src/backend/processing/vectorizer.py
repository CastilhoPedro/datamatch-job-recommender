import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.backend.processing.utils.model_persistence import save_model, load_model
from src.backend.database.database import Database

class Vectorizer:
    def __init__(self):
        
        try:
            data_bundle = load_model()
            self.id_list = data_bundle['ids']
            self.model = data_bundle['model']
            self.matrix = data_bundle['matrix']
            
        except FileNotFoundError:
            self.model = TfidfVectorizer(
                        max_features=2000,          
                        ngram_range=(1, 2),         
                        lowercase=True,             
                        min_df=1,             # Depois será necessário aumentar
                        max_df=0.8,
                        sublinear_tf= True
                    )
            
            db = Database()
            descriptions = db.read_vaga_description_list()
            
            self.id_list = [i[0] for i in descriptions]
            
            descriptions = [i[1] for i in descriptions]
            self.matrix = self.model.fit_transform(descriptions)
            
            save_model(
                model= self.model, 
                matrix= self.matrix,     
                ids= self.id_list
            )
            
    
    def __vectorize_input(self, input: str):
        return self.model.transform([input])
    
    def get_vagas_rank(self, input: str):
        vector_input = self.__vectorize_input(input)
        
        similarity = cosine_similarity(vector_input, self.matrix)[0]
        ordered_indexes = np.argsort(similarity)[::-1]
        
        return [self.id_list[idx] for idx in ordered_indexes]
        

if __name__ == '__main__':
    vct = Vectorizer()
    print(vct.get_vagas_rank("sql power bi spark"))
    