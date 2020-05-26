$(document).ready(function() {
            $('#list').click(function(event){event.preventDefault();$('#projects .item').addClass('list-group-item');});
            $('#grid').click(function(event){event.preventDefault();$('#projects .item').removeClass('list-group-item');$('#projects .item').addClass('grid-group-item');});
        });