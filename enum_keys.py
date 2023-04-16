from enum import Enum, auto

class EnumKeys(Enum):
    ### Header View ###
    HEADER_SERVER_URL_TEXT = auto()
    HEADER_DISPLAY_NAME_TEXT = auto()
    HEADER_WHEEL_IMAGE = auto()

    ### Main View ###
    JOB_ID_INPUT = auto()
    GET_JOB_INFO_BUTTON = auto()
    JOB_INFO_MULTILINE = auto()

    ### Config View ###
    CONFIG_SERVER_URL_INPUT = auto()
    CONFIG_SITE_NAME_INPUT = auto()
    CONFIG_DISPLAY_NAME_INPUT = auto()
    CONFIG_TOKEN_NAME_INPUT = auto()
    CONFIG_TOKEN_VALUE_INPUT = auto()
    CONFIG_AUTH_TEST_BUTTON = auto()
    CONFIG_SAVE_BUTTON = auto()