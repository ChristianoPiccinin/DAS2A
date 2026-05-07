import logging
import azure.functions as func


# Ponto de entrada do Function App.
# Cada trigger é registrado como uma função independente.
app = func.FunctionApp()

# Importa triggers para registrar as functions no app
from triggers.extract_trigger import app as extract_trigger

app.register_functions(extract_trigger)
logging.info("Azure Function App inicializado.")

