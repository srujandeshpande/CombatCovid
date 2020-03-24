import 'package:flutter/material.dart';

class TempLogin extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
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
          onPressed: (){},
          child : Text(
            'SUBMIT',
            style: TextStyle(
              letterSpacing: 2.0,
            ) 
        
          ),
        )
        ],
      )
    );
  }
}