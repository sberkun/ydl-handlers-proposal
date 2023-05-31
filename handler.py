

class Handler():
    """
    A handler object is meant to store a bunch of functions,
    then call the corresponding function whenever a header is received
    """
    def __init__(self):
        self.mapping = {}

    def add_function(self, header, handling_fn):
        """
        Adds a header-function mapping. Incoming messages from the given
        header will be handled with the given function.

        Returns `handling_fn`.
        """
        assert header.name not in self.mapping, "duplicate header"
        self.mapping[header.name] = handling_fn
        return handling_fn

    def can_handle(self, message):
        """
        Returns True if the message is well-formed, and there exists a 
        corresponding function for the handler to call.
        """
        return len(message) == 3 and \
                isinstance(message[1], str) and \
                isinstance(message[2], dict) and \
                message[1] in self.mapping

    def handle(self, message):
        """
        Calls the function corresponding to the given message's header.
        Returns whatever the function returns.
        """
        return self.mapping.get(message[1])(**message[2])

    def try_handle(self, message):
        """
        Combination of `can_handle` and `handle`. If an applicable function
        exists for the given message, calls that function and returns 
        `(True, result)`, where `result` is the return value of the function.
        Otherwise, just returns `(False, None)`.
        """
        if self.can_handle(message):
            return (True, self.handle(message))
        else:
            return (False, None)


def on_header(handler: Handler, header):
    """
    This decorator annotates a function that the handler should call whenever
    the given header is received.
    """
    return lambda f: handler.add_function(header, f)
