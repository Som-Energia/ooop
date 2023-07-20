from __future__ import print_function
from ooop import OOOP

o = OOOP(dbname="testv6")
partners = o.ResPartner.all()
for partner in partners:
    print("id: %d, name: %s" % ( partner._ref, partner.name ))