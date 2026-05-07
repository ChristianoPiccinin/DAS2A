import logging
import azure.functions as func


# Ponto de entrada do Function App.
# Cada trigger é registrado como uma função independente.
app = func.FunctionApp()

# Importa triggers para registrar as functions no app
from triggers import extract_trigger  # noqa: F401
#from triggers import transform_trigger  # noqa: F401
#from triggers import load_trigger  # noqa: F401

app.register_functions(extract_trigger)
logging.info("Azure Function App inicializado.")
