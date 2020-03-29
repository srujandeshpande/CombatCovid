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

function cmaUserMore(phno){
  ar2 = {"phone_number":phno}
  $.ajax({
  url: '/api/ema_single_cma_user_data',
  type: 'POST',
  data: JSON.stringify(ar2),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
      $("#singleUserData").html('<tr><th>Ph Number</th><th>Date Created</th><th>First Name</th><th>Last Name</th><th>DOB</th><th>Email</th></tr>');
      $("#singleUserData").append('<tr><td>'+msg['phone_number']+'</td><td>'+msg['date_time_created']+'</td><td>'+msg['first_name']+'</td><td>'+msg['last_name']+'</td><td>'+msg['dob']+'</td><td>'+msg['email']+'</td></tr>');
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
          event.preventDefault()
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
      event.preventDefault()
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
      event.preventDefault()
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
      event.preventDefault()
      showMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_admin_testing_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userTestList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['date_time']+'</td><td>'+msg[r+i]['test_result']+'</td><td>'+msg[r+i]['other_data']+'</td><td>'+msg[r+i]['mo_phone_number']+'</td></tr>');
    }
    $("#userTestListHeader").html("Testing Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      showMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_admin_checklist_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userChecklistList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['date_time']+'</td><td>'+msg[r+i]['hygenic_space']+'</td><td>'+msg[r+i]['controlled_symptom']+'</td><td>'+msg[r+i]['stamp_reapply']+'</td><td>'+msg[r+i]['mo_phone_number']+'</td></tr>');
    }
    $("#userChecklistListHeader").html("Checklist Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      showMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_admin_request_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userRequestList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="cmauserph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['name']+'</a></td><td>'+msg[r+i]['date_time']+'</td><td>'+msg[r+i]['symptom']+'</td><td>'+msg[r+i]['travel']+'</td><td>'+msg[r+i]['contact']+'</td><td>'+msg[r+i]['dob']+'</td></tr>');
    }
    $("#userRequestListHeader").html("CMA User Request to be Checked")
    $('.cmauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      cmaUserMore(phno)
    });
  }
  });
});
