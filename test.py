import time

import DWX_ZeroMQ_Connector_v2_0_1_RC8 as dwx
from time import sleep


_pulldata_handlers = []
_subdata_handlers = []
_verbose=False
_delay = 0.1
_wbreak = 10

_zmq = dwx.DWX_ZeroMQ_Connector(_pulldata_handlers=_pulldata_handlers,
                                 _subdata_handlers=_subdata_handlers,
                                 _verbose=_verbose)
#
# _zmq._set_response_(None)
#
# while _zmq._valid_response_('zmq') == False:
#     sleep(_delay)
#
#
#
# print(_zmq._get_response_())


_zmq._DWX_MTX_SUBSCRIBE_MARKETDATA_('BTCUSDm')

# _zmq._DWX_MTX_SEND_TRACKPRICES_REQUEST_([('BTCUSDm',0.01)])

# time.sleep(5)
for i in range(10):
    time.sleep(_delay) #必须睡眠拿数据
    #{'BTCUSDm': {'2025-03-01 11:58:24.190618': (84670.12, 84698.92), '2025-03-01 11:58:24.691377': (84671.35, 84700.15)}}
    print(_zmq._Market_Data_DB)