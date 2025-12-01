import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';

class CustomAppBar extends StatelessWidget implements PreferredSizeWidget {
  final String title;
  final List<Widget>? actions;
  final bool showProfileButton;
  final bool showLogoutButton;

  const CustomAppBar({
    super.key,
    required this.title,
    this.actions,
    this.showProfileButton = true,
    this.showLogoutButton = true,
  });

  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);

    return AppBar(
      title: Text(title),
      elevation: 2,
      actions: [
        if (showProfileButton)
          IconButton(
            icon: const Icon(Icons.person),
            onPressed: () {
              // Navigate to profile screen based on role
              final role = authProvider.userRole;
              switch (role) {
                case 'student':
                  // Navigate to student profile
                  break;
                case 'teacher':
                  // Navigate to teacher profile
                  break;
                case 'admin':
                  // Navigate to admin profile
                  break;
              }
            },
            tooltip: 'Profile',
          ),
        if (showLogoutButton)
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              _showLogoutDialog(context, authProvider);
            },
            tooltip: 'Logout',
          ),
        if (actions != null) ...actions!,
      ],
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

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}
