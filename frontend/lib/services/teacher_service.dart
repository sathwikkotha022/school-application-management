import '../models/teacher_model.dart';
import '../models/teacher_subject_model.dart';
import '../models/teacher_class_model.dart';
import '../models/attendance_model.dart';
import '../models/mark_model.dart';
import '../models/teacher_attendance.dart';
import '../utils/mock_data.dart';

class TeacherService {
  // Get teacher profile
  static Future<Teacher> getTeacherProfile(int userId) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return MockData.getMockTeachers().firstWhere(
      (teacher) => teacher.userId == userId,
      orElse: () => MockData.getMockTeachers().first,
    );
  }

  // Get teacher's subjects
  static Future<List<TeacherSubject>> getTeacherSubjects(int teacherId) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return MockData.getMockTeacherSubjects()
        .where((ts) => ts.teacherId == teacherId)
        .toList();
  }

  // Get teacher's classes
  static Future<List<TeacherClass>> getTeacherClasses(int teacherId) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return MockData.getMockTeacherClasses()
        .where((tc) => tc.teacherId == teacherId)
        .toList();
  }

  // Mark student attendance
  static Future<StudentAttendance> markStudentAttendance(Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 500));

    // Create mock attendance record
    return StudentAttendance(
      id: DateTime.now().millisecondsSinceEpoch,
      studentId: data['student_id'],
      teacherId: data['teacher_id'],
      subjectId: data['subject_id'],
      classId: data['class_id'] ?? 1,
      sectionId: data['section_id'] ?? 1,
      date: data['date'],
      status: data['status'],
    );
  }

  // Update student attendance
  static Future<StudentAttendance> updateStudentAttendance(int attendanceId, Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 500));

    // Return updated mock attendance
    return StudentAttendance(
      id: attendanceId,
      studentId: data['student_id'] ?? 1,
      teacherId: data['teacher_id'] ?? 1,
      subjectId: data['subject_id'] ?? 1,
      classId: data['class_id'] ?? 1,
      sectionId: data['section_id'] ?? 1,
      date: data['date'] ?? DateTime.now().toIso8601String(),
      status: data['status'] ?? 'present',
    );
  }

  // Assign attendance to class
  static Future<List<StudentAttendance>> assignClassAttendance(Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 500));

    // Return mock attendance records for class
    return List.generate(30, (index) => StudentAttendance(
      id: DateTime.now().millisecondsSinceEpoch + index,
      studentId: index + 1,
      teacherId: data['teacher_id'],
      subjectId: data['subject_id'],
      classId: data['class_id'] ?? 1,
      sectionId: data['section_id'] ?? 1,
      date: data['date'],
      status: data['status'] ?? 'present',
    ));
  }

  // Teacher login
  static Future<TeacherAttendance> teacherLogin(int teacherId) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return TeacherAttendance(
      id: DateTime.now().millisecondsSinceEpoch,
      teacherId: teacherId,
      date: DateTime.now().toIso8601String(),
      status: 'present',
      loginTime: DateTime.now(),
      logoutTime: null,
    );
  }

  // Teacher logout
  static Future<TeacherAttendance> teacherLogout(int attendanceId) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return TeacherAttendance(
      id: attendanceId,
      teacherId: 1,
      date: DateTime.now().toIso8601String(),
      status: 'present',
      loginTime: DateTime.now().subtract(const Duration(hours: 8)),
      logoutTime: DateTime.now(),
    );
  }

  // Get teacher attendance
  static Future<List<TeacherAttendance>> getTeacherAttendance(int teacherId, {int skip = 0, int limit = 50}) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return MockData.getMockTeacherAttendances()
        .where((ta) => ta.teacherId == teacherId)
        .skip(skip)
        .take(limit)
        .toList();
  }

  // Create marks
  static Future<Mark> createMark(Map<String, dynamic> data) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return Mark(
      id: DateTime.now().millisecondsSinceEpoch,
      studentId: data['student_id'],
      subjectId: data['subject_id'],
      examId: data['exam_id'],
      marksObtained: data['marks_obtained'].toDouble(),
      totalMarks: data['total_marks'].toDouble(),
      student: MockData.getMockStudents().firstWhere((s) => s.id == data['student_id']),
      subject: MockData.getMockSubjects().firstWhere((s) => s.id == data['subject_id']),
      exam: MockData.getMockExams().firstWhere((e) => e.id == data['exam_id']),
    );
  }
}
