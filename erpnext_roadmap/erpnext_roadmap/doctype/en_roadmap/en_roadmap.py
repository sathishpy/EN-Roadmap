# -*- coding: utf-8 -*-
# Copyright (c) 2017, sathishpy@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
import urllib, urllib2

class ENRoadmap(Document):
	pass

@frappe.whitelist()
def sync_from_github():
	url = "https://api.github.com/repos/frappe/erpnext/issues?state=open&labels=framework"
	#quoted_url = url + urllib.quote("?state=open&labels=framework")
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0')
	response = urllib2.urlopen(req)
	data = response.read()
	issues = json.loads(data)
	for issue in issues:
		print "title:{0} number:{1} state:{2}".format(issue["title"], issue["number"], issue["state"])
		name = "GI-" + str(issue["number"])
		if not frappe.db.exists("EN Roadmap Item", name):
			print "Creating roadmap item {0}".format(issue["number"])
			roadmap_item = frappe.new_doc("EN Roadmap Item")
			roadmap_item.github_id = issue["number"]
			roadmap_item.feature_name = issue["title"]
			roadmap_item.feature_description = issue["body"]
			roadmap_item.save()
	return "Sync Complete"
