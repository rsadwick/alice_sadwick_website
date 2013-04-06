function compDate(parm1)
{
    var date1 = new Date(parm1);
    var date2 = new Date();
    return (date2-date1)/(1000*60*60*24*7).toFixed(2);
}

var some_variable = compDate("August 23, 2010"); // Change to appropriate date

function weeks_between(date1, date2) {
    // The number of milliseconds in one week
    var ONE_WEEK = 1000 * 60 * 60 * 24 * 7;
    // Convert both dates to milliseconds
    var date1_ms = date1.getTime();
    var date2_ms = date2.getTime();
    // Calculate the difference in milliseconds
    var difference_ms = Math.abs(date1_ms - date2_ms);
    // Convert back to weeks and return hole weeks
    return Math.floor(difference_ms / ONE_WEEK);
}