$(document).ready(function() {
    $('#form-search').on('submit', function (e) {
        e.preventDefault();
        var data = {};
        data.request_search = $('#search').val();
        var csrf_token = $('#form-search [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
                url: '/search-ajax-edit/',
                type: 'POST',
                data: data,
                success: function(data){
                    var myData = JSON.parse(data);
                    $('#table-body > tr').remove();
                    $.each(myData, function (index, value) {
                        $('#list-table > tbody:last-child').append($('<tr><td>' + (index+1) +'</td><td>' + value.fields.name + '</td><td>' + value.fields.position + '</td><td>' + value.fields.date_begin + '</td><td>' + value.fields.salary + "</td><td align='center'><img class='avatar' src='/media/" + value.fields.photo + "'></td><td><a href='/delete/" + value.pk + "'>del</a>|<a href='/edit/" + value.pk + "'>edit</a></td></tr>"));
                    });
                }
            });
    });
});

$(document).ready(function() {
    $('#form-search-ajax').on('submit', function (e) {
        e.preventDefault();
        var data = {};
        data.request_search = $('#search-ajax').val();
        var csrf_token = $('#form-search [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
                url: '/search-ajax/',
                type: 'POST',
                data: data,
                success: function(data){
                    var myData = JSON.parse(data);
                    $('#table-body > tr').remove();
                    $.each(myData, function (index, value) {
                        $('#list-table > tbody:last-child').append($('<tr><td>' + (index+1) +'</td><td>' + value.fields.name + '</td><td>' + value.fields.position + '</td><td>' + value.fields.date_begin + '</td><td>' + value.fields.salary + "</td></tr>"));
                    });
                }
            });
    });
});

$(document).ready(function() {
    $('.sort-arrow').click(function () {
        var data = {};
        data.sort_param = $(this).data('sort');
        $.ajax({
                url: '/sorter-ajax?sort=' + data.sort_param,
                type: 'GET',
                success: function(data){
                    var myData = JSON.parse(data);
                    $('#table-body > tr').remove();
                    $.each(myData, function (index, value) {
                        $('#list-table > tbody:last-child').append($("<tr><td>" + (index+1) +"</td><td>" + value.fields.name + "</td><td>" + value.fields.position + "</td><td>" + value.fields.date_begin + "</td><td>" + value.fields.salary + "</td></tr>"));
                    });                }
            });
    });
});

$(document).ready(function() {
    $('.sort-arrow-ajax').click(function () {
        var data = {};
        data.sort_param = $(this).data('sort');
        $.ajax({
                url: '/sorter-ajax?sort=' + data.sort_param,
                type: 'GET',
                success: function(data){
                    var myData = JSON.parse(data);
                    $('#table-body > tr').remove();
                    $.each(myData, function (index, value) {
                        $('#list-table > tbody:last-child').append($('<tr><td>' + (index+1) +'</td><td>' + value.fields.name + '</td><td>' + value.fields.position + '</td><td>' + value.fields.date_begin + '</td><td>' + value.fields.salary + "</td><td align='center'><img class='avatar' src='/media/" + value.fields.photo + "'></td><td><a href='/delete/" + value.pk + "'>del</a>|<a href='/edit/" + value.pk + "'>edit</a></td></tr>"));
                    });                }
            });
    });
});


$(document).ready(function() {
    $('.tree-first').click(function(){
        var level = $(this).data('child')+1;
        $('*[data-child=' + level + ']').css('display','block');
    });
});