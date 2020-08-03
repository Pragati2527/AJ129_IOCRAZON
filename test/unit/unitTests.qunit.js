/* global QUnit */
QUnit.config.autostart = false;

sap.ui.getCore().attachInit(function () {
	"use strict";

	sap.ui.require([
		"test/sih/test_sih/test/unit/AllTests"
	], function () {
		QUnit.start();
	});
});