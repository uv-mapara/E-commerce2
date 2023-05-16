/*START - SAVE DATA OPERATIONS*/
$("#btnSubmit").click(function () {
    signup();
});
function signup() {
    debugger;
    var ErrMsg = '';

    if ($("#firstname").val().trim() == '') {
        ErrMsg += '<br/>-- Firstname.';
    }
    if ($("#lastname").val().trim() == '') {
        ErrMsg += '<br/>-- Lastname.';
    }
    if ($('#email').val().trim() == '') {
        ErrMsg += '<br/>-- E-mail ID.';
    }
    else {
        var Valid = validateEmail($("#email").val().trim());
        if (!Valid) {
            ErrMsg += '<br/>-- Invalid E-mail ID.';
        }
    }

    if ($("#phone").val().trim() == '') {
        ErrMsg += '<br/>-- Mobile.';
    }

    if ($("#password").val().trim() == '') {
        ErrMsg += '<br/>-- Password.';
    }    
    
    if (ErrMsg.length != 0) {
        ShowMessage('DivDisplayMsg', "alert alert-warning TextBlack", "Please check below.", '<br/>' + ErrMsg, 0);
    }

    else {
        ShowLoader();
        $.ajax({
            url: '/signup/',
            type: 'POST',
            data: {
                firstname: $('#firstname').val().trim(),
                lastname: $('#lastname').val().trim(),
                email: $('#email').val().trim(),
                phone: $('#phone').val().trim(),
                password: $('#password').val().trim(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            dataType: 'json',
            success: function (resp) {
                HideMessage("DivDisplayMsg");
                setTimeout(HideLoader, 2000);
                console.log(resp.opstatus)
                if (resp.opstatus == "Error") {
                    setTimeout(function () {
                        email = "-- Email has already Exist."
                        ShowMessage('DivDisplayMsg', "alert alert-warning TextBlack", "Please check below.", '<br/>' + email, 0);
                    }, 2000)
                }
                else {
                    HideLoader();
                    setTimeout(function () {
                        window.location.href = "/signupAuthentication/";
                    }, 2000)
                    $("#firstname").val('');
                    $("#lastname").val('');
                    $("#email").val('');
                    $("#phone").val('');
                    $("#password").val('');                    
                }
            },
        });
    }
}
/*END - SAVE DATA OPERATIONS*/