class TeacherAttendance {
  final int id;
  final int teacherId;
  final String date;
  final String status;
  final DateTime? loginTime;
  final DateTime? logoutTime;

  TeacherAttendance({
    required this.id,
    required this.teacherId,
    required this.date,
    required this.status,
    this.loginTime,
    this.logoutTime,
  });

  factory TeacherAttendance.fromJson(Map<String, dynamic> json) {
    return TeacherAttendance(
      id: json['id'],
      teacherId: json['teacher_id'],
      date: json['date'],
      status: json['status'],
      loginTime: json['login_time'] != null ? DateTime.parse(json['login_time']) : null,
      logoutTime: json['logout_time'] != null ? DateTime.parse(json['logout_time']) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'teacher_id': teacherId,
      'date': date,
      'status': status,
      'login_time': loginTime?.toIso8601String(),
      'logout_time': logoutTime?.toIso8601String(),
    };
  }

  // Mock data
  static List<TeacherAttendance> getMockTeacherAttendance() {
    return [
      TeacherAttendance(
        id: 1,
        teacherId: 1,
        date: '2024-01-15',
        status: 'present',
        loginTime: DateTime.parse('2024-01-15T09:00:00Z'),
        logoutTime: DateTime.parse('2024-01-15T17:00:00Z'),
      ),
      TeacherAttendance(
        id: 2,
        teacherId: 1,
        date: '2024-01-16',
        status: 'present',
        loginTime: DateTime.parse('2024-01-16T08:45:00Z'),
        logoutTime: DateTime.parse('2024-01-16T16:30:00Z'),
      ),
    ];
  }
}
