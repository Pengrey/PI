import connexion
from os import environ

from crowdsorcerer_server_export import encoder
from crowdsorcerer_server_export.hudi_utils.initialize import hudi_init
from crowdsorcerer_server_export.exceptions import *



hudi_init()

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'CrowdSorcerer Export API'}, pythonic_params=True)

# Exceptions
app.add_error_handler(**BAD_DATE_FORMAT)
app.add_error_handler(**UNSUPPORTED_EXPORTATION_FORMAT)
app.add_error_handler(**EMTPY_DATASET)
app.add_error_handler(**FEATURE_SPACE_TOO_LARGE)



print('EXPORT_BASE_PATH:', environ.get('EXPORT_BASE_PATH'))
print('PYSPARK_PYTHON:', environ.get('PYSPARK_PYTHON'))
