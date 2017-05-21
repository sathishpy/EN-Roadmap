frappe.listview_settings['EN Roadmap Item'] = {
  onload: function(listview) {
    listview.page.add_menu_item(__("GitHub Sync"), function() {
      frappe.call({
  			method: "erpnext_roadmap.erpnext_roadmap.doctype.en_roadmap_item.en_roadmap_item.sync_from_github",

  			callback: function(r) {
  				if(!r.exe) {
  					msgprint("Added items:" + r.message.Added)
  				}
  			}
  		});
    });
  }
};
