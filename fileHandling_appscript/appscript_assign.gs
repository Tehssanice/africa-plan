// This function checks the delivery status of companies within the last two months.
function checkLastTwoMonthsDelivery() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var outputSheet = ss.getSheetByName("Sheet1");
  var companies = outputSheet.getRange("A2:A511").getValues(); // Get list of companies
  var batchSize = 50; // Process 50 companies at a time
  
  // Loop through companies in batches
  for (var i = 0; i < companies.length; i += batchSize) {
    var companyBatch = companies.slice(i, i + batchSize); // Get a batch of companies
    processCompanyBatch(companyBatch, outputSheet, i + 2); // Process the batch
  }
}

// This function processes a batch of companies
function processCompanyBatch(companyBatch, outputSheet, startRowIndex) {
  var deliveryData = getDeliveryData(); // Retrieve delivery data once
  
  // Loop through each company in the batch
  for (var i = 0; i < companyBatch.length; i++) {
    var company = companyBatch[i][0];
    var lastDelivery = getLastDelivery(company, deliveryData); // Get last delivery date
    var deliveryCount = getDeliveryCount(company, deliveryData); // Get delivery count

    // Set values in the output sheet based on delivery status
    if (lastDelivery) {
      outputSheet.getRange(startRowIndex + i, 2).setValue("True");
      outputSheet.getRange(startRowIndex + i, 3).setValue(lastDelivery);
    } else {
      outputSheet.getRange(startRowIndex + i, 2).setValue("False");
      outputSheet.getRange(startRowIndex + i, 3).setValue("N/A");
    }
    outputSheet.getRange(startRowIndex + i, 4).setValue(deliveryCount);
  }
}

// This function retrieves the last delivery date for a company
function getLastDelivery(company, deliveryData) {
  var lastDeliveryDate = null;

  // Loop through delivery data to find the last delivery date for the company within the last two months
  for (var i = 0; i < deliveryData.length; i++) {
    var row = deliveryData[i];
    if (row[0] == company) {
      var deliveryDate = new Date(row[1]);
      if (isBetween(deliveryDate, new Date("2023-11-01"), new Date("2024-01-30"))) { // Check if delivery date is within the last two months
        if (!lastDeliveryDate || deliveryDate > lastDeliveryDate) {
          lastDeliveryDate = deliveryDate; // Update last delivery date if the current delivery date is later
        }
      }
    }
  }
  return lastDeliveryDate ? getMonthYearString(lastDeliveryDate) : null; // Return last delivery date in a formatted string
}

// This function counts the number of deliveries for a company within the last two months
function getDeliveryCount(company, deliveryData) {
  var deliveryCount = 0;

  // Loop through delivery data to count deliveries for the company within the last two months
  for (var i = 0; i < deliveryData.length; i++) {
    var row = deliveryData[i];
    if (row[0] == company) {
      var deliveryDate = new Date(row[1]);
      if (isBetween(deliveryDate, new Date("2023-11-01"), new Date("2024-01-30"))) { // Check if delivery date is within the last two months
        deliveryCount++; // Increment delivery count
      }
    }
  }
  return deliveryCount; // Return delivery count
}

// This function retrieves delivery data from the sheets for the last two months
function getDeliveryData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var novemberSheet = ss.getSheetByName("November");
  var decemberSheet = ss.getSheetByName("December");
  var januarySheet = ss.getSheetByName("Jan24");
  var sheets = [novemberSheet, decemberSheet, januarySheet];
  var deliveryData = [];

  // Loop through sheets to retrieve delivery data
  for (var i = 0; i < sheets.length; i++) {
    var sheet = sheets[i];
    if (!sheet) continue;
    var dataRange = sheet.getDataRange();
    if (!dataRange) continue;
    var values = dataRange.getValues();
    deliveryData = deliveryData.concat(values); // Concatenate data from each sheet
  }
  return deliveryData; // Return combined delivery data
}

// This function checks if a date falls within a specified range
function isBetween(date, startDate, endDate) {
  return date >= startDate && date <= endDate; // Check if date falls within range
}

// This function formats a date as month, year
function getMonthYearString(date) {
  var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  return months[date.getMonth()] + ", " + date.getFullYear(); // Return formatted date string
}
