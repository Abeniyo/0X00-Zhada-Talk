import 'package:flutter/material.dart';

class ForgotPasswordPage extends StatelessWidget {
  const ForgotPasswordPage({super.key});

  @override
  Widget build(BuildContext context) {
    final email = TextEditingController();

    return Scaffold(
      appBar: AppBar(title: const Text("Forgot Password")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: email, decoration: const InputDecoration(labelText: "Enter your email")),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {},
              child: const Text("Send Reset Link"),
            ),
          ],
        ),
      ),
    );
  }
}
