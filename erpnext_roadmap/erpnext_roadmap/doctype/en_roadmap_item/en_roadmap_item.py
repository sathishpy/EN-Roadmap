# -*- coding: utf-8 -*-
# Copyright (c) 2017, sathishpy@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
import urllib, urllib2

class ENRoadmapItem(Document):
	def autoname(self):
		self.name = "GI-" + str(self.github_id)

	def add_bounty(self):
		bounty_amount = 100
		self.total_bounty += bounty_amount

		for support in self.feature_support:
			if support.user == frappe.session.user:
				support.bounty += bounty_amount
				self.save()
				return {"Result": True}

		support_entry = frappe.new_doc("SupportMap")
		support_entry.user = frappe.session.user
		support_entry.bounty = bounty_amount
		self.append("feature_support", support_entry)
		self.save()
		return {"Result": True}

	def add_dev_days(self):
		dev_days = 5
		self.total_dev_days += dev_days

		for support in self.feature_support:
			if support.user == frappe.session.user:
				support.dev_days += dev_days
				self.save()
				return {"Result": True}

		support_entry = frappe.new_doc("SupportMap")
		support_entry.user = frappe.session.user
		support_entry.dev_days = dev_days
		self.append("feature_support", support_entry)
		self.save()
		return {"Result": True}

	def add_vote(self):
		present = False
		for vote in self.feature_votes:
			if vote.user == frappe.session.user:
				present = True
				break

		if not present:
			self.total_votes += 1
			vote_entry = frappe.new_doc("VoteList")
			vote_entry.user = frappe.session.user
			self.append("feature_votes", vote_entry)
			self.save()
			return {"Result": True}
		else:
			return {"Result": False}

@frappe.whitelist()
def sync_from_github():
	url = "https://api.github.com/repos/frappe/erpnext/issues?state=open&labels=framework"
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0')
	response = urllib2.urlopen(req)
	data = response.read()
	issues = json.loads(data)
	updates = 0
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
			updates += 1
	return {"Added": updates}
