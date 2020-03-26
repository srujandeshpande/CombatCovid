import 'package:flutter/material.dart';
import 'package:covid_qma/qma/login.dart';
import 'package:covid_qma/qma/home.dart';
import 'package:covid_qma/qma/dashboard.dart';
import 'package:covid_qma/qma/face-login.dart';
import 'package:covid_qma/qma/temp-login.dart';
import 'package:covid_qma/qma/notifications.dart';
import 'package:covid_qma/qma/distress.dart';
import 'package:covid_qma/qma/contact-person.dart';
import 'package:shared_preferences/shared_preferences.dart';

Future<void> main() async{ 

  WidgetsFlutterBinding.ensureInitialized();

  SharedPreferences prefs = await SharedPreferences.getInstance();
  var pno = prefs.getInt('PhoneNumber');
  print(pno);
  runApp(
  MaterialApp(
    initialRoute: pno == null? '/' : '/home',
    routes : {
      '/': (context) => Login(),
      '/home': (context) => Home(),
      '/dashboard' : (context) => Dashboard(),
      '/face-login' : (context) => FaceLogin(),
      '/temp-login': (context) => TempLogin(),
      '/notifications' : (context) => Notifications(),
      '/distress' : (context) => Distress(),
      '/contact-person': (context) => ContactPerson(),
    }
  )
);
}
