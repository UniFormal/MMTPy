class Interface:
    def __init__(self, port, host = "localhost"):
        """
        Creates a new MMT Interface representing a connection to the MMT HTTP API.

        port -- Port to connect to.
        host -- Host to connect to. Defaults to localhost.
        """

        # check if port is actually a port
        if not isinstance(port, int) or port < 1 or port > 65535:
            raise ValueError("port must be a valid port number between 1 and 65535 (inclusive)")

        self.port = port

        # TODO: Check if this is a valid host dynamically.
        self.host = host
