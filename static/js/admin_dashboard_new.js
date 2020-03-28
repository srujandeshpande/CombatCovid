$(function(){
  var arr = { 'admin_phone_number': "websiteuser" };
  var keys = [];
  $.ajax({
  url: '/api/ema_admin_user_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
        for(var k in msg) {
          keys.push(k);
          $("#userDataList").append("<li><a id='induser' onclick=showMore("+k+')>'+" "+k+" "+msg[k].first_name+" "+msg[k].last_name+" "+'</a></li>');
          $("#userDataListHeader").html("User Data")
        }
        $('#induser').click(function() {
          //var phno = $(this).data("phno")
          alert("phno");
        });
    }
  });
  $.ajax({
  url: '/api/ema_admin_temp_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userTempList").append('<tr><td>'+(i+1)+'</td><td>'+msg[r+i]['phone_number']+'</td><td>'+msg[r+i]['temperature']+'</td><td>'+msg[r+i]['Date-time']+'</td></tr>');
    }
    $("#userTempListHeader").html("Temperature Data")
        /*
        $('#induser').click(function() {
          //var phno = $(this).data("phno")
          alert("phno");
        });
        */
    }
  });
  $.ajax({
  url: '/api/ema_admin_cc_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userCCList").append('<tr><td>'+(i+1)+'</td><td>'+msg[r+i]['phone_number']+'</td><td>'+msg[r+i]['Date-time']+'</td><td>'+msg[r+i]['contact-pno']+'</td><td>'+msg[r+i]['contact-name']+'</td><td>'+msg[r+i]['contact-address']+'</td></tr>');
    }
    $("#userCCListHeader").html("Close Contact Data")
    }
  });



});
function showMore(e){
  alert(e)
}
