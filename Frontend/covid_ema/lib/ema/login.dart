import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';
import 'package:shared_preferences/shared_preferences.dart';

class Login extends StatefulWidget {
  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login> {

  String phoneNumber = "";
  String password = "";
  String text = "Logged out";
  bool isLoading = false;
  final pnoController = TextEditingController();
  final passController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:  AppBar(
      backgroundColor: Colors.amber,
        title: Text(
          'EMA',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body:Padding(padding: EdgeInsets.all(40),
      
        child: Column(children: <Widget>[
        SizedBox(height:60),
        
        TextField(
          controller: pnoController,
          decoration: InputDecoration(
               border: InputBorder.none,
               hintText: 'Phone number',
          ),
        ),
        TextField(
          controller: passController,
          decoration: InputDecoration(
               border: InputBorder.none,
               hintText: 'Password',
          ),
        ),
       SizedBox(height:40),
        RaisedButton(onPressed:()
        {
            setState(() {
              isLoading = true;
            });
            phoneNumber = pnoController.text;
            password = passController.text;
            doLogin(phoneNumber,password);
        },
          color:Colors.amber,
          child:Text(
            'LOGIN',
            style: TextStyle(
              letterSpacing: 2.0,
              color: Colors.grey[800],
            ),
          )
        ),
        SizedBox(height:24),
        Container(
          child: isLoading == true ? Text('Loading..') : Text('Nope')
        ),
        SizedBox(height: 40,),
        Text(
          text,
          style:TextStyle(
            fontSize: 20,
          )
        )
      ],
      )
      )
    );
  }

  doLogin(String phoneNumber,String password) async
  {
      String _text = text;
      var pno = int.parse(phoneNumber);
      assert(pno is int);
      String url = "https://combat-covid.azurewebsites.net/api/ema_app_login";
      Map<String,String> headers = {"Content-type" : "application/json"};
      Map js = {"phone_number":phoneNumber,"password":password };
      var body = json.encode(js);
      try{
        var response = await http.post(url,headers:headers,body: body);
        int code = response.statusCode;
        print(code);
        print(response.body);
        if (code < 300)
        {
          _text = "SUCCESS, logged in";
          setState(() {
            isLoading = false;
          });
          SharedPreferences prefs = await SharedPreferences.getInstance();
          prefs.setString('PhoneNumber', phoneNumber);
          sleep(Duration(seconds: 1));
          Navigator.pushNamedAndRemoveUntil(context,'/mohome', (Route<dynamic> route)=> false);
        }
        else if(code <=499)
          _text = response.toString();
      }
      catch(Exception)
      {
          _text = Exception.toString();
      }
      setState(() {
        isLoading = false;
        text = _text;
      });
  }
}