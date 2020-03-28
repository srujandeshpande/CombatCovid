import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:convert';
import 'dart:typed_data';

class FaceUtility {

static const String IMG_KEY = "USER_FACE";

static Future<bool> saveImageToPreferences(String value) async {
  final SharedPreferences preferences = await SharedPreferences.getInstance();
  return preferences.setString(IMG_KEY, value);
}

static String base64String(Uint8List data)
{
  return base64Encode(data);
}

static Image imageFromString(String base64String)
{
  return Image.memory(
    base64Decode(base64String),
    fit: BoxFit.fill,
  );
}
} 