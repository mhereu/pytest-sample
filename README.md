# pytest-sample

## Requirements (Ubuntu20)

```
sudo apt-get install python3-venv python3-pip
```

## Setup
```
python3 setup.py install
```

Old way:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --no-deps --upgrade pip
python3 -m pip install -U setuptools
python3 -m pip install -U -r requirements-dev.txt
```
## Update your local venv:
```
python3 -m venv --clear venv
python3 -m pip install -U -r requirements-dev.txt
```