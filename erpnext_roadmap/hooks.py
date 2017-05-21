# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_roadmap"
app_title = "ERPNext Roadmap"
app_publisher = "sathishpy@gmail.com"
app_description = "Roadmap tool for ERPNext project"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "sathishpy@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_roadmap/css/erpnext_roadmap.css"
# app_include_js = "/assets/erpnext_roadmap/js/erpnext_roadmap.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_roadmap/css/erpnext_roadmap.css"
# web_include_js = "/assets/erpnext_roadmap/js/erpnext_roadmap.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_roadmap.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_roadmap.install.before_install"
# after_install = "erpnext_roadmap.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_roadmap.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_roadmap.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_roadmap.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_roadmap.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_roadmap.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_roadmap.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_roadmap.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_roadmap.event.get_events"
# }

