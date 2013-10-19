from fabric.api import *
import fabric.contrib.project as project
import os


# Local path configuration (can be absolute or relative to fabfile)
env.content_path = 'content'
env.local_config = 'pelicanconf.py'
env.publish_config = 'publishconf.py'
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'user@webhost.example.com:22'
dest_path = '/path/to/webroot'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican {content_path} -o {deploy_path} -s {local_config}'.format(**env))

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican {content_path} -o {deploy_path} -s {publish_config}'.format(**env))

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican {content_path} -o {deploy_path} -s {publish_config}'.format(**env))
    project.rsync_project(
        remote_dir=dest_path,
        exclude=[".DS_Store","drafts"],
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
