__author__ = 'artothief'

from decimal import *


#Pipe / Riser volume
def dp_riser(seabed, riser_cap, dp_length, dp_ce_cap):

    if riser_cap < dp_ce_cap:
        print 'Tubular is bigger than riser'

    if 0 < dp_length >= seabed:
        riser_dp_vol = (riser_cap - dp_ce_cap) * seabed
        print seabed

    elif 0 < dp_length < seabed:
        riser_dp_vol = (riser_cap - dp_ce_cap) * dp_length
        print dp_length

    else:
        riser_dp_vol = Decimal('0.00')

    print 'DP/Riser = ' + str(riser_dp_vol)
    return riser_dp_vol


def tub_riser(seabed, riser_cap, above_tub, tub_length, tub_ce_cap):

    if riser_cap < tub_ce_cap:
        print 'Tubular is bigger than riser'

    if above_tub >= seabed:
        riser_tub_vol = Decimal('0.00')

    elif above_tub < seabed <= above_tub + tub_length:
        riser_tub_vol = (riser_cap - tub_ce_cap) * (seabed - above_tub)
        print seabed - above_tub
    else:
        riser_tub_vol = (riser_cap - tub_ce_cap) * tub_length
        if tub_length != Decimal('0.00'):
            print tub_length
        else:
            pass

    print 'Tubular/Riser = ' + str(riser_tub_vol)
    return riser_tub_vol
