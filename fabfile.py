from fabric.api import *
import fabric.contrib.project as project
import os


env.content_path = 'src'
env.deploy_path = 'www'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'wf'
dest_path = '~/webapps/asterias'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))

def build():
    clean()
    local('complexity --noserver {content_path}'.format(**env))

def serve():
    clean()
    local('complexity {content_path}'.format(**env))

@hosts(production)
def publish():
    build()
    project.rsync_project(
        remote_dir=dest_path,
        exclude=[".DS_Store","drafts"],
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
