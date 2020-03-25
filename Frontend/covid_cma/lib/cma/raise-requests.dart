import 'package:flutter/material.dart';

class RaiseRequests extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.redAccent,
        title: Text(
          'Request',
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
              'You are going to raise a request to the authorities indicating that you have been i contact with public places, and is serious about your safety.',
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
              'Please Provide reliable info so that we know you are safe!',
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
                decoration:  InputDecoration(  
                  fillColor: Colors.redAccent,
                  icon:  Icon(Icons.person,color:Colors.redAccent), 
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.redAccent)
                  ), 
                  hintText: 'Enter person\'s name',  
                  labelText: 'Name', 
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.orange,
                  )

                ),  
              ),  
              TextFormField(  
                
                decoration:InputDecoration( 
                  focusColor: Colors.redAccent,
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.redAccent)
                  ),
                  icon: const Icon(Icons.phone,color:Colors.redAccent),  
                  hintText: 'Enter person\'s phone number',  
                  labelText: 'Phone',  
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.orange,
                  )
                ),  
              ),  
              TextFormField( 
                decoration: const InputDecoration(  
                icon: const Icon(Icons.calendar_today,color:Colors.redAccent),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.redAccent)
                  ),
                hintText: 'Enter person\'s date of birth',  
                labelText: 'Dob', 
                labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.orange,
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