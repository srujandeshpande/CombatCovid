
import 'package:flutter/material.dart';
class HeatMap extends StatelessWidget{
  @override 
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
      backgroundColor: Colors.greenAccent,
        title: Text(
          'Updates',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child:Column(children: <Widget>[
        Center(
          child:Container(
            padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child : Text(
              'We want you to be aware of the condition of the COVID-19 so we can work together to slow its spread!.',
               style: TextStyle(
                 color: Colors.grey[600],
                 letterSpacing: 1.5,
                 fontSize: 20,
               )
          ) 
          )
        ),
        /*
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
        */
        SizedBox(height: 50,),
        
        Row(children: <Widget>[
        SizedBox(width: 60,),
        Column(children: <Widget>[
        Text(
          '562',
          style:TextStyle(
            fontSize: 60,
            color: Colors.orangeAccent,
          )
        ),

        SizedBox(height:15,),
        Text('POSITIVE CASES',
        style:TextStyle(
            fontSize: 15,
            letterSpacing: 2.0,
            color: Colors.grey,
          )
        ),
        ],
        ),
        SizedBox(width:45,),
        Column(children: <Widget>[
        Text(
          '9',
          style:TextStyle(
            fontSize: 60,
            color: Colors.red,
          )
        ),
        SizedBox(height:15,),
        Text('DEATHS',
        style:TextStyle(
            fontSize: 15,
            letterSpacing: 2.0,
            color: Colors.grey,
          )
        )
        ],
        )
         ],
      ),
      SizedBox(height:25,),
      Row(children: <Widget>[
        SizedBox(width: 60,),
        Column(children: <Widget>[
        Text(
          '9089',
          style:TextStyle(
            fontSize: 60,
            color: Colors.pinkAccent,
          )
        ),
        SizedBox(height:15,),
        Text('HIGH RISK CASES',
        style:TextStyle(
            fontSize: 15,
            letterSpacing: 2.0,
            color: Colors.grey,
          )
        ),
        ],
        ),
        SizedBox(width: 20,),

        Column(children: <Widget>[
          
        Text(
          '289',
          style:TextStyle(
            fontSize: 60,
            color: Colors.green,
          )
        ),
        SizedBox(height:15,),
        Text('CURED CASES',
        style:TextStyle(
            fontSize: 15,
            letterSpacing: 2.0,
            color: Colors.grey,
          )
        )
        ],
        )
         ],
      ),
      
      SizedBox(height:39,), 
      ],
      )
      )
    );
  }
}
