
local-service:
	FLASK_ENV=dev NEED_REGISTER=True python wishpost_platform_data_engine_api/server.py

container-up:
	dev wishpost-platform-data-engine-api up

container-service:
	dev wishpost-platform-data-engine-api sh FLASK_ENV=dev NEED_REGISTER=True python wishpost_platform_data_engine_api/server.py

