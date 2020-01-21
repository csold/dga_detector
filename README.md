# DGA Detector

Command line interface for classifying domains into legit or from a DGA (domain generated algorithm).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python 3 and pip installed

### Installing

Navigate to the project root directory and install the necessary modules

```
pip install -r requirements.txt
```

### Usage

From the project root directory, the dga-cli command line tool can be used to check domain names
```
dga-cli check google.com
```

Or train a new model
```
dga-cli train --model_path=models/new_model.pickle
```

## Running the tests

Run the tests using pytest.
```
pytest
```

## Exploratory Data Analysis

Check out the EDA on the initial dataset by navigating to notebooks and starting up jupyter in the browser.
```
cd notebooks
jupyter notebook
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details