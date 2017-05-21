// Copyright (c) 2017, sathishpy@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('EN Roadmap', {
	refresh: function(frm) {
		frm.add_custom_button(__('Sync From GitHub'),
		  function() {
				frm.events.sync_from_github()
			});
	},
	sync_from_github: function() {
		frappe.call({
			method: "erpnext_roadmap.erpnext_roadmap.doctype.en_roadmap.en_roadmap.sync_from_github",

			callback: function(r) {
				if(!r.exe) {
					msgprint("Returned")
				}
			}
		});
	}
});
