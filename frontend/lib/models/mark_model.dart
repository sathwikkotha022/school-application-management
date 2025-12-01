import 'student_model.dart';
import 'subject_model.dart';
import 'exam_model.dart';

class Mark {
  final int id;
  final int studentId;
  final int subjectId;
  final int examId;
  final double marksObtained;
  final double totalMarks;
  final Student? student;
  final Subject? subject;
  final Exam? exam;

  Mark({
    required this.id,
    required this.studentId,
    required this.subjectId,
    required this.examId,
    required this.marksObtained,
    required this.totalMarks,
    this.student,
    this.subject,
    this.exam,
  });

  factory Mark.fromJson(Map<String, dynamic> json) {
    return Mark(
      id: json['id'],
      studentId: json['student_id'],
      subjectId: json['subject_id'],
      examId: json['exam_id'],
      marksObtained: json['marks_obtained'].toDouble(),
      totalMarks: json['total_marks'].toDouble(),
      student: json['student'] != null ? Student.fromJson(json['student']) : null,
      subject: json['subject'] != null ? Subject.fromJson(json['subject']) : null,
      exam: json['exam'] != null ? Exam.fromJson(json['exam']) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'student_id': studentId,
      'subject_id': subjectId,
      'exam_id': examId,
      'marks_obtained': marksObtained,
      'total_marks': totalMarks,
      'student': student?.toJson(),
      'subject': subject?.toJson(),
      'exam': exam?.toJson(),
    };
  }
}
