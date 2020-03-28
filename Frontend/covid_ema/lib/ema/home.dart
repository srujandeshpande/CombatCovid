import 'package:covid_ema/ema/distress_calls.dart';
import 'package:covid_ema/ema/quarantine_checklist.dart';
import 'package:covid_ema/ema/calender.dart';
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      appBar:  AppBar(
      backgroundColor: Colors.lightBlue[900],
        title: Text(
          'Home',
           style:TextStyle(
             fontSize:30,
             letterSpacing: 2.0,
           ),
        ),
        centerTitle: true,
      ),
      drawer: Drawer(
        child:ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.lightBlue[900],
              ),
              child: Text(
                'Medical Officer EMA app',
                style:TextStyle(
                  color: Colors.white,
                  fontSize: 24,
                ),
              )
            ),
            ListTile(leading: Icon(Icons.account_circle),
                title:Text('Dashboard'),
                onTap: () {
                      Navigator.pushNamed(context, '/dashboard');
                },
            ),
            ListTile(leading: Icon(Icons.notifications),
                title:Text('Distress Calls'),
                onTap: () {
                      Navigator.push(context, new MaterialPageRoute(
                          builder: (context)=>
                          new DistressCalls())
                        );
                },
            ),
             ListTile(leading: Icon(Icons.calendar_today),
                title:Text('Calender'),
                onTap: () {
                      Navigator.push(context, new MaterialPageRoute(
                          builder: (context)=>
                          new Calender(title: 'Calender'))
                        );
                },
            ),
          ]
        ),
      ),
      body: Padding(
          padding: const EdgeInsets.fromLTRB(30, 40, 40, 40),
          child: SingleChildScrollView(
                    child:Column(children: <Widget>[
                      Text(
                        'Hello moderator,lets work towards a better and healtier India.',
                        style: TextStyle(
                          color: Colors.grey,
                          letterSpacing: 2.0,
                        ),
                      ),
                      Divider(
                        height: 80,
                        color: Colors.grey,
                      ),
                      Text(
                        'Add a Qurantined Citizen:',
                        style: TextStyle(
                          color: Colors.grey,
                          letterSpacing: 2.0,
                        ),
                      ),
                      SizedBox(height: 10),
                      RaisedButton(onPressed: (){
                        Navigator.pushNamed(context, '/create_qc');
                      },
                        color: Colors.lightBlue[900],
                        child : Text(
                          'New Entry',
                          style: TextStyle(
                          color: Colors.white,
                          letterSpacing: 2.0,
                        ),
                        ),
                      ), 

                      Divider(
                        height: 80,
                        color: Colors.grey,
                      ),

                      Text(
                        'Add test results of Quarantined Citizen',
                        style: TextStyle(
                          color: Colors.grey,
                          letterSpacing: 2.0,
                        ),
                      ),
                      SizedBox(height: 10),
                      RaisedButton(onPressed: (){
                        Navigator.pushNamed(context, '/test_results');
                      },
                        color: Colors.lightBlue[900],
                        child : Text(
                          'Test Results',
                          style: TextStyle(
                          color: Colors.white,
                          letterSpacing: 2.0,
                        ),
                        ),
                      ), 

                      Divider(
                        height: 80,
                        color: Colors.grey,
                      ),

                      Text(
                        'Fill the Quarantine checklist on visit',
                        style: TextStyle(
                          color: Colors.grey,
                          letterSpacing: 2.0,
                        ),
                      ),
                      SizedBox(height: 10),
                      RaisedButton(onPressed: (){
                        Navigator.push(context, new MaterialPageRoute(
                          builder: (context)=>
                          new QuarantineChecklist())
                        );
                      },
                        color: Colors.lightBlue[900],
                        child : Text(
                          'Checklist',
                          style: TextStyle(
                          color: Colors.white,
                          letterSpacing: 2.0,
                        ),
                        ),
                      ), 

                      Divider(
                        height: 80,
                        color: Colors.grey,
                      ),
                    ],) , 
      ),
    ),);
  }
}