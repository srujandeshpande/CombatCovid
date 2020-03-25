import 'package:flutter/material.dart';

class Notifications extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.greenAccent,
        title: Text(
          'notif',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Center(
          child : Text(
              'you are at notifications',
               style: TextStyle(
                 color: Colors.black,
               )
          ) 
        )
    );
  }
}