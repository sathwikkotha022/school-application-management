import '../models/student_model.dart';
import '../models/mark_model.dart';
import '../models/attendance_model.dart';
import '../utils/mock_data.dart';

class StudentService {
  // Get student profile
  static Future<Student> getStudentProfile(int userId) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return MockData.getMockStudents().firstWhere(
      (student) => student.userId == userId,
      orElse: () => MockData.getMockStudents().first,
    );
  }

  // Get student attendance
  static Future<List<StudentAttendance>> getStudentAttendance(int studentId, {int skip = 0, int limit = 200}) async {
    await Future.delayed(const Duration(milliseconds: 500));

    return MockData.getMockStudentAttendances()
        .where((attendance) => attendance.studentId == studentId)
        .skip(skip)
        .take(limit)
        .toList();
  }

  // Get student marks
  static Future<List<Mark>> getStudentMarks(int studentId, {int? examId}) async {
    await Future.delayed(const Duration(milliseconds: 500));

    var marks = MockData.getMockMarks()
        .where((mark) => mark.studentId == studentId);

    if (examId != null) {
      marks = marks.where((mark) => mark.examId == examId);
    }

    return marks.toList();
  }
}
