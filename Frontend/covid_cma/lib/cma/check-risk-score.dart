
import 'package:flutter/material.dart';

class CheckRiskScore extends StatelessWidget{
  @override 
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
      backgroundColor: Colors.greenAccent,
        title: Text(
          'risk-score',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Column(children: <Widget>[
        Center(
          child:Container(
            padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child : Text(
              'Add your history details here below and we will generate a risk score based on that.',
               style: TextStyle(
                 color: Colors.grey[600],
                 letterSpacing: 1.5,
                 fontSize: 20,
               )
          ) 
          )
        ),
        Center(
          child:Container(
          color:Colors.grey[200],
          height:350,
          width:250,
          padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          ),
        ),
        SizedBox(height: 20,),
        RaisedButton(onPressed: (){},
          color: Colors.greenAccent,
          child: Text('SUBMIT',
          style: TextStyle(
            letterSpacing: 2.0,
          ))
        ),
        SizedBox(height: 50,),
        Text(
          '60%',
          style:TextStyle(
            fontSize: 60,
            color: Colors.purple,
          )
        ),
        SizedBox(height:15,),
        Text('YOUR RISK SCORE',
        style:TextStyle(
            fontSize: 15,
            letterSpacing: 2.0,
            color: Colors.grey,
          )
        )
      ],)
    );
  }
}

