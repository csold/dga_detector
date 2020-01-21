import pytest
import pandas as pd

from src.model import extract_features, pred

def test_extract_features():
    data = {'host': ['235ovnaewi.ru'], 'domain': ['235ovnaewi']}
    df = pd.DataFrame.from_dict(data)
    features = extract_features(df)
    assert all([a == b for a, b in zip(features[0], [10, 0.4, 0, 1])])

def test_pred():
    y_pred = pred([[10, 0.4, 0, 1]])
    assert y_pred[0] in [0, 1]