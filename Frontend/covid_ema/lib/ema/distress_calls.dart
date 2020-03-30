import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
var body,body1;
class DistressCalls extends StatefulWidget {
  @override
  HomePageState createState() => new HomePageState();
}

class HomePageState extends State<DistressCalls> {

  List data;

  void getData() async {
        String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber'); 
      String url = "https://combat-covid.azurewebsites.net/api/ema_mo_distress_data";
      Map<String,String> headers = {"Content-type" : "application/json"};
      Map js = {"mo_phone_number":pno, };
      body = json.encode(js);
        var response = await http.post(url,headers:headers,body: body);
        int code = response.statusCode;
        body1=json.decode(response.body);
        print(code);
        print(response.body);
  
  }

  @override
  void initState(){
    this.getData();
    super.initState();
  }

  @override
  Widget build(BuildContext context){
    return new Scaffold(
      backgroundColor: Colors.black12,
      appBar: new AppBar(title: new Text("Distress Calls"), backgroundColor: Colors.lightBlue[900]),
      body: new ListView.builder(
        itemCount: body1== null ? 0 : (body1.length-1),
        itemBuilder: (BuildContext context, int index){
          return new Container(
            decoration: new BoxDecoration(
        color: Colors.black,
        borderRadius: BorderRadius.all(Radius.circular(10)),
        border: Border.all(color: Colors.lightBlue[50], width: 2.0)),
           child:Column(
              children: <Widget>[
                SizedBox(height:20),
                Text("Phone Number : "+body1["record"+(index).toString()]["phone_number"]
                , style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 20.0,
                        color:Colors.white,
                      ),),
                  Text("Datetime : "+ body1["record"+(index).toString()]["Date-time"],
                   style: TextStyle(
                     color:Colors.cyanAccent,
                        fontSize: 18.0,
                      ),
               ),
                SizedBox(height:20),
            ],
          ));
        },
      ),
    );
  }
}