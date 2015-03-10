# this is for settings to be used by tasks.py
from __future__ import unicode_literals, absolute_import

import os
from os import path

###############################
# THESE SETTINGS MUST BE EDITED
###############################

# This is the directory inside the project dev dir that contains the django
# application
project_name = "infra-diagnostics"

# The django apps that are part of this project - used for running tests
# and migrations
django_apps = []

# repository type can be "cvs", "svn" or "git"
#repo_type = "svn"
#repository = 'https://svn.aptivate.org/svn/' + project_name + '/dev'

repo_type = "git"
repository = 'git@git.aptivate.org:' + project_name + '.git'

##################################################################
# THESE SETTINGS MAY WELL BE CORRECT FOR A STANDARD DJANGO PROJECT
# BUT SHOULD STILL BE REVIEWED
##################################################################

# put "django" here if you want django specific stuff to run
# put "plain" here for a basic apache app
project_type = "plain"

# does this virtualenv for python packages
use_virtualenv = True

# python version - major version must be exact, minor version is the minimum
python_version = (2, 7)

################################
# PATHS TO IMPORTANT DIRECTORIES
################################

# set the deploy directory to be the one containing this file
local_deploy_dir = path.dirname(__file__)

local_vcs_root = path.abspath(path.join(local_deploy_dir, os.pardir))

# the path from the VCS root to the virtualenv dir
relative_ve_dir = path.join(local_vcs_root, '.ve')

# requirements can be in a single file, or in a directory
# the requirements file
requirements_per_env = False
local_requirements_file = path.join(local_deploy_dir, 'pip_packages.txt')

test_cmd = ' mamba'

# production server - if commented out then the production task will abort
# host_list = {}

# this is the default git branch to use on each server
# default_branch = {}

# where on the server the django apps are deployed
server_home = '/opt/'

# the top level directory on the server
# underneath it there will be dev/ containing the live instance
# and previous/ containing old copies for rollback
server_project_home = path.join(server_home, project_name)

# which web server to use (or None)
webserver = None

import socket

if socket.getfqdn().endswith('.fen.aptivate.org'):
    pypi_cache_url = 'http://fen-vz-pypicache.fen.aptivate.org/simple'
