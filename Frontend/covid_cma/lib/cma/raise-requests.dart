import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import "package:http/http.dart" as http;
import "dart:convert";

class RaiseRequests extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.redAccent,
        title: Text(
          'Raise Request',
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
              'You are going to raise a request to the government for a health checkup.  ',
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
    // Create a corresponding State class. This class holds data related to the form.  
    class MyCustomFormState extends State<MyCustomForm> {  
      // Create a global key that uniquely identifies the Form widget  
      // and allows validation of the form.  
      var _x1,_x2,_x3;
      final nameController = TextEditingController();
      final dobController = TextEditingController();
      String output ="Waiting for submission";
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
              'Ensure that you fill up the questionnaire sincerly!',
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
                controller: nameController,
                decoration:  InputDecoration(  
                  fillColor: Colors.pinkAccent,
                  icon:  Icon(Icons.person,color:Colors.redAccent), 
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.redAccent)
                  ), 
                  hintText: 'Enter name',  
                  labelText: 'Name', 
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.pinkAccent,
                  )

                ),  
              ),  
              TextFormField(
                 style :TextStyle(color:Colors.white),
                controller: dobController,
                decoration:  InputDecoration(  
                  fillColor: Colors.pinkAccent,
                  icon:  Icon(Icons.person,color:Colors.redAccent), 
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.redAccent)
                  ), 
                  hintText: 'Enter dob',  
                  labelText: 'DOB', 
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.pinkAccent,
                  )

                ),  
              ),  
              SwitchListTile(
              title: const Text('Have you experienced any flu symptoms recently?',
              style: TextStyle(
                 color: Colors.white,
               )
              ),
              value: false,
              onChanged: (bool val) =>
                  setState(() => _x1 = val)
                ),
               SwitchListTile(
              title: const Text('Have you travelled abroad recently?',
              style: TextStyle(
                 color: Colors.white,
               )
              ),
              value: false,
              onChanged: (bool val) =>
                  setState(() => _x2 = val)
                ),
                SwitchListTile(
              title: const Text('Have you come in contact with someone who has travelled?',
              style: TextStyle(
                 color: Colors.white,
               )),
              value: false,
              onChanged: (bool val) =>
                  setState(() => _x3 = val)
                ),
               SizedBox(height: 40,),
               Container( 
                  child:RaisedButton(
                  shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
                  side:BorderSide(color:Colors.pinkAccent)),
                  color: Colors.redAccent,
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
            ],  
          ),  
        );  
      
   }  
       logForm() async
  {
   String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber'); 
  String name = nameController.text;
   String dob = dobController.text;
  String now = DateTime.now().toString();
  bool check1 = _x1;
  bool check2 = _x2;
  bool  check3= _x3;
  String url = "https://combat-covid.azurewebsites.net/api/cma_new_request";
  Map<String,String> headers = {"Content-type" : "application/json"};
  Map js = {"phone_number":pno,"name":name,"date_time":now,"symptom":check1,"travel":check2,"contact":check3,"dob":dob}; //ADD OTHER INFO
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