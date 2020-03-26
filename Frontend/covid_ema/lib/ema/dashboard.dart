import 'package:flutter/material.dart';

class Dashboard extends StatelessWidget {
  //const Dashboard({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.lightBlue[900],
        title: Text(
          'Dashboard',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body:Padding(
        padding: EdgeInsets.fromLTRB(40, 40, 40, 40),
        child: Column(children: <Widget>[
          Center(
            child: CircleAvatar(
              backgroundImage: AssetImage('assets/profile-pic.jpg'),
              radius:60,
            )
            ),
          Divider(color: Colors.blueAccent,
            height: 90,
          ),
          Text(
            'NAME',
            style:TextStyle(
              color:Colors.grey,
              letterSpacing: 2.0,
            )
          ),
          SizedBox(height: 10,),
          Text(
            'JOHN',
            style:TextStyle(
              color:Colors.blueAccent,
              letterSpacing: 2.0,
              fontSize: 20,
            )
          ),

          Divider(color: Colors.grey,
            height: 90,
          ),
          Text(
            'PHC',
            style:TextStyle(
              color:Colors.grey,
              letterSpacing: 2.0,
            )
          ),
          SizedBox(height: 10,),
          Text(
            'BANGALORE-SOUTH',
            style:TextStyle(
              color:Colors.blueAccent,
              letterSpacing: 2.0,
              fontSize: 20,
            )
          ),
         Divider(color: Colors.blueAccent,
            height: 90,
          ),

        ],)
      )
    );
  }
}