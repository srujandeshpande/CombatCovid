import 'package:flutter/material.dart';

class TestResults extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        title: Text(
          'TEST RESULT FORM',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body:SingleChildScrollView( 
      child:Padding(
      padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
      child:Column(children: <Widget>[
      SizedBox(height:20),
      Center(
        
          child : Text(
              'You are going to add a test results for quarantined citizen to the database.Ensure that you conduct a checkup before doing the same.',
               style: TextStyle(
                 color: Colors.white,
                 fontSize: 20,
                 letterSpacing: 2.0,
               )
          ) 
      ),
      SizedBox(height: 20,),
      MyCustomForm(),
      SizedBox(height: 40,),
      RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.indigoAccent)),
           color: Colors.indigo,
          onPressed: (){},
          child : Text(
            'CONFIRM',
            style: TextStyle(
              fontSize: 18,
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        SizedBox(height: 200,),
        ],)
      ),
        )
    );
  }
}

class MyCustomForm extends StatefulWidget {  
      @override  
      MyCustomFormState createState() {  
        return MyCustomFormState();  
      }  
    }  
    // Create a corresponding State class. This class holds data related to the form.  
    class MyCustomFormState extends State<MyCustomForm> {  
      // Create a global key that uniquely identifies the Form widget  
      // and allows validation of the form.  
      final _formKey = GlobalKey<FormState>();  
      @override  
      Widget build(BuildContext context) {  
        // Build a Form widget using the _formKey created above.  
        return Form(  
          key: _formKey,  
          child: Column(    
            children: <Widget>[
              Center(
          child:Container(
            padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child : Text(
              'Ensure to reconfirm results before submitting!',
               style: TextStyle(
                 color: Colors.grey[600],
                 letterSpacing: 1.5,
                 fontSize: 20,
               )
          ) 
          )
        ),
              Container(
              padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
              child:Column( 
              children: <Widget>[
              TextFormField(   
                decoration:InputDecoration( 
                  focusColor: Colors.blueAccent,
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blueAccent)
                  ),
                  icon: const Icon(Icons.phone,color:Colors.blueAccent),  
                  hintText: 'Enter citizen\'s phone number',  
                  labelText: 'Phone',  
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  )
                ),  
              ),  
              TextFormField( 
                decoration: const InputDecoration(  
                icon: const Icon(Icons.calendar_today,color:Colors.blueAccent),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blueAccent)
                  ),
                hintText: 'Enter citizens\'s test result as POSITIVE or NEGATIVE',  
                labelText: 'Test Result', 
                labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  ) 
                ),  
               ),  
               SizedBox(height: 40,),
              
              ],
              )
              ) 
            ],  
          ),  
        );  
      
      }  
    }  