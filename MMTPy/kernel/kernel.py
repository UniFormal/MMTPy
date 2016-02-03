from ipykernel.kernelbase import Kernel
from MMTPy.backend import qmtbackend

class MMTKernel(Kernel):
    implementation = 'MMT Kernel'
    implementation_version = '1.0'
    language = 'mmt'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain'}
    banner = "MMT Kernel - Not yet finished"

    def __init__(self, *args, **kwargs):
        super(MMTKernel, self).__init__(*args, **kwargs)
        self.connected = False
        self.q = None

    def run_connect(self, code):
        CONNECT_PREFIX = "@connect "

        if not code.startswith(CONNECT_PREFIX):
            return (False, Exception("Not connected, use '@connect <uri>'"))

        uri = code[len(CONNECT_PREFIX):]
        try:
            self.q = qmtbackend.QMTBackend(uri)
            self.connected = True
            return (True, "Connected to MMT instance at %s" % uri)
        except Exception as e:
            return (False, e)

    def run_code(self, code):
        try:
            return (True, self.q.handleLine(code))
        except Exception as e:
            return (False, e)

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):

        if self.connected:
            (s, c) = self.run_code(code)
        else:
            (s, c) = self.run_connect(code)

        return self.format_response(silent, s, c)

    def format_response(self, silent, state, text):

        if not silent:
            stream_content = {'name': 'stdout' if state else 'stderr', 'text': str(text)}
            if not state:
                stream_content['ename'] = text.__class__.__name__
                stream_content['text'] = str(text)
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok' if state else 'error',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }
