// Override View.remove()'s default behavior
Backbone.View = Backbone.View.extend({

    remove: function() {
        // Empty the element and remove it from the DOM while preserving events
        $(this.el).empty().detach();

        return this;
    }

});

var ContentView = Backbone.View.extend({

    /*
     * Initialize with the template-id
     */
    initialize: function(options) {
        this.template = options.template;
    },

    /*
     * Get the template content and render it into a new div-element
     */
    render: function() {
        var content = $(this.template).html();
        $(this.el).html(content);

        return this;
    }

});
