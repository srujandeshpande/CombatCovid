import 'dart:convert';
import 'dart:io';
import 'location_services.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class HomeLoading extends StatefulWidget {
  @override
  _HomeLoadingState createState() => _HomeLoadingState();
}

class _HomeLoadingState extends State<HomeLoading> {
  
  String loading = "LOADING..";
  

  services() async{
    SharedPreferences prefs = await SharedPreferences.getInstance();
    sleep(Duration(seconds: 1));
    setState(() {
      loading = "getting essential details..";
    });

    String pno = prefs.getString('PhoneNumber');
    String faceid = prefs.getString("reg-face-id");
    String now = DateTime.now().toString();
    String lat = prefs.getString('home-lat');
    String long = prefs.getString('home-long');
    prefs.setString('lastFaceLog', null);
    prefs.setString('lastTempLog', null);
    String url = "https://combat-covid.azurewebsites.net/api/add_new_user_data_qma";
    Map<String,String> headers = {"Content-Type":"application/json"};
    Map js = {"phone_number":"$pno","home-location":"$lat,$long","face-id":"$faceid","date-time":"$now"};
    var body = json.encode(js);

    var response = await http.post(url,headers: headers,body:body);
    print(
     "${response.statusCode} hello"
    );
    setState(() {
      loading = "setting up a last few things..";
    });
    
    intialize();
    sleep(Duration(seconds: 1));
    start();

     setState(() {
      loading = "Everything completely setup! Take care, be safe.";
    });

    sleep(Duration(seconds: 2));
    
    Navigator.pushNamedAndRemoveUntil(context, '/home', (Route<dynamic> route)=> false);
  }
  @override
  void initState(){
    
    super.initState();
    services();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(
      backgroundColor: Colors.amber,
        title: Text(
          'home',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body:Center(
        child: Text(
          loading,
          style: TextStyle(
            color: Colors.grey,
            fontSize: 16,
            letterSpacing: 2.0,
          )
        ),
      )
    );
  }
}