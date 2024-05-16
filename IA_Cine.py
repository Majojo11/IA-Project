import pandas as pd

# Datos simulados
data = {
    'Genero': ['Acción', 'Comedia', 'Drama', 'Acción', 'Comedia', 'Drama', 'Acción', 'Comedia', 'Drama', 'Acción',
               'Drama', 'Comedia', 'Acción', 'Drama', 'Comedia', 'Acción', 'Drama', 'Comedia', 'Acción', 'Drama'],
    'Presupuesto': ['Alto', 'Medio', 'Bajo', 'Alto', 'Bajo', 'Medio', 'Alto', 'Medio', 'Bajo', 'Alto',
                    'Medio', 'Alto', 'Bajo', 'Alto', 'Medio', 'Bajo', 'Alto', 'Medio', 'Bajo', 'Medio'],
    'Temporada': ['Verano', 'Verano', 'Otoño', 'Invierno', 'Otoño', 'Verano', 'Verano', 'Invierno', 'Otoño', 'Invierno',
                  'Verano', 'Otoño', 'Invierno', 'Verano', 'Invierno', 'Otoño', 'Verano', 'Invierno', 'Otoño', 'Verano'],
    'Estrellas': ['Si', 'No', 'No', 'Si', 'No', 'Si', 'Si', 'No', 'No', 'Si',
                  'No', 'Si', 'Si', 'No', 'No', 'Si', 'Si', 'No', 'Si', 'No'],
    'Exitosa': ['Si', 'No', 'Si', 'Si', 'No', 'Si', 'Si', 'No', 'No', 'Si',
                'No', 'Si', 'No', 'Si', 'No', 'Si', 'Si', 'No', 'Si', 'No']
}


df = pd.DataFrame(data)

# Probabilidades previas
exitosa = (df['Exitosa'] == 'Si').mean()
no_exitosa = 1 - exitosa

def calcular_probabilidades(df, feature, target, alpha=1):
    categories = df[feature].unique()
    conditional_probabilities = {}
    for category in categories:
        subset = df[df[feature] == category]
        p_target_given_feature = (subset[target] == 'Si').sum() + alpha
        p_target_given_feature /= (len(subset) + alpha * len(categories))
        conditional_probabilities[category] = p_target_given_feature
    return conditional_probabilities

# Calcula las probabilidades condicionales para cada característica
probabilidades = {}
for feature in ['Genero', 'Presupuesto', 'Temporada', 'Estrellas']:
    probabilidades[feature] = calcular_probabilidades(df, feature, 'Exitosa')

def Prediccion(condition):
    p_success = exitosa
    p_failure = no_exitosa
    
    for feature, value in condition.items():
        p_feature_given_success = probabilidades[feature].get(value, 1 / (len(df[feature].unique()) + 1))
        
        p_success *= p_feature_given_success
        p_failure *= (1 - p_feature_given_success)
    
    if p_success > p_failure:
        return "La película será probablemente exitosa."
    else:
        return "La película probablemente no será exitosa."

# Interfaz de usuario en consola
def main():
    condition = {}
    print("Ingrese las características de la película para predecir si será exitosa:")
    condition['Genero'] = input("Género (Acción, Comedia, Drama): ")
    condition['Presupuesto'] = input("Presupuesto (Alto, Medio, Bajo): ")
    condition['Temporada'] = input("Temporada de lanzamiento (Verano, Otoño, Invierno): ")
    condition['Estrellas'] = input("Presencia de estrellas reconocidas (Si, No): ")
    
    resultado = Prediccion(condition)
    print(resultado)

if __name__ == "__main__":
    main()
