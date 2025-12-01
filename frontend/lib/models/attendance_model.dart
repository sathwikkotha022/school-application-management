import 'student_model.dart';
import 'teacher_model.dart';
import 'subject_model.dart';

class StudentAttendance {
  final int id;
  final int studentId;
  final int? teacherId;
  final int subjectId;
  final int classId;
  final int sectionId;
  final String date;
  final String status; // 'present', 'absent', 'late'
  final String? remarks;
  final DateTime? createdAt;
  final Student? student;
  final Teacher? teacher;
  final Subject? subject;

  StudentAttendance({
    required this.id,
    required this.studentId,
    this.teacherId,
    required this.subjectId,
    required this.classId,
    required this.sectionId,
    required this.date,
    required this.status,
    this.remarks,
    this.createdAt,
    this.student,
    this.teacher,
    this.subject,
  });

  factory StudentAttendance.fromJson(Map<String, dynamic> json) {
    return StudentAttendance(
      id: json['id'],
      studentId: json['student_id'],
      teacherId: json['teacher_id'],
      subjectId: json['subject_id'],
      classId: json['class_id'],
      sectionId: json['section_id'],
      date: json['date'],
      status: json['status'],
      remarks: json['remarks'],
      createdAt: json['created_at'] != null ? DateTime.parse(json['created_at']) : null,
      student: json['student'] != null ? Student.fromJson(json['student']) : null,
      teacher: json['teacher'] != null ? Teacher.fromJson(json['teacher']) : null,
      subject: json['subject'] != null ? Subject.fromJson(json['subject']) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'student_id': studentId,
      'teacher_id': teacherId,
      'subject_id': subjectId,
      'class_id': classId,
      'section_id': sectionId,
      'date': date,
      'status': status,
      'remarks': remarks,
      'created_at': createdAt?.toIso8601String(),
      'student': student?.toJson(),
      'teacher': teacher?.toJson(),
      'subject': subject?.toJson(),
    };
  }
}


