#!/usr/bin/python3.5
# -*- coding utf-8
from flask import Blueprint, render_template, request, jsonify
import json
from com.kaiji.flask.model.CreditMonitor import CreditMonitor

api = Blueprint(name="api", import_name=__name__)


@api.route("/list", methods=["GET", "POST"])
def lists():
    page = request.args.get("page")
    limit = request.args.get("limit")
    pages = CreditMonitor.query.paginate(int(page), int(limit))
    if pages is None:
        return jsonify({"code": 0, "msg": "", "count": 0, "data": {}})
    else:
        data = []
        for item in pages.items:
            item.__dict__['_sa_instance_state'] = ''
            item.__dict__['create_time'] = "%s" % item.__dict__['create_time']
            item.__dict__['monitor_time'] = "%s" % item.__dict__['monitor_time']
            data.append(item.__dict__)

        return json.dumps({"code": 0, "msg": "", "count": pages.total, "data": data})