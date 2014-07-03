var Player = Backbone.Model.extend({
    urlRoot: '/api/player',
    validate: function( attributes ) {
        if (attributes.fname === '') {
            bootbox.alert('Name field is required.');
            return 'Invalid';
        }
    }
});