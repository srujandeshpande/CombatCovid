var map, datasource, client, popup, searchInput, resultsPanel, searchInputLength, centerMapOnResults;
var xcoords = 0;
var ycoords = 0;
var zoombtn = 0;
  function GetMap() {
    map = new atlas.Map('myMap', {
      center: [xcoords,ycoords],
      zoom: 11,
      view: 'Auto',
      authOptions: {
        authType: 'subscriptionKey',
        subscriptionKey: '9IzBADFYR5w43nQRBqJRXG0d2OyVe55caezwWz0fIE4'
      }
    });
    map.events.add('ready', function () {
      if (zoombtn == 0){
      map.controls.add(new atlas.control.ZoomControl(), {
        position: 'top-right'
      });
      zoombtn = 1
    }
      var marker = new atlas.HtmlMarker({
        color: 'Red',
        text: '',
        position: [xcoords,ycoords],
        popup: new atlas.Popup({
          content: '<div style="padding:10px">Hello World</div>',
          pixelOffset: [0, -30]
        })
      });
      map.markers.add(marker);
    });
}


$(function(){


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

$(function(){
  var pageURL = $(location).attr("href");
  var phno = pageURL.slice(-10);
  var arr = JSON.stringify({'phone_number':phno.toString()});

  $.ajax({
  url: '/api/ema_search_user_data',
  type: 'POST',
  data: JSON.stringify({'phone_number':phno.toString()}),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      $("#userDataList").append('<tr><th>Phone Number</th><td>'+msg[r+i]['phone_number']+'</td></tr><tr><th>Date Time Quarantined</th><td>'+msg[r+i]['date_time_quarantined']+'</td></tr><tr><th>First Name</th><td>'+msg[r+i]['first_name']+'</td></tr><tr><th>Last Name</th><td>'+msg[r+i]['last_name']+'</td></tr><tr><th>DOB</th><td>'+msg[r+i]['dob']+'</td></tr><tr><th>Currently Under Quarantine</th><td>'+msg[r+i]['currently_under_quarantine']+'</td></tr><tr><th>Email</th><td>'+msg[r+i]['email']+"</td></tr><tr><th>MO</th><td>"+msg[r+i]['mo_phone_number']+'</td></tr>');
          //$("#userDataList").append('<li>Phone Number: '+msg[r+i]['phone_number']+'</li><li>Date Time Quarantined:'+msg[r+i]['date_time_quarantined']+'</li><li>First Name: '+msg[r+i]['first_name']+'</li><li>Last Name: '+msg[r+i]['last_name']+'</li><li>DOB: '+msg[r+i]['dob']+'</li><li>Currenttly Under Quarantine'+msg[r+i]['currently_under_quarantine']+'</li><li>Email: '+msg[r+i]['email']+"</li><li>MO: "+msg[r+i]['mo_phone_number']+'</li>');
        }
        $("#userDataListHeader").html("User Data")
        GetMap();
    }
  });

  $.ajax({
  url: '/api/ema_search_user_base_data',
  type: 'POST',
  data: JSON.stringify({'phone_number':phno.toString()}),
  contentType: 'application/json; charset=utf-8',
  dataType: 'json',
  async: true,
  success: function(msg) {
    var count = msg['count']
    var r = "record"
    for (var i=0;i<count;i++){
      var hl = msg[r+i]['home-location'].split(',')
      xcoords = parseFloat(hl[1])
      ycoords = parseFloat(hl[0])
      $("#userBaseDataList").append('<tr><th>Phone Number</th><td>'+msg[r+i]['phone_number']+'</td></tr><tr><th>Home Location</th><td>'+msg[r+i]['home-location']+'</td></tr><tr><th>Face ID</th><td>'+msg[r+i]['face-id']+'</td></tr><tr><th>Date Time</th><td>'+msg[r+i]['date-time']+'</td></tr>');
          //$("#userDataList").append('<li>Phone Number: '+msg[r+i]['phone_number']+'</li><li>Date Time Quarantined:'+msg[r+i]['date_time_quarantined']+'</li><li>First Name: '+msg[r+i]['first_name']+'</li><li>Last Name: '+msg[r+i]['last_name']+'</li><li>DOB: '+msg[r+i]['dob']+'</li><li>Currenttly Under Quarantine'+msg[r+i]['currently_under_quarantine']+'</li><li>Email: '+msg[r+i]['email']+"</li><li>MO: "+msg[r+i]['mo_phone_number']+'</li>');
        }
        $("#userBaseDataListHeader").html("User Base Data")
        GetMap();
    }
  });

  $.ajax({
  url: '/api/ema_user_temp_data',
  type: 'POST',
  data: JSON.stringify({'phone_number':phno.toString()}),
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
    }
  });

  $.ajax({
  url: '/api/ema_user_cc_data',
  type: 'POST',
  data: JSON.stringify({'phone_number':phno.toString()}),
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
  }
  });

  $.ajax({
  url: '/api/ema_user_distress_data',
  type: 'POST',
  data: arr,
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
  }
  });

  $.ajax({
  url: '/api/ema_user_lstate_data',
  type: 'POST',
  data: arr,
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
  }
  });

  $.ajax({
  url: '/api/ema_user_state_data',
  type: 'POST',
  data: arr,
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
  }
  });

  $.ajax({
  url: '/api/ema_user_testing_data',
  type: 'POST',
  data: arr,
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
  }
  });

  $.ajax({
  url: '/api/ema_user_checklist_data',
  type: 'POST',
  data: arr,
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
  }
  });
});
});
//frontend oriented

$(document).ready(function () {
$('.table').css({
"scrollY": "50vh",
"scrollCollapse": true,
});
$('.dataTables_length').addClass('bs-select');
});
