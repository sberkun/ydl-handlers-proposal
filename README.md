# YDL Handler Proposal


Currently, receiving messages looks like [receiver.py](./receiver.py). This is slightly ugly. We could make "handlers" instead, and then the same code will look like [receiver2.py](./receiver2.py).

The main difference is that instead of making a big dictionary of headers to functions, we annotate each function with `@on_header` instead

## Quickstart

Prerequisites: Python 3, and the YDL library. `pip3 install ydl-ipc` to get YDL.

To run the "current" code, run `python3 -m ydl`, `python3 receiver.py`, and `python3 sender.py` in 3 separate terminals.

To run the "proposed" code, run `python3 -m ydl`, `python3 receiver2.py`, and `python3 sender.py` in 3 separate terminals.


## Details

This is somewhat inspired by flask/socketIO, which uses similar annotations (`@app.route` and `@socket.on`). Hopefully this makes it easier to write code that listens for messages.

For more details, see [edge cases](./edge_cases.md).