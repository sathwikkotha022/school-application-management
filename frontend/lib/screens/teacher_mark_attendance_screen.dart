import 'package:flutter/material.dart';
import '../widgets/custom_app_bar.dart';
import '../widgets/drawer_menu.dart';

class TeacherMarkAttendanceScreen extends StatelessWidget {
  const TeacherMarkAttendanceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const CustomAppBar(title: 'Mark Attendance'),
      drawer: const DrawerMenu(),
      body: const Center(
        child: Text('Mark Student Attendance Screen - Coming Soon'),
      ),
    );
  }
}
