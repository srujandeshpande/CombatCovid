$(function(){
  var arr = { 'mo_phone_number': "websiteuser" };
  var keys = [];
  $.ajax({
  url: '/api/ema_mo_user_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
        for(var k in msg) {
          keys.push(k);
          $("#userDataList").append("<li><a id='induser' data-phno="+k+'>'+" "+k+" "+msg[k].first_name+" "+msg[k].last_name+" "+'</a></li>');
          $("#userDataListHeader").html("User Data")
        }
    }
});
  $("a").click(function() {
    var phno = $(this).data("phno")
    alert(phno)
  });
});
