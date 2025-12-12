import 'package:flutter/material.dart';
import 'app_routes.dart';
import '../../screens/landing/landing_page.dart';
import '../../screens/auth/login_page.dart';
import '../../screens/auth/register_page.dart';
import '../../screens/auth/forgot_password_page.dart';
import '../../screens/auth/reset_password_page.dart';

class AppPages {
  static const initial = AppRoutes.landing;

  static Map<String, WidgetBuilder> routes = {
    AppRoutes.landing: (context) => const LandingPage(),
    AppRoutes.login: (context) => const LoginPage(),
    AppRoutes.register: (context) => const RegisterPage(),
    AppRoutes.forgotPassword: (context) => const ForgotPasswordPage(),
    AppRoutes.resetPassword: (context) => const ResetPasswordPage(),
  };
}
