/* global QUnit */
QUnit.config.autostart = false;

sap.ui.getCore().attachInit(function () {
	"use strict";

	sap.ui.require([
		"test/sih/test_sih/test/integration/AllJourneys"
	], function () {
		QUnit.start();
	});
});