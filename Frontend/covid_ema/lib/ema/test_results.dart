import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import "package:http/http.dart" as http;
import "dart:convert";
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
      bool testresult; 
      final pnoController = TextEditingController();
      final detailController = TextEditingController();
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
                style :TextStyle(color:Colors.white),
                controller: pnoController,
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
                style :TextStyle(color:Colors.white),
                controller: detailController,
                decoration:InputDecoration( 
                  focusColor: Colors.blueAccent,
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blueAccent)
                  ),
                  icon: const Icon(Icons.phone,color:Colors.blueAccent),  
                  hintText: 'Enter other details about conducted test',  
                  labelText: 'Other Test Details',  
                  labelStyle: TextStyle(
                    letterSpacing: 2.0,
                    color:Colors.cyanAccent,
                  )
                ),  
              ),  
              SwitchListTile(
              title: const Text('Mark switch if tested positive',
              style: TextStyle(
                 color: Colors.white,
               )
              ),
              value: false,
              onChanged: (bool val) =>
                  setState(() => testresult = val)
                ),
               SizedBox(height: 40,),
             Container( 
                  child:RaisedButton(
                  shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
                  side:BorderSide(color:Colors.cyanAccent)),
                  color: Colors.indigo,
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
    String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber'); 
  String qcPno = pnoController.text;
  String qtestdetail = detailController.text;
  String now = DateTime.now().toString();
  bool testQC = testresult;
  String url = "https://combat-covid.azurewebsites.net/api/add_new_test";
  Map<String,String> headers = {"Content-type" : "application/json"};
  Map js = {"phone_number":qcPno,"date_time":now,"test_result":testQC,"other_data":qtestdetail,"mo_phone_number":pno}; //ADD OTHER INFO
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