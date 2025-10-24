import joblib
import os 


_model_path = "src/backend/processing/utils/model.joblib"

def save_model(model, matrix, ids):
    data_bundle = {
        'model': model,
        'matrix': matrix,
        'ids': ids
    }
    joblib.dump(value=data_bundle, filename=_model_path, compress= 3)

def load_model():
    if not os.path.exists(_model_path):
            raise FileNotFoundError(f"Modelo TF-IDF não encontrado em {_model_path}. " f"Execute o treino antes de tentar carregar.")
    return joblib.load(filename=_model_path)


if __name__ == '__main__':
    t = save_model()