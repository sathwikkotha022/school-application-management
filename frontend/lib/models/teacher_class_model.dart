class TeacherClass {
  final int id;
  final int teacherId;
  final int classId;

  TeacherClass({
    required this.id,
    required this.teacherId,
    required this.classId,
  });

  factory TeacherClass.fromJson(Map<String, dynamic> json) {
    return TeacherClass(
      id: json['id'],
      teacherId: json['teacher_id'],
      classId: json['class_id'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'teacher_id': teacherId,
      'class_id': classId,
    };
  }
}
