import pickle

from sklearn.tree import DecisionTreeClassifier

def extract_features(df):
    # Get domain length as column
    df['dom_len'] = [len(i) for i in df['domain'].tolist()]

    # Get number of vowels in domain and divide by domain length
    def vowel_count(domain):
        return len(list(filter(lambda x: x in ['a','e','i','o','u'], domain)))
        
    df['vowels'] = [vowel_count(i) for i in df['domain'].tolist()]
    df['vowels'] /= df['dom_len']

    # Get domain suffix as column and list suffixes used by dga domains
    df['suffix'] = [i.split('.')[-1] for i in df['host'].tolist()]
    for suffix in ['com', 'ru']:
        df[suffix] = (df['suffix'] == suffix).astype(int)

    return df[['dom_len', 'vowels', 'com', 'ru']].values

def train(X, y, model_path='models/model.pickle'):
    model = DecisionTreeClassifier()
    model.fit(X, y)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

def pred(X, model_path='models/model.pickle'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model.predict(X)
