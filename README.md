# wishpost-platform-data-engine-api

A wish_flask based micro service.
# Harbor registry login
**IMPORTANT:** Please login into Harbor before you setup dev environment:

Follow the steps in https://wiki.wish.site/display/Infra/Harbor to get the CLI secret of harbor.
```
docker login harbor.infra.wish-cn.com
# input your username and CLI secret, when you see the "Login success", you may back to here and proceed the next step 
```

## Work to do if you are under linux
IMPORTANT: please add following two lines to your `~/.bashrc` before you setup your dev env
```
export USER_ID=`id -u`
export GROUP_ID=`id -g`
```

## Dev env setup

1. Get our code bases for your dev environment, git clone the repository.

   You may put this repository anywhere you want, but the suggestion is to put it to `~/ContextLogic/wishpost-platform-data-engine-api`

2. Now if you type `dev` in the repo, it shall tell you all your projects that being ready to development.
   ```bash
   >> dev
    dev is a CLI tool that provides a thin layer of porcelain on top of Docker Compose projects.

    Usage:
      dev [command]

    Available Commands:
      help                    Help about any command
      nginx                   Run dev commands on the nginx
      mongo                   Run dev commands on the mongo
      wishpost-platform-data-engine-api               Run dev commands on the wishpost-platform-data-engine-api project

    Flags:
      -h, --help      help for dev
          --version   version for dev
   ```

   As you can see, the dev tool will provide some commands for your project, you shall see `build, up, down, ps and sh`

   ```bash
   >> dev wishpost-platform-data-engine-api
   Usage:
   dev wishpost-platform-data-engine-api [command]

   Available Commands:
   build       Build the wishpost-platform-data-engine-api container (and its dependencies)
   down        Stop and destroy the wishpost-platform-data-engine-api project container
   ps          List status of wishpost-platform-data-engine-api containers
   sh          Get a shell on the wishpost-platform-data-engine-api container
   up          Create and start the wishpost-platform-data-engine-api containers

   Flags:
   -h, --help   help for wishpost-platform-data-engine-api

   Use "dev wishpost-platform-data-engine-api [command] --help" for more information about a command.
   ```

3. The **Build** command lets you to build up all your docker images used for your project.

   ```bash
   cd <repo_dir>
   dev wishpost-platform-data-engine-api build
   ```

   The dev tool will build up `wishpost-platform-data-engine-api` image and anything the project will use to run wishpost-platform-data-engine-api service.

4. The **Up** command lets you to start up your docker containers using the images which are built by `build`.

   ```bash
   cd <repo_dir>
   dev wishpost-platform-data-engine-api up
   ```

   The dev tool will start up `wishpost-platform-data-engine-api` containers.

   Also, please use the following command to see if all the containers are up and healthy.

   ```bash
   cd <repo_dir>
   dev wishpost-platform-data-engine-api ps
   ```

5. On the other hand, the **Down** command will stop all your docker containers(but not the images)

   ```bash
   cd <repo_dir>
   dev wishpost-platform-data-engine-api down
   ```

6. The same applies to the local nginx container with `dev nginx [command]`.


## Start up web server/dbshell

After you set up your dev environment, everything is nearly down. The remain things you need to know is to start up your project services so that you can verify your code change is acting as you what. Theoretically, you can build up your own service start up command as you want, the dev tool do not restrict what you can do. But here take our own projects for example, there are some services used very commonly in dev environment including the web server, and the dbshell.

The dev tool use `sh` command to run commands in your containers.

For web server, the entry point is usually the `server.py`, you can run the following command to start up wishpost-platform-data-engine-api web server.

```bash
cd <repo_dir>
dev wishpost-platform-data-engine-api sh FLASK_ENV=dev python wishpost_platform_data_engine_api/server.py
```

Visit https://wishpost-platform-data-engine-api.corp.contextlogic.com/openapi/swagger to test whether the server is ready. Remember to follow the instructions below and setup nginx first.
**Please follow the "[Nginx setup for dev environment](#Nginx setup for dev environment)" first.**

Beyond that, if you wish to run any other commands then `python`, you may use

```
dev wishpost-platform-data-engine-api sh COMMAND ARGS ...
```

## Nginx setup for dev environment

When you use dev tool to setup dev environment for Wish China's projects, you will find that there is a nginx container which is as a reverse proxy for web servers. Every web request will hit the nginx service first and then nginx will decide which container it sends request to.

As nginx will restrict the host name you visit on your web browser, you should set these host names to your `/etc/hosts` file so that you can visit the web server correctly.

```
127.0.0.1 wishpost-platform-data-engine-api.corp.contextlogic.com
```

**Troueble Shooting:**

If the building process is at this point, your server should be ready to use.

## Mongo setup for local development

You could start up a mongo container in your local docker environment.
```bash
>> dev mongo up
```
In order to use it, you can config like this,
```yaml
  extensions:
    dynaconf_merge: true
    mongo:
      enabled: true
      MONGODB_SETTINGS:
        - host: wishpost-platform-data-engine-api-mongo
          db: test
```

## Postgres setup for local development

You could start up a mongo container in your local docker environment.
```bash
>> dev pg up
```
In order to use it, you can config like this,
```yaml
  extensions:
    dynaconf_merge: true
    pg:
      enabled: true
      settings:
        SQLALCHEMY_DATABASE_URI: postgresql://postgres:123@wishpost-platform-data-engine-api-pg:5432/postgres
```

## Pre-commit

**Reference:** https://wiki.wish.site/display/ENG/Pre-commit+hooks+for+China

**Following is an example to run pre-commit on Mac OS.**


**Install pre-commit**

```bash
pip install pre-commit==1.17.0
pre-commit install
```

**If you are all set, every time a 'git commit' runs, pre-commit hooks will run.**

**Or you can run pre-commit manually. After 'git add', you can run:**

```
pre-commit run
```

## Restful URI Standards
Please follow the [URI standards](https://wiki.wish.site/display/WLFE/Restful+URI+Standards+For+Wish+CN)
while designing your APIs. 

## FAQ
Please contact the project owner for more details.
