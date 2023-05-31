from ydl import YDLClient
from shared import YDL_TARGETS, PONG_HEADERS

YC = YDLClient(YDL_TARGETS.PONG)


def add1(x: int):
    print(x + 1)


def double(x: int):
    print(x * 2)


def triple(x: int):
    print(x * 3)


HEADER_MAPPINGS = {
    PONG_HEADERS.ADD1.name: add1,
    PONG_HEADERS.DOUBLE.name: double,
    PONG_HEADERS.TRIPLE.name: triple
}

while True:
    channel, header, message = YC.receive()
    if header in HEADER_MAPPINGS:
        HEADER_MAPPINGS.get(header)(**message)
