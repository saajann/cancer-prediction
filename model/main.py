import pandas as pd

def get_clean_data():
    data = pd.read_csv("data/data.csv")
    data = data.drop(columns=['Unnamed: 32', 'id'])
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    return data

def main():
    data = get_clean_data()
    print(data.head())

if __name__ == '__main__':
    main()