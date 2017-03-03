from datetime import datetime
from db import *

database.connect()


for i in Dmoz.select():
    print i.description
    print i.__dict__

for i in range(10):
    print Dmoz.create(description="user", link="HuaDong", title="100000%s" % str(i))



    # cityname = CharField(null=True)
    # createdesc = CharField(null=True)
    # createtime = BigIntegerField(null=True)
    # model = CharField(null=True)
    # phone = CharField(null=True)
