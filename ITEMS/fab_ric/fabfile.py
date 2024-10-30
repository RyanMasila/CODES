from fabric.api import *
def host_type():
    run('uname -s')
env.user = 'ubuntu'
env.hosts = ['52.91.134.88']
def uptime():
    run("uptime")
