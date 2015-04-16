__author__ = 'artothief'

from decimal import *


# Pipe / Csg volume
def dp_csg(seabed, csg_shoe, csg_cap, dp_length, dp_ce_cap):

    if csg_cap < dp_ce_cap:
        print 'Tubular is bigger than casing'

    if 0 < dp_length >= csg_shoe:
        pipe_csg_vol = (csg_cap - dp_ce_cap) * (csg_shoe - seabed)
        print csg_shoe - seabed

    elif seabed < dp_length < csg_shoe:
        pipe_csg_vol = (csg_cap - dp_ce_cap) * (dp_length - seabed)
        print dp_length - seabed

    else:
        pipe_csg_vol = Decimal('0.00')

    print 'DP/Csg = ' + str(pipe_csg_vol)
    return pipe_csg_vol


# Tubular / Csg volume
def tub_csg(seabed, csg_shoe, csg_cap, above_tub, tub_length, tub_ce_cap):
    
    if csg_cap < tub_ce_cap:
        print 'Tubular is bigger than casing'

    total_tub = above_tub + tub_length
    if above_tub >= seabed and total_tub <= csg_shoe and tub_length > 0:
        tub_csg_vol = (csg_cap - tub_ce_cap) * tub_length
        print tub_length

    elif csg_shoe > total_tub > seabed > above_tub > 0:
        tub_csg_vol = (csg_cap - tub_ce_cap) * (total_tub - seabed)
        print total_tub - seabed

    elif total_tub > csg_shoe > above_tub > seabed:
        tub_csg_vol = (csg_cap - tub_ce_cap) * ((csg_shoe - seabed) - (above_tub - seabed))
        print (csg_shoe - seabed) - (above_tub - seabed)

    elif above_tub <= seabed and above_tub + tub_length >= csg_shoe:
        tub_csg_vol = (csg_cap - tub_ce_cap) * (csg_shoe - seabed)
        print csg_shoe - seabed

    else:
        tub_csg_vol = Decimal('0.00')

    print 'Tubular/Csg = ' + str(tub_csg_vol)
    return tub_csg_vol