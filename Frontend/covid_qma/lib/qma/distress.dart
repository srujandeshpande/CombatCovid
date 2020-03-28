import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

class Distress extends StatefulWidget {
  //const Login({Key key}) : super(key: key);
  

  @override
  _DistressState createState() => _DistressState();
}

class _DistressState extends State<Distress> {

  String output= "hi";
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.redAccent,
        title: Text(
          'distress',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Padding(
      padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
      child:Column(children: <Widget>[
      SizedBox(height:270),
      Center(
          child : Text(
              'You are going to alert your MO regarding your issues, expect response soon.',
               style: TextStyle(
                 color: Colors.white,
                 fontSize: 20,
                 letterSpacing: 2.0,
               )
          ) 
      ),

      SizedBox(height: 40,),
      
      RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.pinkAccent)),
           color: Colors.redAccent,
          onPressed: (){
            setState(() {
              output = "LOADING ...";
            });
            logDistress();
          },
          child : Text(
            'CONFIRM',
            style: TextStyle(
              fontSize: 18,
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        Text(output,style: TextStyle(color: Colors.red),),
        ],)
    )
    );
  }
  logDistress() async
  {
    
  String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber');
  String now = DateTime.now().toString();
  String url = "https://combat-covid-v1.herokuapp.com/api/add_new_distress_call";
  Map<String,String> headers = {"Content-type" : "application/json"};
  Map js = {"phone_number":pno, "Date-time":now}; //ADD OTHER INFO
  var body = json.encode(js);

  try{
        var response = await http.post(url,headers:headers,body: body);
        setState(() {
          output = "loaded";
        });
        int code = response.statusCode;
        print(code);
        print(response.body);
        if (code<300)
          setState(() {
            output = "SUCCESS";
          });
        else
          setState(() {
            output = "FAILED";
          });
  }
  catch(Exception){
      output  = "NO INTERNET";
  }
  }
}