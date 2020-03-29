import 'dart:async';
import 'dart:io';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:workmanager/workmanager.dart';

String lat = 'x';
String long = 'x';
const simplePeriodicTask = "simplePeriodicTask";

calcDistance(double lat,double long) async{
  SharedPreferences prefs = await SharedPreferences.getInstance();
  double hlat = double.parse(prefs.getString('home-lat'));
  double hlong = double.parse(prefs.getString('home-long'));
  double distance = await Geolocator().distanceBetween(hlat, hlong, lat, long);
  return distance;
}
void callbackDispatcher() {
  Workmanager.executeTask((task, inputData) async {
        SharedPreferences prefs = await SharedPreferences.getInstance();
        DateTime temptime = DateTime.parse(prefs.getString("last-temp-log")!=null?prefs.getString("last-temp-log"):DateTime.now().toString());
        DateTime facetime = DateTime.parse(prefs.getString("last-face-log")!=null?prefs.getString("last-face-log"):DateTime.now().toString());
        print("$simplePeriodicTask was executed");
        bool isface=false,istemp = false;

        String url = "https://combat-covid.azurewebsites.net/api/user_state_qma";
       
        Geolocator geo =  Geolocator()..forceAndroidLocationManager = true;
        bool proximity = true;
        var dis;
        bool st = false;
         GeolocationStatus status = await geo.checkGeolocationPermissionStatus();
        if (status.value ==2){
          print("here lol");
        st = true;
        Position position = await geo.getCurrentPosition(desiredAccuracy: LocationAccuracy.best);
        lat =  position.latitude.toString();
        long = position.longitude.toString();
        dis = await calcDistance(double.parse(lat), double.parse(long));
        
        if (dis > 100)
            proximity = false;}
        DateTime now = DateTime.now();

        if (temptime!=null){
        if (temptime.difference(now).inHours < 4)
        { 
            istemp = true;
        }}

        if (facetime!=null){
        if (facetime.difference(now).inHours < 4)
        { 
            isface = true;
        }}
        if (facetime == null) 
          isface = true;
        if (temptime == null)
          istemp = true;
        prefs.setBool('FTIME', isface);
        prefs.setBool('TTIME', istemp);
        print("lat and long got:$lat and $long");
        String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber');
         Map<String,String> headers = {"Content-type" : "application/json"};
         Map js = {"phone-number":pno,"lat":lat,"long":long,"date-time":(now.toString()),"distance-from-home":(dis.toString()),'proximity-to-home':proximity,"location_enabled":(st.toString()),"Last-face-log":(facetime.toString()),"Last-temp-log":(temptime.toString()),"face_exceeded":(isface.toString()),"temp_exceeded":(istemp.toString())};
         var body = json.encode(js);
         var response = await http.post(url,headers:headers,body: body);
         print(body);
         print(response.statusCode);
    return Future.value(true);
  });
}

class LocationServices extends StatefulWidget {
  @override
  _LocationServicesState createState() => _LocationServicesState();
}

enum _Platform { android, ios }

class PlatformEnabledButton extends RaisedButton {
  final _Platform platform;

  PlatformEnabledButton({
    this.platform,
    @required Widget child,
    @required VoidCallback onPressed,
  })  : assert(child != null, onPressed != null),
        super(
            child: child,
            onPressed: (Platform.isAndroid && platform == _Platform.android ||
                    Platform.isIOS && platform == _Platform.ios)
                ? onPressed
                : null);
}
intialize()
  {
          Workmanager.initialize(
                callbackDispatcher,
                isInDebugMode: true,
          );
          print("initalized");
  }

  start()async
  {
     Workmanager.registerPeriodicTask(
          "3",
          simplePeriodicTask,
          frequency: Duration(minutes: 10),
     );
    print("started");
  }

class _LocationServicesState extends State<LocationServices> {

  
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Flutter WorkManager Example"),
        ),
        body: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Text("Plugin initialization",
                  style: Theme.of(context).textTheme.headline),
              RaisedButton(
                  child: Text("Start the Flutter background service"),
                  onPressed: intialize ),
              SizedBox(height: 16),
              //This task runs once.
              //Most likely this will trigger immediately
             
              //This task runs once
              //This wait at least 10 seconds before running
              SizedBox(height: 8),
              Text("Periodic Tasks (Android only)",
                  style: Theme.of(context).textTheme.headline),
              //This task runs periodically
              //It will wait at least 10 seconds before its first launch
              //Since we have not provided a frequency it will be the default 15 minutes
              PlatformEnabledButton(
                  platform: _Platform.android,
                  child: Text("Register Periodic Task"),
                  onPressed: start),
              //This task runs periodically
              //It will run about every hour
              PlatformEnabledButton(
                platform: _Platform.android,
                child: Text("Cancel All"),
                onPressed: () async {
                  await Workmanager.cancelAll();
                  print('Cancel all tasks completed');
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}