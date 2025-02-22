from enum import Enum


class EventNames(Enum):
    """
    Enum representing event names.
    
    This enum represents different event names.
    """

    STARTED = 0
    SYNC = 1
    PACKET_SENT = 2
    PACKET_AVAILABLE = 3
    DONE = 4
    ERROR = 5
    TIMEOUT = 6
    READY = 7
    SYNC_SENT = 8
    SYNC_AVAILABLE = 9
    CONNECTION_ENDING = 10
    REQUEST_RECEIVED = 11
    RESPONSE_RECEIVED = 12
    REQUEST_ERROR = 13
    SIGNAL_READY_CONNECTION = 14
    SIGNAL_READY_LISTEN = 15
    SIGNAL_LISTENING = 16
    SIGNAL_READY_STOP = 17
    FRAME_RECEIVED = 18
    PREFACE_RECEIVED = 19
    ACK_RECEIVED = 20
    TEST_COMPLETED = 21
    FRAMES_SENT = 22
    CLIENT_STARTED = 23
    SERVER_STARTED = 24
    CONNECTION_TERMINATED = 25
    GOAWAY_RECEIVED = 26
