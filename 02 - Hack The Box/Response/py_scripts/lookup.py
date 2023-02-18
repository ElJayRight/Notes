from enum import Enum
class MSFType(Enum):
    TLV_TYPE_ANY = 0
    TLV_TYPE_COMMAND_ID = 1
    TLV_TYPE_REQUEST_ID = 2
    TLV_TYPE_EXCEPTION = 3
    TLV_TYPE_RESULT = 4
    TLV_TYPE_STRING = 10
    TLV_TYPE_UINT = 11
    TLV_TYPE_BOOL = 12
    TLV_TYPE_LENGTH = 25
    TLV_TYPE_DATA = 26
    TLV_TYPE_FLAGS = 27
    TLV_TYPE_CHANNEL_ID = 50
    TLV_TYPE_CHANNEL_TYPE = 51
    TLV_TYPE_CHANNEL_DATA = 52
    TLV_TYPE_CHANNEL_DATA_GROUP = 53
    TLV_TYPE_CHANNEL_CLASS = 54
    TLV_TYPE_CHANNEL_PARENTID = 55
    TLV_TYPE_SEEK_WHENCE = 70
    TLV_TYPE_SEEK_OFFSET = 71
    TLV_TYPE_SEEK_POS = 72
    TLV_TYPE_EXCEPTION_CODE = 300
    TLV_TYPE_EXCEPTION_STRING = 301
    TLV_TYPE_LIBRARY_PATH = 400
    TLV_TYPE_TARGET_PATH = 401
    TLV_TYPE_MIGRATE_PID = 402
    TLV_TYPE_MIGRATE_PAYLOAD = 404
    TLV_TYPE_MIGRATE_ARCH = 405
    TLV_TYPE_MIGRATE_BASE_ADDR = 407
    TLV_TYPE_MIGRATE_ENTRY_POINT = 408
    TLV_TYPE_MIGRATE_SOCKET_PATH = 409
    TLV_TYPE_MIGRATE_STUB = 411
    TLV_TYPE_LIB_LOADER_NAME = 412
    TLV_TYPE_LIB_LOADER_ORDINAL = 413
    TLV_TYPE_TRANS_TYPE = 430
    TLV_TYPE_TRANS_URL = 431
    TLV_TYPE_TRANS_UA = 432
    TLV_TYPE_TRANS_COMM_TIMEOUT = 433
    TLV_TYPE_TRANS_SESSION_EXP = 434
    TLV_TYPE_TRANS_CERT_HASH = 435
    TLV_TYPE_TRANS_PROXY_HOST = 436
    TLV_TYPE_TRANS_PROXY_USER = 437
    TLV_TYPE_TRANS_PROXY_PASS = 438
    TLV_TYPE_TRANS_RETRY_TOTAL = 439
    TLV_TYPE_TRANS_RETRY_WAIT = 440
    TLV_TYPE_TRANS_HEADERS = 441
    TLV_TYPE_TRANS_GROUP = 442
    TLV_TYPE_MACHINE_ID = 460
    TLV_TYPE_UUID = 461
    TLV_TYPE_SESSION_GUID = 462
    TLV_TYPE_RSA_PUB_KEY = 550
    TLV_TYPE_SYM_KEY_TYPE = 551
    TLV_TYPE_SYM_KEY = 552
    TLV_TYPE_ENC_SYM_KEY = 553
    TLV_TYPE_PIVOT_ID = 650
    TLV_TYPE_PIVOT_STAGE_DATA = 651
    TLV_TYPE_PIVOT_NAMED_PIPE_NAME = 652
    TLV_TYPE_HANDLE = 600
    TLV_TYPE_INHERIT = 601
    TLV_TYPE_PROCESS_HANDLE = 630
    TLV_TYPE_THREAD_HANDLE = 631
    TLV_TYPE_PRIVILEGE = 632
    TLV_TYPE_DIRECTORY_PATH = 1200
    TLV_TYPE_FILE_NAME = 1201
    TLV_TYPE_FILE_PATH = 1202
    TLV_TYPE_FILE_MODE = 1203
    TLV_TYPE_FILE_SIZE = 1204
    TLV_TYPE_FILE_SHORT_NAME = 1205
    TLV_TYPE_FILE_HASH = 1206
    TLV_TYPE_MOUNT = 1207
    TLV_TYPE_MOUNT_NAME = 1208
    TLV_TYPE_MOUNT_TYPE = 1209
    TLV_TYPE_MOUNT_SPACE_USER = 1210
    TLV_TYPE_MOUNT_SPACE_TOTAL = 1211
    TLV_TYPE_MOUNT_SPACE_FREE = 1212
    TLV_TYPE_MOUNT_UNCPATH = 1213
    TLV_TYPE_STAT_BUF32 = 1220
    TLV_TYPE_STAT_BUF = 1221
    TLV_TYPE_SEARCH_RECURSE = 1230
    TLV_TYPE_SEARCH_GLOB = 1231
    TLV_TYPE_SEARCH_ROOT = 1232
    TLV_TYPE_SEARCH_RESULTS = 1233
    TLV_TYPE_SEARCH_MTIME = 1235
    TLV_TYPE_SEARCH_M_START_DATE= 1236
    TLV_TYPE_SEARCH_M_END_DATE = 1237
    TLV_TYPE_FILE_MODE_T = 1234
    TLV_TYPE_HOST_NAME = 1400
    TLV_TYPE_PORT = 1401
    TLV_TYPE_INTERFACE_MTU = 1402
    TLV_TYPE_INTERFACE_FLAGS = 1403
    TLV_TYPE_INTERFACE_INDEX = 1404
    TLV_TYPE_SUBNET = 1420
    TLV_TYPE_NETMASK = 1421
    TLV_TYPE_GATEWAY = 1422
    TLV_TYPE_NETWORK_ROUTE = 1423
    TLV_TYPE_IP_PREFIX = 1424
    TLV_TYPE_ARP_ENTRY = 1425
    TLV_TYPE_IP = 1430
    TLV_TYPE_MAC_ADDRESS = 1431
    TLV_TYPE_MAC_NAME = 1432
    TLV_TYPE_NETWORK_INTERFACE = 1433
    TLV_TYPE_IP6_SCOPE = 1434
    TLV_TYPE_SUBNET_STRING = 1440
    TLV_TYPE_NETMASK_STRING = 1441
    TLV_TYPE_GATEWAY_STRING = 1442
    TLV_TYPE_ROUTE_METRIC = 1443
    TLV_TYPE_ADDR_TYPE = 1444
    TLV_TYPE_PROXY_CFG_AUTODETECT = 1445
    TLV_TYPE_PROXY_CFG_AUTOCONFIGURL = 1446
    TLV_TYPE_PROXY_CFG_PROXY = 1447
    TLV_TYPE_PROXY_CFG_PROXYBYPASS = 1448
    TLV_TYPE_PEER_HOST = 1500
    TLV_TYPE_PEER_PORT = 1501
    TLV_TYPE_LOCAL_HOST = 1502
    TLV_TYPE_LOCAL_PORT = 1503
    TLV_TYPE_CONNECT_RETRIES = 1504
    TLV_TYPE_NETSTAT_ENTRY = 1505
    TLV_TYPE_PEER_HOST_RAW = 1506
    TLV_TYPE_LOCAL_HOST_RAW = 1507
    TLV_TYPE_SHUTDOWN_HOW = 1530
    TLV_TYPE_HKEY = 1000
    TLV_TYPE_BASE_KEY = 1001
    TLV_TYPE_PERMISSION = 1002
    TLV_TYPE_KEY_NAME = 1003
    TLV_TYPE_VALUE_NAME = 1010
    TLV_TYPE_VALUE_TYPE = 1011
    TLV_TYPE_VALUE_DATA = 1012
    TLV_TYPE_TARGET_HOST = 1013
    TLV_TYPE_COMPUTER_NAME = 1040
    TLV_TYPE_OS_NAME = 1041
    TLV_TYPE_USER_NAME = 1042
    TLV_TYPE_ARCHITECTURE = 1043
    TLV_TYPE_LANG_SYSTEM = 1044
    TLV_TYPE_SID = 1045
    TLV_TYPE_DOMAIN = 1046
    TLV_TYPE_LOGGED_ON_USER_COUNT = 1047
    TLV_TYPE_LOCAL_DATETIME = 1048
    TLV_TYPE_BUILD_TUPLE = 1049
    TLV_TYPE_ENV_VARIABLE = 1100
    TLV_TYPE_ENV_VALUE = 1101
    TLV_TYPE_ENV_GROUP = 1102
    TLV_TYPE_BASE_ADDRESS = 2000
    TLV_TYPE_ALLOCATION_TYPE = 2001
    TLV_TYPE_PROTECTION = 2002
    TLV_TYPE_PROCESS_PERMS = 2003
    TLV_TYPE_PROCESS_MEMORY = 2004
    TLV_TYPE_ALLOC_BASE_ADDRESS = 2005
    TLV_TYPE_MEMORY_STATE = 2006
    TLV_TYPE_MEMORY_TYPE = 2007
    TLV_TYPE_ALLOC_PROTECTION = 2008
    TLV_TYPE_PID = 2300
    TLV_TYPE_PROCESS_NAME = 2301
    TLV_TYPE_PROCESS_PATH = 2302
    TLV_TYPE_PROCESS_GROUP = 2303
    TLV_TYPE_PROCESS_FLAGS = 2304
    TLV_TYPE_PROCESS_ARGUMENTS = 2305
    TLV_TYPE_PROCESS_ARCH = 2306
    TLV_TYPE_PARENT_PID = 2307
    TLV_TYPE_PROCESS_SESSION = 2308
    TLV_TYPE_PROCESS_ARCH_NAME = 2309
    TLV_TYPE_DRIVER_ENTRY = 2320
    TLV_TYPE_DRIVER_BASENAME = 2321
    TLV_TYPE_DRIVER_FILENAME = 2322
    TLV_TYPE_IMAGE_FILE = 2400
    TLV_TYPE_IMAGE_FILE_PATH = 2401
    TLV_TYPE_PROCEDURE_NAME = 2402
    TLV_TYPE_PROCEDURE_ADDRESS = 2403
    TLV_TYPE_IMAGE_BASE = 2404
    TLV_TYPE_IMAGE_GROUP = 2405
    TLV_TYPE_IMAGE_NAME = 2406
    TLV_TYPE_THREAD_ID = 2500
    TLV_TYPE_THREAD_PERMS = 2502
    TLV_TYPE_EXIT_CODE = 2510
    TLV_TYPE_ENTRY_POINT = 2511
    TLV_TYPE_ENTRY_PARAMETER = 2512
    TLV_TYPE_CREATION_FLAGS = 2513
    TLV_TYPE_REGISTER_NAME = 2540
    TLV_TYPE_REGISTER_SIZE = 2541
    TLV_TYPE_REGISTER_VALUE_32 = 2542
    TLV_TYPE_REGISTER = 2550
    TLV_TYPE_TERMINAL_ROWS = 2600
    TLV_TYPE_TERMINAL_COLUMNS = 2601
    TLV_TYPE_MEMORY_SEARCH_NEEDLE = 2650
    TLV_TYPE_MEMORY_SEARCH_RESULTS = 2651
    TLV_TYPE_MEMORY_SEARCH_MATCH_LEN = 2652
    TLV_TYPE_MEMORY_SEARCH_START_ADDR = 2653
    TLV_TYPE_MEMORY_SEARCH_SECT_LEN = 2654
    TLV_TYPE_MEMORY_SEARCH_MATCH_ADDR = 2655
    TLV_TYPE_MEMORY_SEARCH_MATCH_STR = 2656
    TLV_TYPE_IDLE_TIME = 3000
    TLV_TYPE_KEYS_DUMP = 3001
    TLV_TYPE_DESKTOP_SCREENSHOT = 3002
    TLV_TYPE_DESKTOP_SWITCH = 3003
    TLV_TYPE_DESKTOP = 3004
    TLV_TYPE_DESKTOP_SESSION = 3005
    TLV_TYPE_DESKTOP_STATION = 3006
    TLV_TYPE_DESKTOP_NAME = 3007
    TLV_TYPE_DESKTOP_SCREENSHOT_QUALITY = 3008
    TLV_TYPE_DESKTOP_SCREENSHOT_PE32DLL_BUFFER = 3010
    TLV_TYPE_DESKTOP_SCREENSHOT_PE64DLL_BUFFER = 3012
    TLV_TYPE_KEYSCAN_TRACK_ACTIVE_WINDOW = 3013
    TLV_TYPE_KEYS_SEND = 3014
    TLV_TYPE_MOUSE_ACTION = 3015
    TLV_TYPE_MOUSE_X = 3016
    TLV_TYPE_MOUSE_Y = 3017
    TLV_TYPE_KEYEVENT_SEND = 3018
    TLV_TYPE_EVENT_SOURCENAME = 4000
    TLV_TYPE_EVENT_HANDLE = 4001
    TLV_TYPE_EVENT_NUMRECORDS = 4002
    TLV_TYPE_EVENT_READFLAGS = 4003
    TLV_TYPE_EVENT_RECORDOFFSET = 4004
    TLV_TYPE_EVENT_RECORDNUMBER = 4006
    TLV_TYPE_EVENT_TIMEWRITTEN = 4008
    TLV_TYPE_EVENT_ID = 4009
    TLV_TYPE_EVENT_TYPE = 4010
    TLV_TYPE_EVENT_CATEGORY = 4011
    TLV_TYPE_EVENT_STRING = 4012
    TLV_TYPE_EVENT_DATA = 4013
    TLV_TYPE_POWER_FLAGS = 4100
    TLV_TYPE_POWER_REASON = 4101
