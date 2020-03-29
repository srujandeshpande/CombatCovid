import 'package:flutter/material.dart';
import "package:http/http.dart" as http;
import "dart:convert";
class Register extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
      
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black12,
      appBar: AppBar(
        backgroundColor: Colors.greenAccent,
        title: Text(
          'NEW Citizen FORM',
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
              'You are going to register as a citizen into the database.This will help us help you in these difficult times',
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
      String output = "Waiting for submission";
      final _formKey = GlobalKey<FormState>(); 
      final pnoController = TextEditingController();
      final fnameController = TextEditingController();
      final lnameController = TextEditingController();
      final dobController = TextEditingController();
      final emailController = TextEditingController();
       final passwordController = TextEditingController();
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
              'Please recheck details before submitting form!',
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
                style :TextStyle(color:Colors.white),
                controller: fnameController,
                decoration:  InputDecoration(  
                  fillColor: Colors.greenAccent,
                  focusColor : Colors.white,
                  icon:  Icon(Icons.person,color:Colors.greenAccent), 
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.greenAccent)
                  ), 
                  hintText: 'Enter first name',  
                  labelText: 'First Name', 
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  )

                ),  
              ),  
              TextFormField(
                style :TextStyle(color:Colors.white),
                controller: lnameController,
                decoration:  InputDecoration(  
                  fillColor: Colors.greenAccent,
                  icon:  Icon(Icons.person,color:Colors.greenAccent), 
                  focusedBorder: UnderlineInputBorder(
                  borderSide: BorderSide(color: Colors.greenAccent),
                  
                  ), 
                  hintText: 'Enter last name',  
                  labelText: 'Last Name', 
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  )

                ),  
              ),  
              TextFormField(  
                style :TextStyle(color:Colors.white),
                controller: pnoController,
                decoration:InputDecoration( 
                  focusColor: Colors.greenAccent,
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.greenAccent)
                  ),
                  icon: const Icon(Icons.phone,color:Colors.greenAccent),  
                  hintText: 'Enter phone number',  
                  labelText: 'Phone',  
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  )
                ),  
              ),  
              TextFormField( 
                style :TextStyle(color:Colors.white),
                controller: dobController,
                decoration: const InputDecoration(  
                icon: const Icon(Icons.calendar_today,color:Colors.greenAccent),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.greenAccent)
                  ),
                hintText: 'Enter date of birth',  
                labelText: 'Dob', 
                labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  ) 
                ),  
               ),  
               TextFormField( 
                 style :TextStyle(color:Colors.white),
                 controller: emailController,
                decoration: const InputDecoration(  
                icon: const Icon(Icons.calendar_today,color:Colors.greenAccent),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.greenAccent)
                  ),
                hintText: 'Enter email address',  
                labelText: 'Email Address', 
                labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  ) 
                ),  
               ),  
               TextFormField( 
                 style :TextStyle(color:Colors.white),
                 controller: passwordController,
                decoration: const InputDecoration(  
                icon: const Icon(Icons.calendar_today,color:Colors.greenAccent),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.greenAccent)
                  ),
                hintText: 'Enter password',  
                labelText: 'Password', 
                labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  ) 
                ),  
               ),  
               SizedBox(height: 40,),
              Container( 
                  child:RaisedButton(
                  shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
                  side:BorderSide(color:Colors.cyanAccent)),
                  color: Colors.lightGreenAccent,
                  onPressed: (){

                      setState(() {
                        output = "Loading";
                      });
                      logForm();
                  },
                  child : Text(
                    'SUBMIT',
                    style: TextStyle(
                      color: Colors.white,
                      letterSpacing: 2.0,
                    ) 
                
                  ),
                ),
                
        ), 
            Text(
                  output,
                  style:TextStyle(color:Colors.white,)
                ),
              ],
              )
              ) 
             ], ));  
      
      }  
       logForm() async
  {
  String qcPno = pnoController.text;
  String qcfname = fnameController.text;
  String qclname = lnameController.text;
  String qcDOB = dobController.text;
   String qcemail = emailController.text;
   String password= passwordController.text;
  String now = DateTime.now().toString();
  String url = "https://combat-covid.azurewebsites.net/api/cma_add_new_user";
  Map<String,String> headers = {"Content-type" : "application/json"};
  Map js = {"phone_number":qcPno,"date_time_created":now,"first_name":qcfname,"last_name":qclname,"dob":qcDOB,"email":qcemail,"password":password,}; //ADD OTHER INFO
  var body = json.encode(js);

  try{
        var response = await http.post(url,headers:headers,body: body);
        setState(() {
          output = "loaded";
        });
        int code = response.statusCode;
        print(code);
        print(response.body);
        if (code<300)
          setState(() {
            output = "SUCCESS";
          });
        else
          setState(() {
            output = "FAILED";
          });
  }
  catch(Exception){
      output  = "NO INTERNET";
  }
  }
}