from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'wf'
dest_path = 'path/to/out'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

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
    local('pelican -s publishconf.py')

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=['.DS_Store', 'drafts'],
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
