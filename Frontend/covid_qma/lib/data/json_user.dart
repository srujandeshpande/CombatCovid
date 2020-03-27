class JsonUser {
  String email;

  JsonUser({
    this.email,
  });

  factory JsonUser.fromJson(Map<String, dynamic> parsedJson) {
    Map json = parsedJson['phone_number'];
    return JsonUser(
      email: json['password'],
    );
  }
}