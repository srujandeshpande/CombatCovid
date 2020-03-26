import 'package:flutter/material.dart';
import 'package:covid_ema/ema/login.dart';
import 'package:covid_ema/ema/quarantine_checklist.dart';
import 'package:covid_ema/ema/home.dart';
import 'package:covid_ema/ema/dashboard.dart';
import 'package:covid_ema/ema/test_results.dart';
import 'package:covid_ema/ema/create_qc.dart';
import 'package:covid_ema/ema/distress_calls.dart';
import 'package:covid_ema/ema/calender.dart';

void main() => runApp(
  MaterialApp(
    initialRoute: '/',
    routes : {
      '/': (context) => Login(),
      '/home': (context) => Home(),
      '/dashboard' : (context) => Dashboard(),
      '/distress_calls' : (context) => DistressCalls(),
      '/quarantine_checklist' : (context) => QuarantineChecklist(),
      '/calender': (context) => Calender(),
      '/create_qc' : (context) => QuarantineCitizen(),
      '/test_results': (context) => TestResults(),
    }
  )
);