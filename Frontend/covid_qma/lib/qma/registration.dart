import 'face_utilities.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
class RegisterFace extends StatefulWidget {
  @override
  _RegisterFaceState createState() => _RegisterFaceState();
}

class _RegisterFaceState extends State<RegisterFace> {
  String output = "HI";
  File _image;
  String faceId= '';
  static const String IMG_KEY = 'USER_PIC';
  
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
              'Please log your face for later procedures. Make sure there\'s ample lighting',
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
            SharedPreferences prefs = await SharedPreferences.getInstance();
            final bytes = _image.readAsBytesSync();
            
             setState(() {
                output = "loading";
              });
              try{
                  var uri = Uri.parse("https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect");

                  var request = http.Request("POST",uri)
                                  ..headers["Content-type"] = "application/octet-stream"
                                  ..headers["Ocp-Apim-Subscription-Key"] = "4b823f3294a047fbac047b2dd7ed445e"
                                  ..bodyBytes = bytes;
                    setState(() {
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
                        var p = jsonDecode(s);
                        faceId = p["faceId"];
                        prefs.setString("reg-face-id", faceId);
                        setState(() {
                          faceId = faceId;
                        });
                      }
                    );
                    if ((code < 300))
                    {
                      output = "SUCCESS, picture logged";
                      SharedPreferences prefs = await SharedPreferences.getInstance();
                      var pno = prefs.getString('PhoneNumber');
                      await FaceUtility.saveImageToPreferences(FaceUtility.base64String(_image.readAsBytesSync()),"USER_PIC_$pno");
                    }
                    else if(code <=499)
                      output = 'Some request error';
                    else{
                      output = 'server down';
                    }
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
        Text('$output, $faceId'),
        ],),
      floatingActionButton:FloatingActionButton(
        onPressed: (){
          Navigator.pushNamed(context, '/reg-location');
          },
        child: Icon(Icons.done,color: Colors.white,),
        backgroundColor: Colors.redAccent,
      ),
    );
  }
}