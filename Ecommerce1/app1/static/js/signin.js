$('#btnSubmit').click(function () {
    ShowLoader();
    $.ajax({
        url: '/signin/',
        type: 'POST',
        data: {
            email: $('#email').val(),
            password: $('#password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: "json",
        success: function (resp) {            
            if (resp.optstatus == 'success') {
                console.log(resp)
                HideLoader();
                $('#email').val(),
                $('#password').val(),                
                window.history.back();
            }
            else if (resp.optstatus == 'error') {
                HideLoader();
                window.location.href = "login";
            }
        }
    });
});