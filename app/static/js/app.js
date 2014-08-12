App = Ember.Application.create();

App.Router.map(function() {
    this.route("home");
    this.route("home", {path: "/"});
    this.route("players", { path: "/players" });
});

App.IndexRoute = Ember.Route.extend({
  model: function() {
      return this.store.find('tournament');
  }
});

App.HomeRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('tournament');
    }
});

App.PlayersRoute = Ember.Route.extend({
    model: function() {
        return this.store.find('player');
    }
});
