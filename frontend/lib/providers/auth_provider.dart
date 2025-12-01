import 'package:flutter/material.dart';
import '../models/user_model.dart';

class AuthProvider with ChangeNotifier {
  User? _user;
  bool _isAuthenticated = false;

  User? get user => _user;
  bool get isAuthenticated => _isAuthenticated;
  String? get userRole => _user?.role;

  void login(String email, String role) {
    _user = User(
      id: 1, // Mock ID
      username: email, // Use email as username for mock
      email: email,
      role: role,
    );
    _isAuthenticated = true;
    notifyListeners();
  }

  void logout() {
    _user = null;
    _isAuthenticated = false;
    notifyListeners();
  }
}
