import 'package:flutter/material.dart';
import 'package:covid_qma/qma/login.dart';
import 'package:covid_qma/qma/home.dart';
import 'package:covid_qma/qma/dashboard.dart';
import 'package:covid_qma/qma/face-login.dart';
import 'package:covid_qma/qma/temp-login.dart';
import 'package:covid_qma/qma/notifications.dart';
import 'package:covid_qma/qma/distress.dart';
import 'package:covid_qma/qma/contact-person.dart';


void main() => runApp(
  MaterialApp(
    initialRoute: '/',
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

