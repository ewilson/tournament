App = Ember.Application.create();

App.Router.map(function() {
    this.route("home");
    this.route("home", {path: "/"});
    this.route("players", { path: "/players" });
});

App.ApplicationAdapter = DS.FixtureAdapter.extend();

App.IndexRoute = Ember.Route.extend({
  model: function() {
    return ['red', 'yellow', 'blue'];
  }
});

App.HomeRoute = Ember.Route.extend({
    model: function() {
        return ['red', 'yellow', 'black'];
    }
});

App.PlayersRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('player');
    }
});
