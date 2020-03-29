import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import "package:http/http.dart" as http;
import "dart:convert";

class ContactPerson extends StatefulWidget {  
  @override
  _ContactPersonState createState() => _ContactPersonState();
}

class _ContactPersonState extends State<ContactPerson> {
  
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
      String output = "hi";
      
      final pnoController = TextEditingController();
      final nameController = TextEditingController();
      final dobController = TextEditingController();
  
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
                controller: nameController,
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
                controller: pnoController,
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
                controller: dobController,
                decoration: const InputDecoration(  
                icon: const Icon(Icons.calendar_today,color:Colors.amber),  
                focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.amber)
                  ),
                hintText: 'Enter person\'s address',  
                labelText: 'Address', 
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
                  onPressed: (){

                      setState(() {
                        output = "Loading";
                      });
                      logForm();
                  },
                  child : Text(
                    'SUBMIT',
                    style: TextStyle(
                      letterSpacing: 2.0,
                    ) 
                
                  ),
                ),
                
        ), 
            Text(
                  output
                ),
              ],
              )
              ) 
            ],  
          ),  
        );  
      }  
      logForm() async
  {
    
  String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber');
  String contactPno = pnoController.text;
  String name = nameController.text;
  String address = dobController.text;
  String now = DateTime.now().toString();
  String url = "https://combat-covid-v1.herokuapp.com/api/add_close_contact";
  Map<String,String> headers = {"Content-type" : "application/json"};
  Map js = {"phone_number":pno,"Date-time":now, "contact-pno":contactPno,"contact-name":name,"contact-address":address}; //ADD OTHER INFO
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