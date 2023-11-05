import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from xgboost import XGBClassifier

if __name__ == "__main__":
    # data processing
    df = pd.read_csv('diabetes_prediction_dataset.csv')
    df.columns = [i.lower().replace(' ', '_') for i in df.columns]
    df.drop_duplicates(inplace=True)

    df.drop(df[df['gender']=='Other'].index, inplace=True)
    df['gender'] = df.gender.map({'Female': 0, 'Male': 1})

    # splitting and vectorizing the data
    def x_y_split_and_index(data, y_column):
        data.reset_index(drop=True, inplace=True)
        cols_x = data.columns[data.columns!=y_column]
        X = data[cols_x].copy()
        y = data[y_column].values
        return X, y

    df_train_val, df_test = train_test_split(df, test_size=0.2, random_state=42)
    df_train, df_val = train_test_split(df_train_val, test_size=0.25, random_state=42)
    X_train, y_train = x_y_split_and_index(df_train, 'diabetes')
    X_test, y_test = x_y_split_and_index(df_test, 'diabetes')
    X_val, y_val = x_y_split_and_index(df_val, 'diabetes')

    train_dicts = X_train.to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dicts)

    xgb = XGBClassifier(random_state=7, subsample=0.5, max_depth=7, eta=0.1)
    xgb.fit(X_train, y_train)

    output = 'diabetes_dv_and_xgboost.bin'
    with open(output, 'wb') as f_out:
        pickle.dump((dv, xgb), f_out)
