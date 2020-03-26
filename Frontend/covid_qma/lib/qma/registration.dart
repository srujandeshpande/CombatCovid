import 'face_utilities.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:flutter/material.dart';

class RegisterFace extends StatefulWidget {
  @override
  _RegisterFaceState createState() => _RegisterFaceState();
}

class _RegisterFaceState extends State<RegisterFace> {
  
  File _image;
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
            await FaceUtility.saveImageToPreferences(FaceUtility.base64String(_image.readAsBytesSync()));
            Navigator.pushNamedAndRemoveUntil(context, '/home', (Route<dynamic> route)=> false);
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
        ],)
      
    );
  }
}