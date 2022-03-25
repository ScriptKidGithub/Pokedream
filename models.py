from tortoise.models import Model
import tortoise.fields as fields


class Guild(Model):
    guild_id = fields.BigIntField(pk=True, index=True)
    prefix = fields.CharField(max_length=3, default="p!")
    blacklisted = fields.BooleanField(default=False)


class Trainer(Model):
    trainer_id = fields.BigIntField(pk=True)
    started_at = fields.DatetimeField()
    suspended = fields.BooleanField(default=False)
    suspension_reason = fields.TextField(default=None, null=True)

    balance = fields.BigIntField(default=0)
     = fields.BigIntField(default=0)
    shards = fields.BigIntField(default=0)
    gifts = 
