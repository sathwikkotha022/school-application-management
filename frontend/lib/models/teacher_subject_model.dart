class TeacherSubject {
  final int id;
  final int teacherId;
  final int subjectId;
  final int classId;
  final int sectionId;

  TeacherSubject({
    required this.id,
    required this.teacherId,
    required this.subjectId,
    required this.classId,
    required this.sectionId,
  });

  factory TeacherSubject.fromJson(Map<String, dynamic> json) {
    return TeacherSubject(
      id: json['id'],
      teacherId: json['teacher_id'],
      subjectId: json['subject_id'],
      classId: json['class_id'],
      sectionId: json['section_id'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'teacher_id': teacherId,
      'subject_id': subjectId,
      'class_id': classId,
      'section_id': sectionId,
    };
  }
}
