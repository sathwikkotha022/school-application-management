
import 'package:flutter/material.dart';
import '../widgets/custom_app_bar.dart';
import '../widgets/drawer_menu.dart';

class AdminUsersScreen extends StatelessWidget {
  const AdminUsersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const CustomAppBar(title: 'Users Management'),
      drawer: const DrawerMenu(),
      body: const Center(
        child: Text('Admin Users Management Screen - Coming Soon'),
      ),
    );
  }
}
