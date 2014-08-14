App.TournamentController = Ember.ObjectController.extend({
    actions: {
        removeTournament: function() {
            var tournament = this.get('model');

            if (confirm("Are you sure? There is no undelete?")) {
                var onFail = function(response) {
                    alert(response.responseText);
                    tournament.rollback();
                };

                tournament.deleteRecord();
                tournament.save().then(function() {}, onFail);
            }
        }
    }
});