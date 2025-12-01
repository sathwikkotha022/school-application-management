import 'user_model.dart';
import 'class_model.dart';
import 'section_model.dart';

class Student {
  final int id;
  final int userId;
  final String rollNumber;
  final int classId;
  final int sectionId;
  final User? user;
  final SchoolClass? schoolClass;
  final Section? section;

  Student({
    required this.id,
    required this.userId,
    required this.rollNumber,
    required this.classId,
    required this.sectionId,
    this.user,
    this.schoolClass,
    this.section,
  });

  factory Student.fromJson(Map<String, dynamic> json) {
    return Student(
      id: json['id'],
      userId: json['user_id'],
      rollNumber: json['roll_number'],
      classId: json['class_id'],
      sectionId: json['section_id'],
      user: json['user'] != null ? User.fromJson(json['user']) : null,
      schoolClass: json['school_class'] != null ? SchoolClass.fromJson(json['school_class']) : null,
      section: json['section'] != null ? Section.fromJson(json['section']) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'user_id': userId,
      'roll_number': rollNumber,
      'class_id': classId,
      'section_id': sectionId,
      'user': user?.toJson(),
      'school_class': schoolClass?.toJson(),
      'section': section?.toJson(),
    };
  }
}
