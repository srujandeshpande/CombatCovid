import 'package:flutter/material.dart';


class Login extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.lightBlue[900],
        title: Text(
          'EMA',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Center(
        child: RaisedButton(
          onPressed: (){
            Navigator.pushNamed(context, '/home');
          },
          color: Colors.lightBlue[900],
          child : Text(
              'Login',
               style: TextStyle(
                 color: Colors.white,
               )
          ) 
        )
      )
    );
  }
}