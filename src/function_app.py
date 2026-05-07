import logging
import azure.functions as func

# Ponto de entrada do Function App.
# Cada trigger é registrado como uma função independente.
app = func.FunctionApp()

# Importa triggers para registrar as functions no app
from triggers.extract_cliente import app as extract_cliente
from triggers.extract_pedido import app as extract_pedido
from triggers.extract_entrega import app as extract_entrega




