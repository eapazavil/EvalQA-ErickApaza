import 'package:flutter_driver/flutter_driver.dart';
import 'package:test/test.dart';

void main() {
  group('Flutter App', () {
    final usernameField = find.byValueKey('username');
    final passwordField = find.byValueKey('password');
    final loginButton = find.byValueKey('loginButton');
    final employeeList = find.byValueKey('employeeList');

    FlutterDriver driver;

    setUpAll(() async {
      driver = await FlutterDriver.connect();
    });

    tearDownAll(() async {
      if (driver != null) {
        await driver.close();
      }
    });

    test('Inicio de sesión', () async {
      await driver.tap(usernameField);
      await driver.enterText('prueba');
      await driver.tap(passwordField);
      await driver.enterText('prueba');
      await driver.tap(loginButton);

      await driver.waitFor(employeeList);

      expect(await driver.getText(find.byValueKey('viewTitle')), 'Empleados');
    });

    test('Medición de rendimiento', () async {
      final timeline = await driver.traceAction(() async {
        await driver.tap(usernameField);
        await driver.enterText('prueba');
        await driver.tap(passwordField);
        await driver.enterText('prueba');
        await driver.tap(loginButton);
        await driver.waitFor(employeeList);
      });

      final summary = TimelineSummary.summarize(timeline);
      await summary.writeSummaryToFile('login_performance', pretty: true);
      await summary.writeTimelineToFile('login_performance', pretty: true);
    });

    test('Medir tiempo de carga de la lista de empleados', () async {
      final timeline = await driver.traceAction(() async {
        await driver.tap(usernameField);
        await driver.enterText('prueba');
        await driver.tap(passwordField);
        await driver.enterText('prueba');
        await driver.tap(loginButton);
        await driver.waitFor(employeeList);
      });

      final summary = TimelineSummary.summarize(timeline);
      await summary.writeSummaryToFile('carga_lista_empleados', pretty: true);
      await summary.writeTimelineToFile('carga_lista_empleados', pretty: true);
    });
  });
}
