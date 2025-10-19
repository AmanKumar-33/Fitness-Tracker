from math import sin,cos,sqrt,atan2,radians

def gpsDistance(p1,p2):
    R = 6373.0
    lat1 = radian(p1[0])
    lon1 = radian(p1[1])
    lat2 = radian(p2[0])
    lon2 = radian(p2[1])


    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c