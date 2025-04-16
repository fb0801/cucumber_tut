var { Given } = require('cucumber');

Given(/^I have a CV and I'm on the edit description page$/, function () {
  this.employee = new Employee('Sally');
  this.employee.createCV();
});