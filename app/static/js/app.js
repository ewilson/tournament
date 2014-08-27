App = Ember.Application.create();

App.ApplicationAdapter = DS.FixtureAdapter.extend();

App.Router.map(function() {
    this.resource("tournaments", {path: "/"});
});

App.TournamentsRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('tournament');
    }
});
