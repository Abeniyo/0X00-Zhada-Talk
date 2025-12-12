import 'package:flutter/material.dart';
import 'core/routes/app_pages.dart';
import 'core/theme/app_theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Zhada Talk",
      theme: AppTheme.lightTheme,
      initialRoute: AppPages.initial,
      routes: AppPages.routes,
    );
  }
}
