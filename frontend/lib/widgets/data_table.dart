import 'package:flutter/material.dart';

class CustomDataTable<T> extends StatelessWidget {
  final List<String> columns;
  final List<T> data;
  final Widget Function(T item, int index) rowBuilder;
  final int? maxRows;

  const CustomDataTable({
    super.key,
    required this.columns,
    required this.data,
    required this.rowBuilder,
    this.maxRows,
  });

  @override
  Widget build(BuildContext context) {
    final displayData = maxRows != null ? data.take(maxRows!).toList() : data;

    return Card(
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: DataTable(
          columns: columns.map((col) => DataColumn(label: Text(col))).toList(),
          rows: List.generate(
            displayData.length,
            (index) => DataRow(
              cells: [
                DataCell(rowBuilder(displayData[index], index)),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class SimpleListView<T> extends StatelessWidget {
  final List<T> items;
  final Widget Function(T item, int index) itemBuilder;
  final String? emptyMessage;

  const SimpleListView({
    super.key,
    required this.items,
    required this.itemBuilder,
    this.emptyMessage,
  });

  @override
  Widget build(BuildContext context) {
    if (items.isEmpty) {
      return Center(
        child: Text(
          emptyMessage ?? 'No items found',
          style: Theme.of(context).textTheme.bodyLarge,
        ),
      );
    }

    return ListView.builder(
      itemCount: items.length,
      itemBuilder: (context, index) {
        return itemBuilder(items[index], index);
      },
    );
  }
}
