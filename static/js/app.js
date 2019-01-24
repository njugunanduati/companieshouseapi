/*jslint browser: true*/
/*global $ */
$(document).ready(function () {
    "use strict";
    $("#searchForm").submit(function (event) {
        event.preventDefault();
        var $form = $(this),
            term = $form.find("input[name='company_name']").val(),
            url = $form.attr("action"),
            method = $form.attr("method");

        $.ajax({
            method: method,
            url: url,
            data: { company_name: term }
        })
        .done(function (data) {
            var result = JSON.parse(data);
            $("#result_data").append(result['message']);
        });
    });
});
