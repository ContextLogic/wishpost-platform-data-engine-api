from wish_flask.creation import create_app, create_api

from wishpost_platform_data_engine_api.blueprints.hello import hello_blp

app = create_app(
    __name__,
    # Make sure the service layer classes are imported
    import_modules=['wishpost_platform_data_engine_api.services']
)
api = create_api(app)


api.register_blueprint(hello_blp)

if __name__ == '__main__':
    app.run(host=app.config['listener_host'], port=app.config['listener_port'])


# If you are running outside of docker:
# Try running this script by:
#    >> make local-service
#
# Please go to http://localhost:5557/openapi/swagger for api observation
# Please go to http://localhost:5557/metrics for metrics observation


# If you are running inside docker:
# If you don't up the container, try running with:
#    >> make container-up container-service
# else, try running with:
#    >> make container-service
#
# Please add the following line in your /etc/hosts file.
#    127.0.0.1       wishpost-platform-data-engine-api.corp.contextlogic.com
# Please go to https://wishpost-platform-data-engine-api.corp.contextlogic.com/openapi/swagger for api observation
# Please go to https://wishpost-platform-data-engine-api.corp.contextlogic.com/metrics for metrics observation
