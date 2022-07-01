from wish_flask.shell import ipshell, VariableCollector
from wishpost_platform_data_engine_api.server import app
try:
    from flask_mongoengine import Document
except:
    Document = object


ipshell(
    app,
    var_collectors=[
        VariableCollector(
            'wishpost_platform_data_engine_api.models',
            class_types=[Document],
            collect_subclasss=True
        )
    ]
)

# Try running this script by:
#    >> FLASK_ENV=dev python wishpost_platform_data_engine_api/shell.py
