## Enviornment Set Up Instructions
### Create the environment: 
    python -m venv backend_env

### Activate it:
    Windows: backend_env\Scripts\Activate.ps1
    MacOS: source backend_env/bin/activate
(backend_env) should be at the start of all your prompts in the terminal now

### Install the needed packages:
    python -m pip install --upgrade pip
    pip install fastapi uvicorn scikit-learn joblib

### OR 

### Install the packages using requirements.txt: 
    pip install -r requirements.txt

# Launch API server
    uvicorn backend.app.main:app --reload