#!/bin/sh

# Entrypoint for worker
exec /production/wishpost-platform-data-engine-api/persistent/virtualenv/bin/python /production/wishpost-platform-data-engine-api/current/wishpost-platform-data-engine-api/wishpost_platform_data_engine_api/worker.py