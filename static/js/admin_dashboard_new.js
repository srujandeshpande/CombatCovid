var arr = { 'admin_phone_number': "websiteuser" };

function showMore(phno){
  ar2 = {"phone_number":phno}
  $.ajax({
  url: '/api/ema_single_user_data',
  type: 'POST',
  data: JSON.stringify(ar2),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
      $("#singleUserData").html('<tr><th>Ph Number</th><th>Date Quarantined</th><th>First Name</th><th>Last Name</th><th>DOB</th><th>Currently Under Quarantine</th><th>Email</th><th>Mo Phno</th></tr>');
      $("#singleUserData").append('<tr><td>'+msg['phone_number']+'</td><td>'+msg['date_time_quarantined']+'</td><td>'+msg['first_name']+'</td><td>'+msg['last_name']+'</td><td>'+msg['dob']+'</td><td>'+msg['currently_under_quarantine']+'</td><td>'+msg['email']+'</td><td>'+msg['mo_phone_number']+'</td></tr>');
    }
  });
}


$(function(){

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
          $("#userDataList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['date_time_quarantined']+'</td><td>'+msg[r+i]['first_name']+'</td><td>'+msg[r+i]['last_name']+'</td><td>'+msg[r+i]['dob']+'</td><td>'+msg[r+i]['currently_under_quarantine']+'</td><td>'+msg[r+i]['email']+'</td><td>'+msg[r+i]['mo_phone_number']+'</td></tr>');
        }
        $("#userDataListHeader").html("User Data")
        $('.userph').click(function(event) {
          phno = event.target.innerHTML
          showMore(phno)
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
      $("#userTempList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['temperature']+'</td><td>'+msg[r+i]['Date-time']+'</td></tr>');
    }
    $("#userTempListHeader").html("Temperature Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      showMore(phno)
    });
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
      $("#userCCList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['Date-time']+'</td><td>'+msg[r+i]['contact-pno']+'</td><td>'+msg[r+i]['contact-name']+'</td><td>'+msg[r+i]['contact-address']+'</td></tr>');
    }
    $("#userCCListHeader").html("Close Contact Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      showMore(phno)
    });
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
      $("#userDistressList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['Date-time']+'</td><td>'+msg[r+i]['active']+'</td></tr>');
    }
    $("#userDistressListHeader").html("Distress Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      showMore(phno)
    });
  }
  });

});
