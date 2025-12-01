import '../models/user_model.dart';

class AuthService {
  // Mock login - returns different users based on email
  static Future<Map<String, dynamic>> login(String email, String password) async {
    await Future.delayed(const Duration(milliseconds: 800)); // Simulate API delay

    // Mock authentication logic
    if (email.contains('admin')) {
      return {
        'success': true,
        'user': User(
          id: 1,
          username: email,
          email: email,
          role: 'admin',
          firstName: 'Admin',
          lastName: 'User',
        ).toJson(),
        'token': 'mock_admin_token_12345'
      };
    } else if (email.contains('teacher')) {
      return {
        'success': true,
        'user': User(
          id: 2,
          username: email,
          email: email,
          role: 'teacher',
          firstName: 'Teacher',
          lastName: 'User',
        ).toJson(),
        'token': 'mock_teacher_token_12345'
      };
    } else if (email.contains('student')) {
      return {
        'success': true,
        'user': User(
          id: 3,
          username: email,
          email: email,
          role: 'student',
          firstName: 'Student',
          lastName: 'User',
        ).toJson(),
        'token': 'mock_student_token_12345'
      };
    } else {
      return {
        'success': false,
        'message': 'Invalid credentials'
      };
    }
  }

  // Mock register student
  static Future<Map<String, dynamic>> registerStudent(Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 1000));

    return {
      'success': true,
      'message': 'Student registered successfully',
      'user_id': 100,
      'student_id': 200
    };
  }

  // Mock register teacher
  static Future<Map<String, dynamic>> registerTeacher(Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 1000));

    return {
      'success': true,
      'message': 'Teacher registered successfully',
      'user_id': 101,
      'teacher_id': 201
    };
  }

  // Mock register admin
  static Future<Map<String, dynamic>> registerAdmin(Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 1000));

    return {
      'success': true,
      'message': 'Admin registered successfully',
      'user_id': 102
    };
  }
}
