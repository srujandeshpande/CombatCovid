import 'package:flutter/material.dart';
import 'package:covid_cma/cma/login.dart';
import 'package:covid_cma/cma/publicReport.dart';
import 'package:covid_cma/cma/home.dart';
import 'package:covid_cma/cma/dashboard.dart';
import 'package:covid_cma/cma/raise-requests.dart';
import 'package:covid_cma/cma/check-risk-score.dart';
import 'package:covid_cma/cma/notifications.dart';
import 'package:covid_cma/cma/heat-map.dart';
import 'package:covid_cma/cma/register.dart';
import 'package:shared_preferences/shared_preferences.dart';
Future<void> main() async{ 

  WidgetsFlutterBinding.ensureInitialized();

  SharedPreferences prefs = await SharedPreferences.getInstance();
  var pno = prefs.getString('PhoneNumber');
  print(pno);
  runApp(
  MaterialApp(
    initialRoute: pno == null ? '/' : '/home',
    routes: {
      '/': (context) => Login(),
      '/register':(context)=>Register(),
      '/home': (context) => Home(),
      '/dashboard' : (context) => Dashboard(),
      '/notifications' : (context) => Notifications(),
      '/risk-score' : (context) => CheckRiskScore(),
      '/heat-map': (context) => HeatMap(),
      '/report-public' : (context) => ReportContact(),
      '/raise-requests': (context) => RaiseRequests(),
    }
  )
);

}