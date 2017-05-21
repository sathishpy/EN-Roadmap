// Copyright (c) 2017, sathishpy@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('EN Roadmap Item', {
	setup: function(frm) {
		frm.get_field('feature_support').grid.editable_fields = [
				{fieldname: 'user', columns: 2},
				{fieldname: 'bounty', columns: 2},
				{fieldname: 'dev_days', columns: 2}
			];
		frm.get_field('feature_votes').grid.editable_fields = [
				{fieldname: 'user', columns: 2},
			];
	},

	refresh: function(frm) {
		frm.add_custom_button(__('Upvote'),
		  function() {
				frm.events.upvote_feature(frm)
			});

		frm.add_custom_button(__('Add Bounty - $100'),
			  function() {
					frm.events.add_bounty(frm)
				});

		frm.add_custom_button(__('Donate Dev - 5 Eng Days'),
			  function() {
					frm.events.donate_dev(frm)
				});
	},

	upvote_feature: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "add_vote",
			callback: function(r) {
				msgprint(r.exe)
				if(!r.exe) {
					refresh_field("total_votes");
					refresh_field("feature_votes");
				}
			}
		});
	},

	add_bounty: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "add_bounty",
			callback: function(r) {
				if(!r.exe) {
					refresh_field("total_bounty");
					refresh_field("feature_support");
				}
			}
		});
	},
	donate_dev: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "add_dev_days",
			callback: function(r) {
				if(!r.exe) {
					refresh_field("total_dev_days");
					refresh_field("feature_support");
				}
			}
		});
	},
});
