sap.ui.define([
	"sap/ui/core/mvc/Controller"
], function (Controller) {
	"use strict";

	return Controller.extend("test.sih.test_sih.controller.View1", {
		onInit: function () {

		},

		onAfterRendering: function () {},

		getData: function () {
//			this.aws = [{
//				'VID': 'Vendor 1',
//				'Date': '3-8-2020',
//				'Quantity': 3.41,
//				'Email': 'amirraaj0@gmail.com',
//				'TID': 'd76daad7-1f08-44fb-9d47-ebf8baa4ab73'
//			}, {
//				'VID': 'Vendor 1',
//				'Date': '3-8-2020',
//				'Quantity': 2.07,
//				'Email': 'amirraaj0@gmail.com',
//				'TID': 'aabde6ac-287b-489d-ad08-26739f410300'
//			}];
//
//			this.mysql = [{
//				'date': '3-8-2020',
//				'tid': 'aabde6ac-287b-489d-ad08-26739f410300',
//				'vid': 'Vendor 1',
//				'amount': 2.070,
//				'email': 'amirraaj0@gmail.com'
//			}, {
//				'date': '3-8-2020',
//				'tid': 'd76daad7-1f08-44fb-9d47-ebf8baa4ab73',
//				'vid': 'Vendor 1',
//				'amount': 4.410,
//				'email': 'amirraaj0@gmail.com'
//			}];
            var em = this.getView().byId("email").getValue();
            var  that = this;
			$.ajax({
                url:'http://localhost:5000/get',
                type:'POST',
                headers:{
                    "Content-Type":"application/json"
                },
                data:JSON.stringify({email:em}),
                async:false,
                success:function(r){
                    that.aws =r;
                    $.ajax({
                url:'http://localhost:5000/local',
                type:'POST',
                headers:{
                    "Content-Type":"application/json"
                },
                data:JSON.stringify({email:em}),
                async:false,
                success:function(r){
                    that.mysql = r;
                    that.setData();
                },error:function(e){
                    console.log(e);
                }
                    });
                           
                },error:function(e){
                    console.log(e);
                }
            });
			
		},

		setData: function () {
			var aws = this.aws;
			var mysql = this.mysql;

			var data = {
				r: []
			};

			for (var i = 0; i < mysql.length; i++) {

				for (var j = 0; j < aws.length; j++) {
					
					if (mysql[i].tid === aws[j].TID) {
						var match = "match";
						var status = "Success";

						if (aws[j].Quantity !== mysql[i].amount) {
							var match = "no match";
							var status = "Error";
						}
						data.r.push({
							aws: aws[j],
							mysql: mysql[i],
							match:match,
							state:status
						})

						break;
					}
					
					
				}

			}
			
			this.getView().byId("list").setModel(new sap.ui.model.json.JSONModel(data));
			
		}
	});
});