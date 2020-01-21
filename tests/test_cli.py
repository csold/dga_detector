import pytest, subprocess

def test_classify_domain():
    result = subprocess.check_output(['dga-cli', 'check', 'google.com'])
    assert result == b'Prediction for google.com: legit\r\n'
    # self.assertIn('expected out', result.stdout)

# test_classify_domain()