# -*- coding: utf8 -*-

import ots2.const as const

const.HEADER = 0x75

# tag type
const.TAG_ROW_PK = 0x1
const.TAG_ROW_DATA = 0x2
const.TAG_CELL = 0x3
const.TAG_CELL_NAME = 0x4
const.TAG_CELL_VALUE = 0x5
const.TAG_CELL_TYPE = 0x6
const.TAG_CELL_TIMESTAMP = 0x7
const.TAG_DELETE_ROW_MARKER = 0x8
const.TAG_ROW_CHECKSUM = 0x9
const.TAG_CELL_CHECKSUM = 0x0A

# cell op type
const.DELETE_ALL_VERSION = 0x1
const.DELETE_ONE_VERSION = 0x3

# variant type
const.VT_INTEGER = 0x0
const.VT_DOUBLE = 0x1
const.VT_BOOLEAN = 0x2
const.VT_STRING = 0x3
const.VT_NULL = 0x6
const.VT_BLOB = 0x7
const.VT_INF_MIN = 0x9
const.VT_INF_MAX = 0xa
const.VT_AUTO_INCREMENT = 0xb

# othber
const.LITTLE_ENDIAN_32_SIZE = 4
const.LITTLE_ENDIAN_64_SIZE = 8
const.MAX_BUFFER_SIZE = 64 * 1024 * 1024

