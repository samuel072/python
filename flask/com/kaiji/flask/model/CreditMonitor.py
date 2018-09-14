#!/usr/bin/python3.5
# -*- coding utf-8
from com.kaiji.flask.model.db import db


class CreditMonitor(db.Model):
    __tablename__ = "f_credit_monitor"
    id = db.Column(db.String, primary_key=True)
    credit_type = db.Column('credit_type', db.String(128))
    query_type = db.Column('query_type', db.String(128))
    credit_status = db.Column('credit_status', db.String(128))
    monitor_time = db.Column('monitor_time', db.String(128))
    elapsed_time = db.Column('elapsed_time', db.String(128))
    create_time = db.Column('create_time', db.String(128))

    def __init__(self, id, credit_type, query_type, credit_status, monitor_time, elapsed_time, create_time):
        self.id = id
        self.credit_type = credit_type
        self.query_type = query_type
        self.credit_status = credit_status
        self.monitor_time = monitor_time
        self.elapsed_time = elapsed_time
        self.create_time = create_time

