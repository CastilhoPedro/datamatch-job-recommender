import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.backend.NLP.utils.model_persistence import save_model, load_model

class Vectorizer:
    def __init__(self):

        self.model_exists = None
        try:
            data_bundle = load_model()
            self.id_list = data_bundle['ids']
            self.model = data_bundle['model']
            self.matrix = data_bundle['matrix']
            self.model_exists = True
        except FileNotFoundError:
            # self.model = TfidfVectorizer(
            #             max_features=2000,          
            #             ngram_range=(1, 2),         
            #             lowercase=True,             
            #             min_df=1,             # Depois será necessário aumentar
            #             max_df=0.8,
            #             sublinear_tf= True
            #         )
            self.model_exists = False

            
    def fit(self, descriptions: list[tuple[int, str]]):
        """ Esta função é responsável por salvar um modelo com todas as linhas da tabela Vagas (processado = True) no banco de dados.  

        Args:
            descriptions (list[tuple[int, str]]): será usada a função read_vaga_description_list() da classe Database para passar como parâmetro. 
        """

        self.id_list = [i[0] for i in descriptions]
        
        descriptions = [i[1] for i in descriptions]
        self.matrix = self.model.fit_transform(descriptions)
        
        save_model(
            model= self.model, 
            matrix= self.matrix,     
            ids= self.id_list
        )
                
    
    def __vectorize_input(self, text: str):
        return self.model.transform([text])
    
    def get_idx_vagas_rank(self, text: str):
        """Esta função recebe um `text` (palavras-chaves que o usuário inserir) para ser feita a vetorização do mesmo em cima do modelo do Tf-Idf que tiver disponível. 
        Então os índices das vagas são ranqueados e ordenados por proximidade.

        Args:
            text (str): palavras-chaves inseridas pelo usuário no frontend.

        Returns:
            list[int]: lista dos ids em ordem decrescente de similaridade.
        """
        vector_input = self.__vectorize_input(text)
        
        similarity = cosine_similarity(vector_input, self.matrix)[0]
        ordered_indexes = np.argsort(similarity)[::-1]
        
        return [self.id_list[idx] for idx in ordered_indexes]
        

if __name__ == '__main__':
    from src.backend.database.database import Database

    db = Database()

    vct = Vectorizer()

    vct.fit(db.read_vaga_description_list())
    print(vct.get_idx_vagas_rank("sql power bi spark"))
    