var app = app || {};
var ENTER_KEY = 13;
var ESC_KEY = 27;

$(function () {
    'use strict';

    new app.ApplicationRouter($('#content'));
    Backbone.history.start();

    new app.AppView();

});