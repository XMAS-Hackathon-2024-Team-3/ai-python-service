import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import json

kmeans_model = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_priority(json_data):

    df = pd.DataFrame(json_data)

    required_columns = ['id', 'conversion', 'avg_time', 'commission']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Отсутствует необходимый столбец: {col}")

    df = df.rename(columns={
        'conversion': 'CONVERSION',
        'avg_time': 'AVG_TIME',
        'commission': 'COMMISSION'
    })

    features = ['CONVERSION', 'AVG_TIME', 'COMMISSION']
    scaled_data = scaler.transform(df[features])

    clusters = kmeans_model.predict(scaled_data)

    df['priority'] = (
        df['CONVERSION'] -
        df['AVG_TIME'] * 0.1 -
        df['COMMISSION'] * 0.5 +
        clusters * 0.3
    )

    df = df.sort_values(by='priority', ascending=False)

    df = df.rename(columns={
        'CONVERSION': 'conversion',
        'AVG_TIME': 'avg_time',
        'COMMISSION': 'commission'
    })

    result = df[['id', 'conversion', 'avg_time', 'limit_min', 'limit_max']].to_dict(orient='records')
    return json.dumps(result)
