import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
import umongo.fields as fields
from umongo import Document



class Trainer(Document):
    class Meta:
        strict = False

    trainer_id = fields.IntegerField(attribute="_id")
    started_at = fields.DateTimeField(default=None)
    suspended = fields.BooleanField(default=False)
    suspension_reason = fields.StringField(default=None)

    balance = fields.IntegerField(default=0)
    gems = fields.IntegerField(default=0)
    redeems = fields.IntegerField(default=0)
    gifts = fields.IntegerField(default=0)

    show_trainer_stats = fields.BooleanField(default=True)
