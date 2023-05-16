
$('#slideclick').click(function () {
    $('#slideshow').slideToggle();
    $(this).children('.icon-chevron-right').toggleClass('toggle');
});

function MinusQuantity(ele) {
    if ($(ele).next().val() > 1) {
        if ($(ele).next().val() > 1) $(ele).next().val(+$(ele).next().val() - 1);
    }
}

function AddQuantity(ele) {
    stock = $(ele).next('.product-stock').val(); 
    
    var intValue = parseInt(stock);
   
    if ($(ele).prev().val() < intValue) {        
        $(ele).prev().val(+$(ele).prev().val() + 1);
    }
}


function SaveAddToCart(ele) {
    addcart = $(ele).attr('id');
    quantity = $('.input-qty').val();
    $.ajax({
        url: '/addtocart/' + addcart + '/',
        type: "POST",
        data: {
            quantity: quantity,
            addcart: addcart,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (resp) {
            if (resp.optstatus == 'added') {
                /*window.location.href = window.location.href;*/
                window.location.href = window.location.href;
                HideToastrMsg();
                ShowToastrMsg("Success", "toast-top-full-width", "Cart Added SuccessFully.", "", 15000);
            }
            else if (resp.optstatus == 'exists') {
                HideToastrMsg();
                window.location.href = window.location.href;
            }
            else {
                window.location.href = '/signin/';
            }
        },
    });
}