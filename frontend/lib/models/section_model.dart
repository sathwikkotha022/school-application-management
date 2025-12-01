class Section {
  final int id;
  final String name;
  final int classId;

  Section({
    required this.id,
    required this.name,
    required this.classId,
  });

  factory Section.fromJson(Map<String, dynamic> json) {
    return Section(
      id: json['id'],
      name: json['name'],
      classId: json['class_id'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'class_id': classId,
    };
  }
}
