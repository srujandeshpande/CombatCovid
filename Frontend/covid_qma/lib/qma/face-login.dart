import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class FaceLogin extends StatefulWidget {
  @override
  _FaceLoginState createState() => _FaceLoginState();
}

class _FaceLoginState extends State<FaceLogin> {
  String regFaceid='';
  String logFaceid='';
  File _image; 
  String output = "HI";
  bool isLoading = false;
  Future getImage(ImageSource src) async {
      var image = await ImagePicker.pickImage(source: src);

      setState(() {
        _image = image;
      });
  }

  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.amber,
        title: Text(
          'Face log',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      body: Column(
        children: <Widget>[
        Center(
          child:Container(
            padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child : Text(
              'Please log your face every few hours so we know that you are inside where you are supposed to be',
               style: TextStyle(
                 color: Colors.grey[600],
                 letterSpacing: 1.5,
                 fontSize: 20,
               )
          ) 
          )
        ),
       
        Center(
          child:Container(
          color:Colors.grey[200],
          height:350,
          width:250,
          padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child: _image == null 
                ?Center(child:Text('No image Selected'))
                : Image.file(
                  _image,
                  fit : BoxFit.fitWidth,
                ),
          ),
        ),
        Row(
        mainAxisAlignment : MainAxisAlignment.center,
        children: <Widget>[
        RaisedButton(onPressed: (){getImage(ImageSource.camera);},
          child: Icon(Icons.add_a_photo),
          color: Colors.orangeAccent,
          
        ),
        SizedBox(width: 20,),
        RaisedButton(onPressed: (){getImage(ImageSource.gallery);},
          child: Icon(Icons.photo_album),
          color: Colors.orangeAccent,
        )

         ],),
        
        Container(
          padding: EdgeInsets.fromLTRB(30, 30, 30, 30),
          child:RaisedButton(onPressed: () async{
              setState(() {
                output = "loading";
              });
              try{
                  final bytes = _image.readAsBytesSync();
                  SharedPreferences prefs = await SharedPreferences.getInstance();
                  DateTime now = DateTime.now();
                  var n = now.toString();
                  String pno = prefs.getString('PhoneNumber');
                  var uri = Uri.parse("https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect");
                  Map<String,String> headers = {"Content-type" : "application/octet-stream", "Ocp-Apim-Subscription-Key":"4b823f3294a047fbac047b2dd7ed445e"};
                  Map js = {"phone_number":pno,"Date-time": n};
                  var body = json.encode(js);
                  var request = http.Request("POST",uri)
                                  ..headers["Content-type"] = "application/octet-stream"
                                  ..headers["Ocp-Apim-Subscription-Key"] = "4b823f3294a047fbac047b2dd7ed445e"
                                  ..bodyBytes = bytes;
                    
                    
                    setState(() {

                      regFaceid = prefs.getString("reg-face-id");
                      output = "Loading";
                    });
                    var response = await request.send();
                    var code = response.statusCode;
                    print(request);
                    print(code);
                    response.stream.transform(utf8.decoder).listen(
                      (value){
                        String s = value.toString();
                        var x = s.substring(1).split(']');
                        s = x[0].toString();
                        var q = jsonDecode(s);
                        logFaceid = q["faceId"];
                        
                        setState(() {
                          logFaceid = logFaceid;
                          
                        });
                      }

                    );
                    if ((code < 300))
                    {
                      setState(() {
                        output = "obtained your cur face id..loading verification";
                      });
                      String url = "https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/verify";
                      Map<String,String> headers = {"Content-type" : "application/json", "Ocp-Apim-Subscription-Key":"4b823f3294a047fbac047b2dd7ed445e"};
                      Map js = {"faceId1":regFaceid,"FaceId2": logFaceid};
                      var body = json.encode(js);
                      
                      var response = await http.post(url,headers: headers,body: body);
                      code = response.statusCode;
                      print(code);
                      print(response.body.toString());
                      
                      if (code <300)
                      {
                        var j = json.decode(response.body.toString());
                        //var s = jsonDecode(response.body.toString());
                        if (j['isIdentical'] == true){
                            prefs.setString("last-face-log", DateTime.now().toString());
                            output = "Successfully logged!!";
                            String url = "https://combat-covid.azurewebsites.net/api/user_face";
                      Map<String,String> headers = {"Content-type" : "application/json", "Ocp-Apim-Subscription-Key":"4b823f3294a047fbac047b2dd7ed445e"};
                      Map js = {"phone_number":pno,"logged-in":true,"confidence-level":j['confidence'],"face-id":logFaceid};
                      var body = json.encode(js);
                       
                      var response = await http.post(url,headers: headers,body: body);
                      print(response.statusCode);
                            }

                        else
                            output= "didn't detect similar faces, try again";

                        setState(() {
                              _image = null;
                            });
                      }
                      else if(code <499)
                      {
                        output = "something happend ops";
                      }
                      else
                      {
                        output = "no internet";
                      }
                      
                    }
                    else if(code <=499)
                      output = 'Some request error';
                    else{
                      output = 'server down';
                    }
                    setState(() {
                          output =output;
                        });
                  }
                  catch(Exception)
                  {
                      output = 'No internet';
                  }
                  setState(() 
                  {
                    output = output;
                  });
            
          },
            shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(40),
            side:BorderSide(color:Colors.amber)),
            color: Colors.amber,
            child: Text(
              'UPLOAD',
              style:TextStyle(
                color: _image==null
                  ?Colors.grey
                  :Colors.black,
                letterSpacing: 2.0,
              )
            )
          )
        ),
        Text(output),
        ],)
    );
  }
}