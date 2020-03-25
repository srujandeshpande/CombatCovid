import 'package:flutter/material.dart';

class ContactPerson extends StatelessWidget {  
  @override  
      Widget build(BuildContext context) {    
        return Scaffold(  
            appBar: AppBar(
                  backgroundColor: Colors.amber,
                  title: Text(
                  'cont',
                style:TextStyle(
                  fontSize:30,
                  letterSpacing: 2.0,
                ),
              ),
              centerTitle: true,
            ), 
            body: MyCustomForm(),  
        );  
      }  
    }  
    // Create a Form widget.  
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
              'Please Provide reliable info on the close contact person so that we know they are safe!',
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
                  fillColor: Colors.amber,
                  icon:  Icon(Icons.person,color:Colors.amber), 
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.amber)
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
                  focusColor: Colors.amber,
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.amber)
                  ),
                  icon: const Icon(Icons.phone,color:Colors.amber),  
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
                icon: const Icon(Icons.calendar_today,color:Colors.amber),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.amber)
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
              Container( 
                  child:RaisedButton(
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
        ), 
              ],
              )
              ) 
            ],  
          ),  
        );  
      }  
    }  