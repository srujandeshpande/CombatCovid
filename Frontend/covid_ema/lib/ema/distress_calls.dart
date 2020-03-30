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

  Future<String> getData() async {
        String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber'); 
      String url = "https://combat-covid.azurewebsites.net/api/ema_mo_distress_data";
      Map<String,String> headers = {"Content-type" : "application/json"};
      Map js = {"mo_phone_number":pno, };
      body = json.encode(js);
        var response = await http.post(url,headers:headers,body: body);
        int code = response.statusCode;
        var body1=json.decode(response.body);
        print(code);
        print(response.body);
        return body1;
  }

  @override
  void initState(){
    this.getData();
    super.initState();
  }

  @override
  Widget build(BuildContext context){
    return new Scaffold(
      appBar: new AppBar(title: new Text("Distress Calls"), backgroundColor: Colors.blue),
      body: new ListView.builder(
        itemCount: body == null ? 0 : body.length-1,
        itemBuilder: (BuildContext context, int index){
          return new Card(
           child: new Text(body1["record"+(index+1).toString()]["phone_number"]),
          );

        },
      ),
    );
  }
}