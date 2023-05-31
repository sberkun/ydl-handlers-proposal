from ydl import YDLClient
from shared import PONG_HEADERS, YDL_TARGETS

YC = YDLClient()

YC.send(PONG_HEADERS.ADD1(x=5))
YC.send(PONG_HEADERS.DOUBLE(x=12))
YC.send(PONG_HEADERS.TRIPLE(x=7))
YC.send(PONG_HEADERS.TRIPLE(x=-3))
YC.send((YDL_TARGETS.PONG, "cheese", {}))
