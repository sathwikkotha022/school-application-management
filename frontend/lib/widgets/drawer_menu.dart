import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:go_router/go_router.dart';
import '../providers/auth_provider.dart';

class DrawerMenu extends StatelessWidget {
  const DrawerMenu({super.key});

  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);
    final userRole = authProvider.userRole;

    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          _buildDrawerHeader(context, authProvider),
          _buildDrawerItems(context, userRole),
          const Divider(),
          _buildLogoutItem(context, authProvider),
        ],
      ),
    );
  }

  Widget _buildDrawerHeader(BuildContext context, AuthProvider authProvider) {
    return UserAccountsDrawerHeader(
      accountName: Text(
        '${authProvider.user?.firstName ?? ''} ${authProvider.user?.lastName ?? ''}'.trim(),
        style: const TextStyle(fontWeight: FontWeight.bold),
      ),
      accountEmail: Text(authProvider.user?.email ?? ''),
      currentAccountPicture: CircleAvatar(
        backgroundColor: Theme.of(context).primaryColor,
        child: Text(
          authProvider.user?.firstName?.substring(0, 1).toUpperCase() ?? 'U',
          style: const TextStyle(
            fontSize: 24,
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
      decoration: BoxDecoration(
        color: Theme.of(context).primaryColor,
      ),
    );
  }

  Widget _buildDrawerItems(BuildContext context, String? userRole) {
    switch (userRole) {
      case 'admin':
        return _buildAdminDrawerItems(context);
      case 'teacher':
        return _buildTeacherDrawerItems(context);
      case 'student':
        return _buildStudentDrawerItems(context);
      default:
        return const SizedBox.shrink();
    }
  }

  Widget _buildAdminDrawerItems(BuildContext context) {
    return Column(
      children: [
        ListTile(
          leading: const Icon(Icons.dashboard),
          title: const Text('Dashboard'),
          onTap: () {
            context.go('/admin');
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.people),
          title: const Text('Users'),
          onTap: () {
            // Navigate to users management
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.class_),
          title: const Text('Classes'),
          onTap: () {
            // Navigate to classes management
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.subject),
          title: const Text('Subjects'),
          onTap: () {
            // Navigate to subjects management
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.calendar_today),
          title: const Text('Exams'),
          onTap: () {
            // Navigate to exams management
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.bar_chart),
          title: const Text('Attendance Reports'),
          onTap: () {
            // Navigate to attendance reports
            Navigator.of(context).pop();
          },
        ),
      ],
    );
  }

  Widget _buildTeacherDrawerItems(BuildContext context) {
    return Column(
      children: [
        ListTile(
          leading: const Icon(Icons.dashboard),
          title: const Text('Dashboard'),
          onTap: () {
            context.go('/teacher');
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.calendar_today),
          title: const Text('Mark Attendance'),
          onTap: () {
            // Navigate to mark attendance
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.grade),
          title: const Text('Enter Marks'),
          onTap: () {
            // Navigate to enter marks
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.schedule),
          title: const Text('My Attendance'),
          onTap: () {
            // Navigate to teacher attendance
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.class_),
          title: const Text('My Classes'),
          onTap: () {
            // Navigate to my classes
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.subject),
          title: const Text('My Subjects'),
          onTap: () {
            // Navigate to my subjects
            Navigator.of(context).pop();
          },
        ),
      ],
    );
  }

  Widget _buildStudentDrawerItems(BuildContext context) {
    return Column(
      children: [
        ListTile(
          leading: const Icon(Icons.dashboard),
          title: const Text('Dashboard'),
          onTap: () {
            context.go('/student');
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.person),
          title: const Text('My Profile'),
          onTap: () {
            context.go('/student/profile');
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.calendar_today),
          title: const Text('Attendance'),
          onTap: () {
            context.go('/student/attendance');
            Navigator.of(context).pop();
          },
        ),
        ListTile(
          leading: const Icon(Icons.grade),
          title: const Text('Marks'),
          onTap: () {
            context.go('/student/marks');
            Navigator.of(context).pop();
          },
        ),
      ],
    );
  }

  Widget _buildLogoutItem(BuildContext context, AuthProvider authProvider) {
    return ListTile(
      leading: const Icon(Icons.logout, color: Colors.red),
      title: const Text(
        'Logout',
        style: TextStyle(color: Colors.red),
      ),
      onTap: () {
        Navigator.of(context).pop();
        _showLogoutDialog(context, authProvider);
      },
    );
  }

  void _showLogoutDialog(BuildContext context, AuthProvider authProvider) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Logout'),
          content: const Text('Are you sure you want to logout?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
                authProvider.logout();
              },
              style: TextButton.styleFrom(
                foregroundColor: Theme.of(context).colorScheme.error,
              ),
              child: const Text('Logout'),
            ),
          ],
        );
      },
    );
  }
}
