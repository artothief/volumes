__author__ = 'artothief'

from decimal import *


#Pipe/Liner volume
def dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap):

    if liner_cap < tub_ce_cap:
        print 'Tubular is bigger than liner'

    if 0 < dp_length >= liner_shoe:
        dp_liner_vol = (liner_cap - dp_ce_cap) * (liner_shoe - pbr)
        print liner_shoe - pbr

    elif pbr < dp_length <= liner_shoe:
        dp_liner_vol = (liner_cap - dp_ce_cap) * (dp_length - pbr)
        print dp_length - pbr

    else:
        dp_liner_vol = Decimal('0.00')

    print 'DP/Liner = ' + str(dp_liner_vol)
    return dp_liner_vol


# Tubular/Liner volume
def tub_liner(pbr, liner_shoe, liner_cap, above_tub, tub_length, tub_ce_cap):

    if liner_cap < tub_ce_cap:
        print 'Tubular is bigger than liner'

    total_tub = above_tub + tub_length
    if above_tub >= pbr and total_tub <= liner_shoe and tub_length > 0:
        tub_liner_vol = (liner_cap - tub_ce_cap) * tub_length
        print tub_length

    elif liner_shoe > total_tub > pbr > above_tub > 0:
        tub_liner_vol = (liner_cap - tub_ce_cap) * (total_tub - pbr)
        print total_tub - pbr

    elif total_tub > liner_shoe > above_tub > pbr:
        tub_liner_vol = (liner_cap - tub_ce_cap) * (liner_shoe - above_tub)
        print liner_shoe - above_tub

    elif above_tub <= pbr and above_tub + tub_length >= liner_shoe:
        tub_liner_vol = (liner_cap - tub_ce_cap) * (liner_shoe - pbr)
        print liner_shoe - pbr

    else:
        tub_liner_vol = Decimal('0.00')

    print 'Tubular /Liner = ' + str(tub_liner_vol)
    return tub_liner_vol
