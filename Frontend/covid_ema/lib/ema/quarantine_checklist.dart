import 'package:flutter/material.dart';

class QuarantineChecklist extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        title: Text(
          'QC CHECKLIST FORM',
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
              'You are going to fill up the checklist after examining quarantined citizen\'s condition ',
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
    // Create a corresponding State class. This class holds data related to the form.  
    class MyCustomFormState extends State<MyCustomForm> {  
      // Create a global key that uniquely identifies the Form widget  
      // and allows validation of the form.  
      var _x1,_x2,_x3;
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
              'Please conduct survey properly to ensure safety!',
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
                  fillColor: Colors.blueAccent,
                  icon:  Icon(Icons.person,color:Colors.blueAccent), 
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blueAccent)
                  ), 
                  hintText: 'Enter citizen\'s phone number',  
                  labelText: 'Phone Number', 
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  )

                ),  
              ),  
              SwitchListTile(
              title: const Text('Hygienic Living Space',
              style: TextStyle(
                 color: Colors.white,
               )
              ),
              value: false,
              onChanged: (bool val) =>
                  setState(() => _x1 = val)
                ),
               SwitchListTile(
              title: const Text('Controlled Symptoms',
              style: TextStyle(
                 color: Colors.white,
               )
              ),
              value: false,
              onChanged: (bool val) =>
                  setState(() => _x2 = val)
                ),
                SwitchListTile(
              title: const Text('Stamp Re-applied',
              style: TextStyle(
                 color: Colors.white,
               )),
              value: false,
              onChanged: (bool val) =>
                  setState(() => _x3 = val)
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