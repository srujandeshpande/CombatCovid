import 'package:flutter/material.dart';
import "package:http/http.dart" as http;
import "dart:convert";
import 'package:shared_preferences/shared_preferences.dart';
import 'package:geolocator/geolocator.dart';
 
class ReportContact extends StatefulWidget {
  @override
  _ReportContactState createState() => _ReportContactState();
}
  String output="Waiting for response";
class _ReportContactState extends State<ReportContact> {
  
  @override 
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
      backgroundColor: Colors.greenAccent,
        title: Text(
          'REPORT',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body:Column(children: <Widget>[
      SizedBox(height: 40,),
      Padding(padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
        child: Text('If you are in a crowded public area ,please share your loaction with us!You can even go ahead and raise a request to be on the safer side!',
        style: TextStyle(
          letterSpacing: 2.0,
          fontSize: 20,
          color: Colors.grey[600],
        )),
      ),
        RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.greenAccent)),
           color: Colors.greenAccent,
           onPressed: (){
   
                      setState(() {
                        output = "Loading";
                      });
                      logForm();
                  },
          child : Text(
            'Share Location',
            style: TextStyle(
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        Text(
          output,
          style:TextStyle(color:Colors.black),
        ),
        RaisedButton(
           shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
           side:BorderSide(color:Colors.redAccent)),
           color: Colors.redAccent,
          onPressed: (){

            Navigator.pushNamed(context, '/raise-requests');
          },
          child : Text(
            'RAISE A REQUEST',
            style: TextStyle(
              letterSpacing: 2.0,
            ) 
        
          ),
        ),
        ],
        )
    );
  }
  logForm() async
  {
    Position position = await Geolocator().getCurrentPosition(desiredAccuracy: LocationAccuracy.high);
  String pno = (await SharedPreferences.getInstance()).getString('PhoneNumber'); 
  String now = DateTime.now().toString();
  String lat = position.latitude.toString();
  String long = position.longitude.toString();
  String url = "https://combat-covid.azurewebsites.net/api/cma_add_location";
  Map<String,String> headers = {"Content-type" : "application/json"};
  Map js = {"phone_number":pno,"date_time":now,"latitude":lat,"longitude":long,}; //ADD OTHER INFO
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