$('#productSize').on('change', function () {
    var selectedValue = $(this).val(); 
    if ($(this).val() == '0') {
        $('#AvailableSize').text('')
    }
    else {
        $('#AvailableSize').text(`only ` + selectedValue + ` product available.`)
    }    
});