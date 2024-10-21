import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Carregar dados
data = pd.read_csv('melbourne_data2.csv')

# Selecionar features e target
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'YearBuilt', 'TypeHome']
target = 'Price'

X = data[features]
y = data[target]

# Definir colunas numéricas e categóricas
numeric_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'YearBuilt']
categorical_features = ['TypeHome']

# Pré-processamento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ])

# Criar pipeline com GradientBoosting
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(random_state=42))
])

# Hiperparâmetros para busca aleatória
param_distributions = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__learning_rate': [0.01, 0.1, 0.2],
    'regressor__max_depth': [3, 5, 7],
    'regressor__min_samples_split': [2, 5, 10],
    'regressor__min_samples_leaf': [1, 2, 4]
}

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Busca aleatória de hiperparâmetros
random_search = RandomizedSearchCV(pipeline, param_distributions, n_iter=10, cv=3, random_state=42, n_jobs=-1)

# Treinar o modelo
random_search.fit(X_train, y_train)

# Melhor modelo
best_model = random_search.best_estimator_

# Avaliar o modelo
y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Melhor MAE: {mae}")
print(f"R²: {r2}")

# Salvar o melhor modelo treinado
joblib.dump(best_model, 'melbourne_model.joblib')
