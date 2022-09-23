from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.sql import func
import datetime

from enum import Enum
from src.configs import db
import uuid

class Topic(Enum):
    PH = "PH",
    DHT = "DHT" 
    TEMPERATURE = "TEMPERATURE"
    WATER_LEVEL = "WATER_LEVEL"

class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # Could be a brand name or some other identifier
    name = db.Column(db.String())
    topic= db.Column(db.Enum(Topic))
    device_details = db.Column(JSONB)
    token = db.Column(db.String())
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, topic, device_details=None):
        self.name = name
        # Check if this works
        self.topic= Topic.value == topic
        self.device_details = device_details

    def __str__(self):
        return '<id:{0} , type:{1} , created_at {2}>'.format(self.id, self.type, self.created_at)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'type': self.topic,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at,
            'deviceDetails':self.device_details
        }


class Recording(db.Model):
    __tablename__ = 'recording'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    device_id = db.Column(UUID(as_uuid=True), ForeignKey("device.id"))
    topic= db.Column(db.Enum(Topic))
    value = db.Column(db.Float())
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)
    # updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, device_id, topic, value):
        self.device_id = device_id
        # Check if this works
        self.topic = topic
        self.value = value

    def __str__(self):
        return '<id:{0} , type:{1} , value: {2}, created_at: {3}>'.format(
            self.id, self.topic, self.value, self.created_at)
    
    def serialize(self):
        return {
            'id': self.id, 
            'device_id': self.device_id,
            'value':self.value,
            'type': self.topic,
            'createdAt':self.created_at
        }