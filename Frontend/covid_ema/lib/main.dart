import 'package:flutter/material.dart';
import 'package:covid_ema/ema/login.dart';
import 'package:covid_ema/ema/quarantine_checklist.dart';
import 'package:covid_ema/ema/home.dart';
import 'package:covid_ema/ema/dashboard.dart';
import 'package:covid_ema/ema/test_results.dart';
import 'package:covid_ema/ema/create_qc.dart';
import 'package:covid_ema/ema/distress_calls.dart';
import 'package:covid_ema/ema/calender.dart';
import 'package:shared_preferences/shared_preferences.dart';
Future<void> main() async{ 

  WidgetsFlutterBinding.ensureInitialized();

  SharedPreferences prefs = await SharedPreferences.getInstance();
  var pno = prefs.getString('PhoneNumber');
  print(pno);
  runApp(
  MaterialApp(
    initialRoute: pno == null ? '/' : '/mohome',
    routes : {
      '/': (context) => Login(),
      '/mohome': (context) => MOHome(),
      '/dashboard' : (context) => Dashboard(),
      '/distress_calls' : (context) => DistressCalls(),
      '/quarantine_checklist' : (context) => QuarantineChecklist(),
      '/calender': (context) => Calender(),
      '/create_qc' : (context) => QuarantineCitizen(),
      '/test_results': (context) => TestResults(),
    }
  )
);
}