import 'package:flutter/material.dart';
import 'dart:async';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:shared_preferences/shared_preferences.dart';

class MyWebView extends StatelessWidget {
  final String title;
  final String selectedUrl;

  final Completer<WebViewController> _controller =
      Completer<WebViewController>();
      
  MyWebView({
    @required this.title,
    @required this.selectedUrl,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(title),
        ),
        body:
         WebView(
          initialUrl: selectedUrl,
          javascriptMode: JavascriptMode.unrestricted,
          onWebViewCreated: (WebViewController webViewController) {
            _controller.complete(webViewController);
          },
        ));
  }
}

class Home extends StatelessWidget {
  //const Login({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      appBar:  AppBar(
      backgroundColor: Colors.greenAccent,
        title: Text(
          'HOME',
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
                color: Colors.greenAccent,
              ),
              child: Text(
                'Citizen management app',
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
                title:Text('Updates'),
                onTap: () {
                      Navigator.pushNamed(context, '/heat-map');
                },
            ),
             ListTile(leading: Icon(Icons.notifications),
                title:Text('Raise Requests'),
                onTap: () {
                      Navigator.pushNamed(context, '/raise-requests');
                },
            ),
             ListTile(leading: Icon(Icons.notifications),
                title:Text('Log out'),
                onTap: () async {
                      SharedPreferences prefs = await SharedPreferences.getInstance();
                      prefs.remove('PhoneNumber');
                      Navigator.pushNamedAndRemoveUntil(context, '/', (Route<dynamic> route)=> false);
                },
            ),
          ]
        ),
      ),
      body: Padding(
          padding: const EdgeInsets.fromLTRB(30, 40, 40, 40),
          child: Column(children: <Widget>[
            Text(
              'Hello fellow citizen, be safe, be aware, and take care.',
              style: TextStyle(
                color: Colors.grey,
                letterSpacing: 2.0,
              ),
            ),
            Divider(
              height: 86,
              color: Colors.grey,
            ),
            Text(
              'Check your risk score:',
              style: TextStyle(
                color: Colors.grey,
                letterSpacing: 2.0,
              ),
            ),
            SizedBox(height: 10),
            RaisedButton(onPressed: (){
              Navigator.pushNamed(context, '/risk-score');
            },
              color: Colors.greenAccent,
              child : Text(
                'Risk score'
              ),
            ), 

            Divider(
              height: 85,
              color: Colors.grey,
            ),

            Text(
              'Check the cases close to you through our Heat Map:',
              style: TextStyle(
                color: Colors.grey,
                letterSpacing: 2.0,
              ),
            ),
            SizedBox(height: 10),
            RaisedButton(onPressed: (){
             Navigator.of(context).push(MaterialPageRoute(
        builder: (BuildContext context) => MyWebView(
              title: "Heat Map",
              selectedUrl: "https://local-test-server.herokuapp.com/",
            )));
            },
              color: Colors.greenAccent,
              child : Text(
                'Heat map'
              ),
            ), 

            Divider(
              height: 85,
              color: Colors.grey,
            ),

            Text(
              'Report public contact',
              style: TextStyle(
                color: Colors.grey,
                letterSpacing: 2.0,
              ),
            ),
            SizedBox(height: 10),
            RaisedButton(onPressed: (){
              Navigator.pushNamed(context, '/report-public');
            },
              color: Colors.greenAccent,
              child : Text(
                'Report'
              ),
            ), 

            Divider(
              height: 90,
              color: Colors.grey,
            ),
          ],)  
      ),

     
    );
  }
}

 