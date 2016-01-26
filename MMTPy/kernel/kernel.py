from ipykernel.kernelbase import Kernel

class MMTKernel(Kernel):
    implementation = 'MMT Kernel'
    implementation_version = '1.0'
    language = 'mmt'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain'}
    banner = "MMT Kernel - Not yet finished"

    def __init__(self, *args, **kwargs):
        super(MMTKernel, self).__init__(*args, **kwargs)

        self._start_mmt("http://localhost:8080")

    def _start_mmt(self, connection):
        pass

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        if not silent:
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }
