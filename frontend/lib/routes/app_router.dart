import 'package:go_router/go_router.dart';
import '../providers/auth_provider.dart';
import '../screens/login_screen.dart';
import '../screens/admin_dashboard_screen.dart';
import '../screens/teacher_dashboard_screen.dart';
import '../screens/student_dashboard_screen.dart';
import '../screens/teacher_mark_attendance_screen.dart';
import '../screens/student_attendance_screen.dart';

class AppRouter {
  static GoRouter router(AuthProvider authProvider) {
    return GoRouter(
      initialLocation: '/',
      refreshListenable: authProvider,
      routes: [
        GoRoute(
          path: '/',
          builder: (context, state) => const LoginScreen(),
        ),
        GoRoute(
          path: '/admin-dashboard',
          builder: (context, state) => const AdminDashboardScreen(),
        ),
        GoRoute(
          path: '/teacher-dashboard',
          builder: (context, state) => const TeacherDashboardScreen(),
        ),
        GoRoute(
          path: '/student-dashboard',
          builder: (context, state) => const StudentDashboardScreen(),
        ),
        GoRoute(
          path: '/teacher-mark-attendance',
          builder: (context, state) => const TeacherMarkAttendanceScreen(),
        ),
        GoRoute(
          path: '/student-attendance',
          builder: (context, state) => const StudentAttendanceScreen(),
        ),
      ],
      redirect: (context, state) {
        final isAuthenticated = authProvider.isAuthenticated;
        final user = authProvider.user;

        // If not authenticated and not on login page, redirect to login
        if (!isAuthenticated && state.matchedLocation != '/') {
          return '/';
        }

        // If authenticated, redirect to appropriate dashboard
        if (isAuthenticated && state.matchedLocation == '/') {
          switch (user?.role) {
            case 'admin':
              return '/admin-dashboard';
            case 'teacher':
              return '/teacher-dashboard';
            case 'student':
              return '/student-dashboard';
            default:
              return '/';
          }
        }

        return null;
      },
    );
  }
}
