import 'user_model.dart';

class Teacher {
  final int id;
  final int userId;
  final String? employeeId;
  final String? qualification;
  final String? phone;
  final User? user;

  Teacher({
    required this.id,
    required this.userId,
    this.employeeId,
    this.qualification,
    this.phone,
    this.user,
  });

  factory Teacher.fromJson(Map<String, dynamic> json) {
    return Teacher(
      id: json['id'],
      userId: json['user_id'],
      employeeId: json['employee_id'],
      qualification: json['qualification'],
      phone: json['phone'],
      user: json['user'] != null ? User.fromJson(json['user']) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'user_id': userId,
      'employee_id': employeeId,
      'qualification': qualification,
      'phone': phone,
      'user': user?.toJson(),
    };
  }
}
