#!/bin/sh

# Entrypoint for api server
exec /production/wishpost-platform-data-engine-api/persistent/virtualenv/bin/gevent-wsgi wishpost_platform_data_engine_api.server:app
