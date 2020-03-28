$(function(){
  var arr = { 'admin_phone_number': "websiteuser" };

  $.ajax({
  url: '/api/ema_admin_user_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
          $("#userDataList").append('<tr><td>'+(i+1)+'</td><td>'+msg[r+i]['phone_number']+'</td><td>'+msg[r+i]['date_time_quarantined']+'</td><td>'+msg[r+i]['first_name']+'</td><td>'+msg[r+i]['last_name']+'</td><td>'+msg[r+i]['dob']+'</td><td>'+msg[r+i]['currently_under_quarantine']+'</td><td>'+msg[r+i]['email']+'</td><td>'+msg[r+i]['mo_phone_number']+'</td></tr>');
        }
        $("#userDataListHeader").html("User Data")
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

  $.ajax({
  url: '/api/ema_admin_distress_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userDistressList").append('<tr><td>'+(i+1)+'</td><td>'+msg[r+i]['phone_number']+'</td><td>'+msg[r+i]['Date-time']+'</td><td>'+msg[r+i]['active']+'</td></tr>');
    }
    $("#userDistressListHeader").html("Distress Data")
    }
  });


});
function showMore(e){
  alert(e)
}
