var arr = { 'phc_phone_number': "websiteuser" };

(function ($) {
    $.fn.serializeFormJSON = function () {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function () {
            if (this.value) {
              o[this.name] = this.value
            }
        });
        return o;
    };
})(jQuery);

function searchMore(data){
  $.ajax({
    url: '/api/ema_search_user_data',
    type: 'POST',
    data: JSON.stringify(data),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: true,
    success: function(msg) {
      var count = msg['count']
      m = msg
      var r = "record"
      $("#singleUserData").html('')
      if(count == 0){
        $("#singleUserData").append('<tr><th>No records found. Please try again</th></tr>');
        return;
      }
      $("#singleUserData").append('<tr><th>Ph Number</th><th>Date Quarantined</th><th>First Name</th><th>Last Name</th><th>DOB</th><th>Currently Under Quarantine</th><th>Email</th><th>Mo Phno</th></tr>');
      for (var i=0;i<count;i++){
        msg = m[r+i]
        $("#singleUserData").append('<tr><td>'+msg['phone_number']+'</td><td>'+msg['date_time_quarantined']+'</td><td>'+msg['first_name']+'</td><td>'+msg['last_name']+'</td><td>'+msg['dob']+'</td><td>'+msg['currently_under_quarantine']+'</td><td>'+msg['email']+"</td><td>"+msg['mo_phone_number']+'</td></tr>');
      }
    }
  });
}

$('#userDataSearch').submit(function (e) {
    e.preventDefault();
    var data = $(this).serializeFormJSON();
    if(data['currently_under_quarantine'] == 'on') {
      data['currently_under_quarantine'] = true
    }
    searchMore(data);
    console.log(data);
});

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
      $("#singleUserData").append('<tr><td>'+msg['phone_number']+'</td><td>'+msg['date_time_quarantined']+'</td><td>'+msg['first_name']+'</td><td>'+msg['last_name']+'</td><td>'+msg['dob']+'</td><td>'+msg['currently_under_quarantine']+'</td><td>'+msg['email']+"</td><td>"+msg['mo_phone_number']+'</td></tr>');
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

function emaUserMore(phno){
  $.ajax({
  url: '/api/ema_admin_ema_data',
  type: 'POST',
  data: JSON.stringify({"phone_number":phno}),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
      msg = msg['record0']
      $("#singleUserData").html('<tr><th>EMA Role</th><th>First Name</th><th>Last Name</th><th>Phno</th><th>District</th><th>State</th><th>CHC</th><th>PHC</th></tr>');
      $("#singleUserData").append('<tr><td>'+msg['ema_role']+'</td><td>'+msg['first_name']+'</td><td>'+msg['last_name']+"</td><td>"+msg['phone_number']+'</td><td>'+msg['district']+'</td><td>'+msg['state']+"</td><td>"+msg['chc_phone_number']+"</td><td>"+msg['phc_phone_number']+'</td></tr>');
    }
  });
}

