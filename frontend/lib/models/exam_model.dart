class Exam {
  final int id;
  final String name;
  final String date;

  Exam({
    required this.id,
    required this.name,
    required this.date,
  });

  factory Exam.fromJson(Map<String, dynamic> json) {
    return Exam(
      id: json['id'],
      name: json['name'],
      date: json['date'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'date': date,
    };
  }

  // Mock data
  static List<Exam> getMockExams() {
    return [
      Exam(id: 1, name: 'Mid Term Exam', date: '2024-02-15'),
      Exam(id: 2, name: 'Final Exam', date: '2024-05-20'),
      Exam(id: 3, name: 'Unit Test 1', date: '2024-01-10'),
      Exam(id: 4, name: 'Unit Test 2', date: '2024-03-05'),
    ];
  }
}
