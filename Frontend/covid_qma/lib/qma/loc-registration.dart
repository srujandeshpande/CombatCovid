import 'dart:io';

import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:shared_preferences/shared_preferences.dart';


class LocationReg extends StatefulWidget {
  @override
  _LocationRegState createState() => _LocationRegState();
}

class _LocationRegState extends State<LocationReg>{
  String output ='';
  Geolocator geo = new Geolocator()..forceAndroidLocationManager=true;
  String lat='x',long='x';
  setCoordinates() async
  {
    Position position = await geo.getCurrentPosition(desiredAccuracy : LocationAccuracy.high);
    lat = position.latitude.toString();
    long = position.longitude.toString();
    setState(() {
      lat = lat;
      long = long;
    });
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:  AppBar(
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
      body:Padding(
        padding:EdgeInsets.all(40),
        child:Column(children: <Widget>[
          Text('Now is the time to add your home location, make sure you mark your coordinates correctly, these will be used by the Medical officers and everyone to track you down.Be safe.'),
          SizedBox(height: 60,),
          Text(
            'Coordinates: $lat , $long. $output',
            style: TextStyle(
              color: Colors.grey,
              letterSpacing: 2.0,
            ),
          ),
          SizedBox(height: 30,),
          RaisedButton(onPressed: (){
            setCoordinates();
          },
            color: Colors.orange,
            child: Text(
              'GET COORDINATES'
            ),
            
          ),
          SizedBox(height: 90,),
            RaisedButton(onPressed: () async{
                SharedPreferences prefs = await SharedPreferences.getInstance();
                prefs.setString('home-lat',lat);
                prefs.setString('home-long',long);
                setState(() {
                  output = "Location updated!";
                });
            },
            color: Colors.amber,
            child: Text(
              'CONFIRM',
            ),
          ),
          FloatingActionButton(onPressed: (){
            Navigator.pushNamed(context, '/home-services');
          },
            child: Icon(Icons.done,color: Colors.white,),
            backgroundColor: Colors.redAccent,
          )
        ]
        ,)
      )
    );
  }
}