import '../models/section_model.dart';
import '../models/subject_model.dart';
import '../models/exam_model.dart';
import '../models/student_model.dart';
import '../models/teacher_model.dart';
import '../models/attendance_model.dart';
import '../models/mark_model.dart';
import '../models/teacher_subject_model.dart';
import '../models/teacher_class_model.dart';
import '../models/user_model.dart';
import '../models/class_model.dart';
import '../models/teacher_attendance.dart';

class MockData {
  // Singleton pattern
  static final MockData _instance = MockData._internal();

  factory MockData() {
    return _instance;
  }

  MockData._internal();

  // Mock data lists
  static List<User> getMockUsers() {
    return [
      User(
        id: 1,
        username: 'admin',
        email: 'admin@school.com',
        firstName: 'Admin',
        lastName: 'User',
        role: 'admin',
      ),
      User(
        id: 2,
        username: 'teacher1',
        email: 'teacher1@school.com',
        firstName: 'John',
        lastName: 'Doe',
        role: 'teacher',
      ),
      User(
        id: 3,
        username: 'student1',
        email: 'student1@school.com',
        firstName: 'Jane',
        lastName: 'Smith',
        role: 'student',
      ),
    ];
  }

  static List<Student> getMockStudents() {
    return [
      Student(
        id: 1,
        userId: 3,
        rollNumber: '001',
        classId: 1,
        sectionId: 1,
      ),
    ];
  }

  static List<Teacher> getMockTeachers() {
    return [
      Teacher(
        id: 1,
        userId: 2,
        employeeId: 'T001',
      ),
    ];
  }

  static List<Subject> getMockSubjects() {
    return [
      Subject(
        id: 1,
        name: 'Mathematics',
        code: 'MATH101',
      ),
    ];
  }

  static List<SchoolClass> getMockClasses() {
    return [
      SchoolClass(
        id: 1,
        name: 'Class 10',
      ),
    ];
  }

  static List<Section> getMockSections() {
    return [
      Section(
        id: 1,
        name: 'A',
        classId: 1,
      ),
    ];
  }

  static List<Exam> getMockExams() {
    return [
      Exam(
        id: 1,
        name: 'Mid Term Exam',
        date: '2024-01-15',
      ),
    ];
  }

  static List<StudentAttendance> getMockStudentAttendances() {
    return [
      StudentAttendance(
        id: 1,
        studentId: 1,
        teacherId: 1,
        subjectId: 1,
        classId: 1,
        sectionId: 1,
        date: '2024-01-15',
        status: 'present',
      ),
    ];
  }

  static List<TeacherAttendance> getMockTeacherAttendances() {
    return [
      TeacherAttendance(
        id: 1,
        teacherId: 1,
        date: '2024-01-15',
        status: 'present',
      ),
    ];
  }

  static List<Mark> getMockMarks() {
    return [
      Mark(
        id: 1,
        studentId: 1,
        subjectId: 1,
        examId: 1,
        marksObtained: 85,
        totalMarks: 100,
      ),
    ];
  }

  static List<TeacherSubject> getMockTeacherSubjects() {
    return [
      TeacherSubject(
        id: 1,
        teacherId: 1,
        subjectId: 1,
        classId: 1,
        sectionId: 1,
      ),
    ];
  }

  static List<TeacherClass> getMockTeacherClasses() {
    return [
      TeacherClass(
        id: 1,
        teacherId: 1,
        classId: 1,
      ),
    ];
  }
}
