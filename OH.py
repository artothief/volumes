__author__ = 'artothief'

from decimal import *


def dp_oh(csg_shoe, oh_cap, dp_length, dp_ce_cap):
        
    #Pipe / OH
    if 0 < dp_length > csg_shoe:
        dp_oh_vol = (oh_cap - dp_ce_cap) * (dp_length - csg_shoe)
        print dp_length - csg_shoe
    else:
        dp_oh_vol = Decimal('0.00')

    print 'Dp/OH = ' + str(dp_oh_vol)
    return dp_oh_vol


# Tubular / OH volume
def tub_oh(csg_shoe, oh_cap, above_tub, tub_length, tub_ce_cap):

    total_tub = above_tub + tub_length
    if above_tub > csg_shoe and tub_length > 0:
        tub_oh_vol = (oh_cap - tub_ce_cap) * tub_length
        print tub_length

    elif above_tub < csg_shoe <= total_tub:
        tub_oh_vol = (oh_cap - tub_ce_cap) * (total_tub - csg_shoe)
        print total_tub - csg_shoe

    elif 0 < tub_length > csg_shoe:
        tub_oh_vol = (oh_cap - tub_ce_cap) * (tub_length - csg_shoe)

    else:
        tub_oh_vol = Decimal('0.00')

    print 'Tubular/OH = ' + str(tub_oh_vol)
    return tub_oh_vol