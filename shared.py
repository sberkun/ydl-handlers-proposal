from ydl import header

class YDL_TARGETS:
    PONG = "ydl_target_pong"


class PONG_HEADERS:
    @staticmethod
    @header(YDL_TARGETS.PONG, "add1")
    def ADD1(x: int):
        pass

    @staticmethod
    @header(YDL_TARGETS.PONG, "double")
    def DOUBLE(x: int):
        pass

    @staticmethod
    @header(YDL_TARGETS.PONG, "triple")
    def TRIPLE(x: int):
        pass
