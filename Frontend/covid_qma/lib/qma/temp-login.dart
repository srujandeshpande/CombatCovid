import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';

import 'package:shared_preferences/shared_preferences.dart';

class TempLogin extends StatefulWidget {
  //const Login({Key key}) : super(key: key);
  @override
  _TempLoginState createState() => _TempLoginState();
}

class _TempLoginState extends State<TempLogin> {

  String text = "NONE";
  var _text = "NONE";
  bool isLoading;
  final temp = TextEditingController();
  String url = "https://combat-covid.azurewebsites.net/api/add_new_temperature";
  Map<String,String> headers = {"Content-type" : "application/json"};
  DateTime date;
  String _temp;
  final tempController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.amber,
        title: Text(
          'temp-login',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Column(
        children: <Widget>[
        Center(
          child:Container(
            padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child : Text(
              'Please log your temperature every few hours so we know that you are safe!',
               style: TextStyle(
                 color: Colors.grey[600],
                 letterSpacing: 1.5,
                 fontSize: 20,
               )
          ) 
          )
        ),
        Padding(
        padding: EdgeInsets.fromLTRB(30, 40, 30, 30),
        child:TextFormField(
          controller: tempController,
          enabled:true,
          keyboardType: TextInputType.numberWithOptions(),
          decoration: InputDecoration(
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.amber),
              borderRadius: BorderRadius.all(Radius.circular(40)),
            ),
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.amber),
              borderRadius: BorderRadius.all(Radius.circular(40)),
            ),
            focusColor: Colors.amber,
            labelText: 'Temperature ',
            labelStyle: TextStyle(
              color: Colors.orange,
            )
          ),
        ),
        ),
        RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.amber)),
           color: Colors.amber,
          onPressed: (){
            setState(() {
              _temp = tempController.text;
            });
            logTemperature();
          },
          child : Text(
            'SUBMIT',
            style: TextStyle(
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        SizedBox(height: 40,),
        Text(
          text,
        )
        ],
      )
    );
  }
  logTemperature() async
  {
    try{
      DateTime now = DateTime.now();
      var n = now.toString();
      SharedPreferences prefs = await SharedPreferences.getInstance();
      String pno = prefs.getString('PhoneNumber');
      Map js = {"phone_number":pno,"temperature":_temp,"Date-time": n};
      var body = json.encode(js);
        var response = await http.post(url,headers:headers,body: body);
        int code = response.statusCode;
        print(code);
        print(response.body);
        if (code < 300)
        {
          prefs.setString("last-temp-log", DateTime.now().toString());
          _text = "SUCCESS, logged in";
          setState(() {
            isLoading = false;
          });
          sleep(Duration(seconds: 1));
        }
        else if(code <=499)
          _text = response.toString();
      }
      catch(Exception)
      {
          _text = Exception.toString();
      }
      setState(() 
      {
        isLoading = false;
        text = _text;
      });
  }
}