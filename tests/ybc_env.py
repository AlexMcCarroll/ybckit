import os


def setup():
    os.environ['YBC_RESPONSE_FILE_PREFIX'] = '/tmp/response_'
    os.environ['YBC_REQUEST_FILE'] = '/tmp/request'
    os.environ['YBC_ENV'] = 'True'


def cleanup():
    del os.environ['YBC_RESPONSE_FILE_PREFIX']
    del os.environ['YBC_REQUEST_FILE']
    del os.environ['YBC_ENV']
