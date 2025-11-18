import 'package:flutter/material.dart';
import 'package:provider/provider.dart'; // <--- Ajouter provider dans pubspec.yaml

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => ThemeProvider(),
      child: const SpeedRecommenderApp(),
    ),
  );
}

// -----------------------------------------------------------
// THEME PROVIDER
// -----------------------------------------------------------
class ThemeProvider extends ChangeNotifier {
  ThemeMode themeMode = ThemeMode.dark;

  void setTheme(ThemeMode mode) {
    themeMode = mode;
    notifyListeners();
  }
}

// -----------------------------------------------------------
// MAIN APP
// -----------------------------------------------------------
class SpeedRecommenderApp extends StatelessWidget {
  const SpeedRecommenderApp({super.key});

  @override
  Widget build(BuildContext context) {
    final themeProvider = Provider.of<ThemeProvider>(context);

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Softespeed',
      themeMode: themeProvider.themeMode,
      theme: ThemeData(
        brightness: Brightness.light,
        scaffoldBackgroundColor: Colors.white,
        fontFamily: "Roboto",
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.lightBlueAccent,
          brightness: Brightness.light,
        ),
        useMaterial3: true,
      ),
      darkTheme: ThemeData(
        brightness: Brightness.dark,
        scaffoldBackgroundColor: const Color(0xFF121212),
        fontFamily: "Roboto",
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blueAccent,
          brightness: Brightness.dark,
        ),
        useMaterial3: true,
      ),
      home: const DashboardPage(),
    );
  }
}

// -----------------------------------------------------------
// DASHBOARD PAGE
// -----------------------------------------------------------
class DashboardPage extends StatelessWidget {
  const DashboardPage({super.key});

  @override
  Widget build(BuildContext context) {
    final themeProvider = Provider.of<ThemeProvider>(context, listen: false);

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: const Text(
          "Softespeed Assistant",
          style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        actions: [
          PopupMenuButton<String>(
            onSelected: (value) {
              if (value == 'Dark') {
                themeProvider.setTheme(ThemeMode.dark);
              } else if (value == 'Light') {
                themeProvider.setTheme(ThemeMode.light);
              } else if (value == 'Pastel') {
                themeProvider.setTheme(ThemeMode.light); // on utilisera light + couleurs pastel
              }
            },
            itemBuilder: (context) => [
              const PopupMenuItem(value: 'Dark', child: Text('Dark Mode')),
              const PopupMenuItem(value: 'Light', child: Text('Light Mode')),
              const PopupMenuItem(value: 'Pastel', child: Text('Pastel Mode')),
            ],
            icon: const Icon(Icons.palette),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [

            // VITESSE RECOMMANDÉE
            Container(
              padding: const EdgeInsets.all(25),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: Theme.of(context).brightness == Brightness.dark
                      ? const [Color(0xFF4FC3F7), Color(0xFFB3E5FC)]
                      : const [Color(0xFF81D4FA), Color(0xFFB3E5FC)], // pastel clair
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(25),
                boxShadow: const [
                  BoxShadow(color: Colors.blueAccent, blurRadius: 20, spreadRadius: -5),
                ],
              ),
              child: Column(
                children: const [
                  Text(
                    "Vitesse Recommandée",
                    style: TextStyle(fontSize: 18, color: Colors.white70),
                  ),
                  SizedBox(height: 10),
                  Text(
                    "73 km/h",
                    style: TextStyle(
                      fontSize: 60,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // METRICS
            Row(
              children: const [
                Expanded(
                  child: MetricCard(
                    title: "Vigilance",
                    value: "87%",
                    color: Color(0xFFFFB74D), // orange pastel
                  ),
                ),
                SizedBox(width: 12),
                Expanded(
                  child: MetricCard(
                    title: "Risque",
                    value: "32%",
                    color: Color(0xFFE57373), // rouge pastel
                  ),
                ),
              ],
            ),

            const SizedBox(height: 30),

            // NAV BUTTONS
            Row(
              children: [
                Expanded(
                  child: NavButton(
                    icon: Icons.sensors,
                    label: "Capteurs",
                    onTap: () {},
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: NavButton(
                    icon: Icons.notifications_active,
                    label: "Alertes",
                    onTap: () {},
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

// -----------------------------------------------------------
// METRIC CARD
// -----------------------------------------------------------
class MetricCard extends StatelessWidget {
  final String title;
  final String value;
  final Color color;

  const MetricCard({super.key, required this.title, required this.value, required this.color});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white12,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: color.withOpacity(.5)),
      ),
      child: Column(
        children: [
          Text(
            title,
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: color),
          ),
          const SizedBox(height: 8),
          Text(
            value,
            style: TextStyle(fontSize: 34, fontWeight: FontWeight.bold, color: color),
          ),
        ],
      ),
    );
  }
}

// -----------------------------------------------------------
// NAV BUTTON
// -----------------------------------------------------------
class NavButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onTap;

  const NavButton({super.key, required this.icon, required this.label, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(20),
      child: Container(
        height: 110,
        decoration: BoxDecoration(
          color: Colors.white12,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: Colors.white24),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 40, color: Colors.lightBlueAccent),
            const SizedBox(height: 10),
            Text(label, style: const TextStyle(fontSize: 18)),
          ],
        ),
      ),
    );
  }
}
