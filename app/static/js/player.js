$(document).ready(function() {
    $('#new-player form').submit(function(e) {
        e.preventDefault();

        $.ajax({
            url: $SCRIPT_ROOT + '/_add-player',
            type: 'POST',
            dataType: 'json',
            data: { text: $('#fname').val() },
            success: function(data) {
                $('#players').append('<li>' + data.text + '</li>');
                $('#fname').val('');
            }
        });
    });
});
