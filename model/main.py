import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def create_model(data):
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']

    # scaling the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # training the model 
    model = LogisticRegression()
    model.fit(X_train, y_train)
    




def get_clean_data():
    data = pd.read_csv("data/data.csv")
    data = data.drop(columns=['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    return data

def main():
    data = get_clean_data()
    print(data.head())
    model = create_model(data)

if __name__ == '__main__':
    main()