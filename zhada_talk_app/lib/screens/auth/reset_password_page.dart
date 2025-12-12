import 'package:flutter/material.dart';

class ResetPasswordPage extends StatelessWidget {
  const ResetPasswordPage({super.key});

  @override
  Widget build(BuildContext context) {
    final pass = TextEditingController();
    final confirm = TextEditingController();

    return Scaffold(
      appBar: AppBar(title: const Text("Reset Password")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(controller: pass, obscureText: true, decoration: const InputDecoration(labelText: "New Password")),
            TextField(controller: confirm, obscureText: true, decoration: const InputDecoration(labelText: "Confirm Password")),
            const SizedBox(height: 20),
            ElevatedButton(onPressed: () {}, child: const Text("Reset Password")),
          ],
        ),
      ),
    );
  }
}
