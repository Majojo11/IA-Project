import pandas as pd

data = {
    'Cielo': ['Lluvia', 'Lluvia', 'Nublado', 'Sol', 'Sol', 'Sol', 'Nublado', 'Lluvia', 'Lluvia', 'Soleado', 'Lluvia', 'Nublado', 'Nublado', 'Soleado'],
    'Temperatura': ['Calor', 'Calor', 'Calor', 'Templado', 'Frio', 'Frio', 'Frio', 'Templado', 'Frio', 'Templado', 'Templado', 'Templado', 'Calor', 'Templado'],
    'Humedad': ['Alta', 'Alta', 'Alta', 'Alta', 'Normal', 'Normal', 'Normal', 'Alta', 'Normal', 'Normal', 'Normal', 'Alta', 'Normal', 'Alta'],
    'Viento': ['No', 'Si', 'No', 'No', 'No', 'Si', 'Si', 'No', 'No', 'No', 'Si', 'Si', 'No', 'Si'],
    'SeJugo': ['No', 'No', 'Si', 'Si', 'Si', 'No', 'Si', 'No', 'Si', 'Si', 'Si', 'Si', 'Si', 'No']
}

df = pd.DataFrame(data)


se_jugo = (df['SeJugo'] == 'Si').mean()
no_se_jugo = 1 - se_jugo

def calcular_probabilidades(df, feature, target):
    conditional_probabilities = {}
    for category in df[feature].unique():
        subset = df[df[feature] == category]
        p_target_given_feature = (subset[target] == 'Si').mean()
        conditional_probabilities[category] = p_target_given_feature
    return conditional_probabilities

probabilidades = {}
for feature in ['Cielo', 'Temperatura', 'Humedad', 'Viento']:
    probabilidades[feature] = calcular_probabilidades(df, feature, 'SeJugo')

def Prediccion(condition):
    p_play = se_jugo
    p_not_play = no_se_jugo
    
    for feature, value in condition.items():
        p_feature_given_play = probabilidades[feature].get(value, 0)
        
        p_play *= p_feature_given_play
        p_not_play *= (1 - p_feature_given_play)
    
    if p_play > p_not_play:
        return "Se puede jugar al golf."
    else:
        return "No se puede jugar al golf."

condicion = {'Cielo': 'LLuvia', 'Temperatura': 'Calor', 'Humedad': 'Normal', 'Viento': 'Si'}
print(Prediccion(condicion))
