import 'package:flutter/material.dart';

class DistressCalls extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.lightBlue[900],
        title: Text(
          'Distress calls',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Center(
          child : Text(
              'distress calls to be alerted here',
               style: TextStyle(
                 color: Colors.black,
               )
          ) 
        )
    );
  }
}