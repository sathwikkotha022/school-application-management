import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';
import '../services/student_service.dart';
import '../models/attendance_model.dart';
import '../widgets/loading_indicator.dart';
import '../widgets/error_message.dart';

class StudentAttendanceScreen extends StatefulWidget {
  const StudentAttendanceScreen({super.key});

  @override
  State<StudentAttendanceScreen> createState() => _StudentAttendanceScreenState();
}

class _StudentAttendanceScreenState extends State<StudentAttendanceScreen> {
  List<StudentAttendance> _attendances = [];
  bool _isLoading = true;
  String? _error;
  int _skip = 0;
  final int _limit = 50;
  bool _hasMore = true;

  @override
  void initState() {
    super.initState();
    _loadAttendance();
  }

  Future<void> _loadAttendance({bool loadMore = false}) async {
    try {
      if (!loadMore) {
        setState(() {
          _isLoading = true;
          _error = null;
          _skip = 0;
        });
      }

      final attendances = await StudentService.getStudentAttendance(
        1, // mock studentId
        skip: _skip,
        limit: _limit,
      );

      setState(() {
        if (loadMore) {
          _attendances.addAll(attendances);
        } else {
          _attendances = attendances;
        }
        _hasMore = attendances.length == _limit;
        _skip += attendances.length;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _error = e.toString();
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('My Attendance'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: () => _loadAttendance(),
          ),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              authProvider.logout();
            },
          ),
        ],
      ),
      body: _isLoading && _attendances.isEmpty
          ? const LoadingIndicator()
          : _error != null
              ? ErrorMessage(
                  message: _error!,
                  onRetry: () => _loadAttendance(),
                )
              : _buildAttendanceContent(),
    );
  }

  Widget _buildAttendanceContent() {
    if (_attendances.isEmpty) {
      return const Center(
        child: Text('No attendance records found'),
      );
    }

    return Column(
      children: [
        // Summary Card
        Card(
          margin: const EdgeInsets.all(16.0),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildSummaryItem(
                  'Total Days',
                  _attendances.length.toString(),
                  Colors.blue,
                ),
                _buildSummaryItem(
                  'Present',
                  _attendances.where((a) => a.status == 'present').length.toString(),
                  Colors.green,
                ),
                _buildSummaryItem(
                  'Absent',
                  _attendances.where((a) => a.status == 'absent').length.toString(),
                  Colors.red,
                ),
                _buildSummaryItem(
                  'Late',
                  _attendances.where((a) => a.status == 'late').length.toString(),
                  Colors.orange,
                ),
              ],
            ),
          ),
        ),

        // Attendance List
        Expanded(
          child: ListView.builder(
            itemCount: _attendances.length + (_hasMore ? 1 : 0),
            itemBuilder: (context, index) {
              if (index == _attendances.length) {
                // Load more indicator
                return Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: ElevatedButton(
                    onPressed: () => _loadAttendance(loadMore: true),
                    child: const Text('Load More'),
                  ),
                );
              }

              final attendance = _attendances[index];
              return _buildAttendanceCard(attendance);
            },
          ),
        ),
      ],
    );
  }

  Widget _buildSummaryItem(String label, String value, Color color) {
    return Column(
      children: [
        Text(
          value,
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
        const SizedBox(height: 4),
        Text(
          label,
          style: TextStyle(
            fontSize: 12,
            color: Colors.grey[600],
          ),
        ),
      ],
    );
  }

  Widget _buildAttendanceCard(StudentAttendance attendance) {
    Color statusColor;
    IconData statusIcon;

    switch (attendance.status.toLowerCase()) {
      case 'present':
        statusColor = Colors.green;
        statusIcon = Icons.check_circle;
        break;
      case 'absent':
        statusColor = Colors.red;
        statusIcon = Icons.cancel;
        break;
      case 'late':
        statusColor = Colors.orange;
        statusIcon = Icons.schedule;
        break;
      default:
        statusColor = Colors.grey;
        statusIcon = Icons.help;
    }

    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 4.0),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: statusColor.withValues(alpha: 0.1),
          child: Icon(
            statusIcon,
            color: statusColor,
          ),
        ),
        title: Text(
          attendance.subject?.name ?? 'Unknown Subject',
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Date: ${attendance.date}'),
            Text('Teacher: ${attendance.teacher?.user?.firstName ?? ''} ${attendance.teacher?.user?.lastName ?? ''}'.trim()),
            if (attendance.remarks != null && attendance.remarks!.isNotEmpty)
              Text('Remarks: ${attendance.remarks}'),
          ],
        ),
        trailing: Container(
          padding: const EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
          decoration: BoxDecoration(
            color: statusColor.withValues(alpha: 0.1),
            borderRadius: BorderRadius.circular(12.0),
          ),
          child: Text(
            attendance.status.toUpperCase(),
            style: TextStyle(
              color: statusColor,
              fontWeight: FontWeight.bold,
              fontSize: 12,
            ),
          ),
        ),
      ),
    );
  }
}
