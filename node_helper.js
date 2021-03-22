/* Magic Mirror
 * Node Helper: magic_mirror_face_recognition
 *
 * By Tom Wenzel
 * MIT Licensed.
 */

var NodeHelper = require("node_helper");

module.exports = NodeHelper.create({

	// Override socketNotificationReceived method.

	/* socketNotificationReceived(notification, payload) Orange
	   * This method is called when a socket notification arrives.
	   *
	   * argument notification string - The identifier of the noitication.
	   * argument payload mixed - The payload of the notification.
	   */
	socketNotificationReceived: function (notification, payload) {
		if (notification === "magic_mirror_face_recognition-NOTIFICATION_TEST") {
			console.log("Working notification system. Notification:", notification, "payload: ", payload);
			// Send notification
			this.sendNotificationTest(this.anotherFunction()); //Is possible send objects :)
		}
	},

	// Example function send notification test
	sendNotificationTest: function (payload) {
		this.sendSocketNotification("magic_mirror_face_recognition-NOTIFICATION_TEST", payload);
	},

	// this you can create extra routes for your module
	extraRoutes: function () {
		var self = this;
		this.expressApp.get("/magic_mirror_face_recognition/extra_route", function (req, res) {
			// call another function
			values = self.anotherFunction();
			res.send(values);
		});
	},

	// Test another function
	anotherFunction: function () {
		return {date: new Date()};
	}
});
