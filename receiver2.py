from ydl import YDLClient
from shared import YDL_TARGETS, PONG_HEADERS
from handler import Handler, on_header

YC = YDLClient(YDL_TARGETS.PONG)
YH = Handler()


@on_header(YH, PONG_HEADERS.ADD1)
def add1(x: int):
    print(x + 1)


@on_header(YH, PONG_HEADERS.DOUBLE)
def double(x: int):
    print(x * 2)


@on_header(YH, PONG_HEADERS.TRIPLE)
def triple(x: int):
    print(x * 3)


while True:
    YH.try_handle(YC.receive())
