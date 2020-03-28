$(function(){
    var phno = $('#headerboard').data('phno')
    var arr = { 'mo_phone_number': phno };
    $.ajax({
    url: '/api/ema_mo_user_data',
    type: 'POST',
    data: JSON.stringify(arr),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: true,
    success: function(msg) {
        var keys = [];
        for(var k in msg) {
          keys.push(k);

          $("#userDataList").append('<li>'+" "+k+" "+msg[k].first_name+" "+msg[k].last_name+" "+'</li>');
        }
    }
});
});
