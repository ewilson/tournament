App.TournamentsController = Ember.ArrayController.extend({
    actions: {
        createTournament: function() {
            console.log('gots it');
            var description = this.get('newDescription');
            if (!description || !description.trim()) { return false; }

            var tournament = this.store.createRecord('tournament', {
                description: description
            });

            var onFail = function(response) {
                alert(response.responseText);
                tournament.rollback();
            };

            this.set('newDescription', '');
            tournament.save().then(function() {}, onFail);
        }
    }
});
