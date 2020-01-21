"""DGA detector

Usage:
    dga-cli train [--data_path=<data_path>] [--model_path=<model_path>]
    dga-cli check <domain> [--model_path=<model_path>]
    dga-cli (-h | --help)

Arguments:
    <domain>  Domain name to be classified.

Options:
    --data_path=<data_path>    Path to data csv [default: data/dga_domains.csv]
    --model_path=<model_path>  Path to model [default: models/model.pickle]
    -h --help                  Show this screen.

"""
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from docopt import docopt
from src.model import extract_features, train, pred

def train_model(data_path='data/dga_domains.csv', model_path='models/model.pickle'):
    df = pd.read_csv(data_path)
    X = extract_features(df)
    y = (df['class'] == 'dga').astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    train(X_train, y_train, model_path)

    y_pred = pred(X_test, model_path)
    print(classification_report(y_test, y_pred))

def classify_domain(domain, model_path='models/model.pickle'):
    data = {'host': [domain], 'domain': [domain.split('.')[0]]}
    df = pd.DataFrame.from_dict(data)
    X = extract_features(df)

    y_pred = pred(X, model_path)

    result = 'dga' if y_pred[0] else 'legit'
    print(f'Prediction for {domain}: {result}')

def main():
    arguments = docopt(__doc__)

    if arguments['train']:
        train_model(arguments['--data_path'], arguments['--model_path'])
    elif arguments['check']:
        classify_domain(arguments['<domain>'], arguments['--model_path'])

if __name__ == '__main__':
    main()