$(function(){

  $.ajax({
  url: '/api/ema_cp_user_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
          $("#userDataList").append('<tr><td>'+(i+1)+"</td><td><a href=# class='userph'>"+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['date_time_quarantined']+'</td><td>'+msg[r+i]['first_name']+'</td><td>'+msg[r+i]['last_name']+'</td><td>'+msg[r+i]['dob']+'</td><td>'+msg[r+i]['currently_under_quarantine']+'</td><td>'+msg[r+i]['email']+"</td><td><a href=# class='emauserph'>"+msg[r+i]['mo_phone_number']+'</a></td></tr>');
        }
        $("#userDataListHeader").html("User Data")
        $('.userph').click(function(event) {
          phno = event.target.innerHTML
          event.preventDefault()
          showMore(phno)
        });
        $('.emauserph').click(function(event) {
          phno = event.target.innerHTML
          event.preventDefault()
          emaUserMore(phno)
        });
    }
  });

  $.ajax({
  url: '/api/ema_cp_temp_data',
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
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
    }
  });

  $.ajax({
  url: '/api/ema_cp_cc_data',
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
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_cp_distress_data',
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
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_cp_lstate_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userLatestStateList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone-number']+'</a></td><td>'+msg[r+i]['lat']+'</td><td>'+msg[r+i]['long']+'</td><td>'+msg[r+i]['date-time']+'</td><td>'+msg[r+i]['distance-from-home']+'</td><td>'+msg[r+i]['proximity-to-home']+'</td><td>'+msg[r+i]['location_enabled']+'</td><td>'+msg[r+i]['Last-face-log']+'</td><td>'+msg[r+i]['Last-temp-log']+'</td></tr>');
    }
    $("#userLatestStateListHeader").html("User Latest State Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      showMore(phno)
    });
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_cp_state_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userStateList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone-number']+'</a></td><td>'+msg[r+i]['lat']+'</td><td>'+msg[r+i]['long']+'</td><td>'+msg[r+i]['date-time']+'</td><td>'+msg[r+i]['distance-from-home']+'</td><td>'+msg[r+i]['proximity-to-home']+'</td><td>'+msg[r+i]['location_enabled']+'</td><td>'+msg[r+i]['Last-face-log']+'</td><td>'+msg[r+i]['Last-temp-log']+'</td></tr>');
    }
    $("#userStateListHeader").html("User State Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      showMore(phno)
    });
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_cp_testing_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userTestList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['date_time']+'</td><td>'+msg[r+i]['test_result']+'</td><td>'+msg[r+i]['other_data']+'</td><td><a href=# class="emauserph">'+msg[r+i]['mo_phone_number']+'</a></td></tr>');
    }
    $("#userTestListHeader").html("Testing Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      showMore(phno)
    });
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_cp_checklist_data',
  type: 'POST',
  data: JSON.stringify(arr),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userChecklistList").append('<tr><td>'+(i+1)+'</td><td><a href=# class="userph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['date_time']+'</td><td>'+msg[r+i]['hygienic_space']+'</td><td>'+msg[r+i]['controlled_symptom']+'</td><td>'+msg[r+i]['stamp_reapply']+'</td><td><a href=# class="emauserph">'+msg[r+i]['mo_phone_number']+'</a></td></tr>');
    }
    $("#userChecklistListHeader").html("Checklist Data")
    $('.userph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      showMore(phno)
    });
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
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

  $.ajax({
  url: '/api/ema_admin_ema_data',
  type: 'POST',
  data: JSON.stringify({'ema_role':'phc', 'chc_phone_number':"websiteuser"}),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#emaPHCList").append('<tr><td>'+(i+1)+'</td><td>'+msg[r+i]['ema_role']+'</td><td>'+msg[r+i]['first_name']+'</a></td><td>'+msg[r+i]['last_name']+'</td><td><a href=# class="emauserph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['district']+'</td><td>'+msg[r+i]['state']+'</td><td><a href=# class="emauserph">'+msg[r+i]['chc_phone_number']+'</a></td></tr>');
    }
    $("#emaPHCListHeader").html("EMA PHCs")
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
  });

  $.ajax({
  url: '/api/ema_admin_ema_data',
  type: 'POST',
  data: JSON.stringify({'ema_role':'mo', 'phc_phone_number':'websiteuser'}),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#emaMOList").append('<tr><td>'+(i+1)+'</td><td>'+msg[r+i]['ema_role']+'</td><td>'+msg[r+i]['first_name']+'</a></td><td>'+msg[r+i]['last_name']+'</td><td><a href=# class="emauserph">'+msg[r+i]['phone_number']+'</a></td><td>'+msg[r+i]['district']+'</td><td>'+msg[r+i]['state']+'</td><td><a href=# class="emauserph">'+msg[r+i]['chc_phone_number']+'</a></td><td><a href=# class="emauserph">'+msg[r+i]['phc_phone_number']+'</a></td></tr>');
    }
    $("#emaMOListHeader").html("EMA MOs")
    $('.emauserph').click(function(event) {
      phno = event.target.innerHTML
      event.preventDefault()
      emaUserMore(phno)
    });
  }
});

});
