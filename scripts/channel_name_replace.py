#!/usr/bin/python
# ================================
# (C)2023 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# search and replace selected user channel names


import lx

import h3d_utilites.scripts.h3d_utils as h3du
from h3d_utilites.scripts.h3d_exceptions import H3dExitException


USERVAL_CNR_SEARCH_NAME = 'h3d_cnr_search'
USERVAL_CNR_REPLACE_NAME = 'h3d_cnr_replace'


def main():
    SEARCH_STR = h3du.get_user_value(USERVAL_CNR_SEARCH_NAME)
    REPLACE_STR = h3du.get_user_value(USERVAL_CNR_REPLACE_NAME)

    selection_service = lx.service.Selection()
    chan_sel_type = selection_service.LookupType(lx.symbol.sSELTYP_CHANNEL)

    chan_transpacket = lx.object.ChannelPacketTranslation(selection_service.Allocate(lx.symbol.sSELTYP_CHANNEL))

    chan_n = selection_service.Count(chan_sel_type)

    if not chan_n:
        return

    for x in range(chan_n):
        packet_pointer = selection_service.ByIndex(chan_sel_type, x)
        if not packet_pointer:
            lx.out('Bad selection packet, skipping...')
            continue

        item = lx.object.Item(chan_transpacket.Item(packet_pointer))
        chan_idx = chan_transpacket.Index(packet_pointer)
        # item_id = item.UniqueName()
        item_id = item.Ident()
        channel_id = item.ChannelName(chan_idx)
        # lx.out('%s : %s' % (item_id, channel_id))
        username = lx.eval('channel.username channel:{{{}:{}}} username:?'.format(item_id, channel_id))
        new_username = '{}'.format(username).replace(SEARCH_STR, REPLACE_STR)
        # print(username, new_username)
        lx.eval('channel.username channel:{{{}:{}}} username:{{{}}}'.format(item_id, channel_id, new_username))


if __name__ == '__main__':
    try:
        main()
    except H3dExitException as e:
        print(e.message)
