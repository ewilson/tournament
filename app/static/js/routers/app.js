app.ApplicationRouter = Backbone.Router.extend({

	initialize: function(el) {
		this.el = el;

		this.loremView = new app.ContentView({template: '#home'});
		this.playersView = new app.PlayersView();
		this.notFoundView = new app.ContentView({template: '#not-found'});
	},

	routes: {
		"": "home",
		"home": "home",
		"players": "players",
		"*else": "notFound"
	},

	currentView: null,

	switchView: function(view) {
		if (this.currentView) {
			// Detach the old view
			this.currentView.remove();
		}

		// Move the view element into the DOM (replacing the old content)
		this.el.html(view.el);

		// Render view after it is in the DOM (styles are applied)
		view.render();

		this.currentView = view;
	},

	 // Change the active element in the topbar
	setActiveEntry: function(url) {
		// Unmark all entries
		$('li').removeClass('active');

		// Mark active entry
		$("li a[href='" + url + "']").parents('li').addClass('active');
	},

	home: function() {
		this.switchView(this.loremView);
		this.setActiveEntry('#home');
	},

	players: function() {
		this.switchView(this.playersView);
		this.setActiveEntry('#players');
	},

	notFound: function() {
		this.switchView(this.notFoundView);
	}

});
