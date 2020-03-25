import 'package:flutter/material.dart';

class Distress extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
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
          onPressed: (){},
          child : Text(
            'CONFIRM',
            style: TextStyle(
              fontSize: 18,
              letterSpacing: 2.0,
            ) 
        
          ),
        )
        ],)
    ));
  }
}