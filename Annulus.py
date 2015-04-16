__author__ = 'artothief'

from decimal import *


# Pipe / Riser volume
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


# Tubular / Riser volume
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


# Pipe/Liner volume
def dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap):

    if liner_cap < dp_ce_cap:
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


# Pipe / OH
def dp_oh(csg_shoe, oh_cap, dp_length, dp_ce_cap):

    if oh_cap < dp_ce_cap:
        print 'Tubular is bigger than open hole'

    if 0 < dp_length > csg_shoe:
        dp_oh_vol = (oh_cap - dp_ce_cap) * (dp_length - csg_shoe)
        print dp_length - csg_shoe
    else:
        dp_oh_vol = Decimal('0.00')

    print 'Dp/OH = ' + str(dp_oh_vol)
    return dp_oh_vol


# Tubular / OH volume
def tub_oh(csg_shoe, oh_cap, above_tub, tub_length, tub_ce_cap):

    if oh_cap < tub_ce_cap:
        print 'Tubular is bigger than open hole'

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


