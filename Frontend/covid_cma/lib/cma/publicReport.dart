import 'package:flutter/material.dart';

class ReportContact extends StatelessWidget
{
  @override 
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
      backgroundColor: Colors.greenAccent,
        title: Text(
          'report',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body:Column(children: <Widget>[
      SizedBox(height: 40,),
      Padding(padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
        child: Text('Enter the public places you\'ve been to',
        style: TextStyle(
          letterSpacing: 2.0,
          fontSize: 20,
          color: Colors.grey[600],
        )),
      ),
      Padding(
        padding: EdgeInsets.fromLTRB(30, 40, 30, 30),
        child:TextFormField(
          
          enabled:true,
          keyboardType: TextInputType.numberWithOptions(),
          decoration: InputDecoration(
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.greenAccent),
              borderRadius: BorderRadius.all(Radius.circular(40)),
            ),
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(color: Colors.greenAccent),
              borderRadius: BorderRadius.all(Radius.circular(40)),
            ),
            focusColor: Colors.amber,
            labelText: 'Public contacts ',
            labelStyle: TextStyle(
              color: Colors.greenAccent,
            )
          ),
        ),
      ),
        RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.greenAccent)),
           color: Colors.greenAccent,
          onPressed: (){},
          child : Text(
            'SUBMIT',
            style: TextStyle(
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.redAccent)),
           color: Colors.redAccent,
          onPressed: (){

            Navigator.pushNamed(context, '/raise-requests');
          },
          child : Text(
            'RAISE A REQUEST',
            style: TextStyle(
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        ],
        )
    );
  }
}

