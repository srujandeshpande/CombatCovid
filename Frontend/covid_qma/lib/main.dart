import 'package:covid_qma/qma/loc-registration.dart';
import 'package:covid_qma/qma/location_services.dart';
import 'package:flutter/material.dart';
import 'package:covid_qma/qma/login.dart';
import 'package:covid_qma/qma/home.dart';
import 'package:covid_qma/qma/dashboard.dart';
import 'package:covid_qma/qma/face-login.dart';
import 'package:covid_qma/qma/temp-login.dart';
import 'package:covid_qma/qma/notifications.dart';
import 'package:covid_qma/qma/distress.dart';
import 'package:covid_qma/qma/registration.dart';
import 'package:covid_qma/qma/contact-person.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:covid_qma/qma/home_services.dart';

Future<void> main() async{ 

  WidgetsFlutterBinding.ensureInitialized();

  SharedPreferences prefs = await SharedPreferences.getInstance();
  var pno = prefs.getString('PhoneNumber');
  runApp(
  MaterialApp(
    //initialRoute: '/register-face',
    initialRoute: pno == null ? '/' : '/home',
    routes : {
      '/home-services': (context) => HomeLoading(),
      '/location':(context)=> LocationServices(),
      '/reg-location' : (context) => LocationReg(),
      '/': (context) => Login(),
      '/home': (context) => Home(),
      '/register-face':(context) => RegisterFace(),
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
