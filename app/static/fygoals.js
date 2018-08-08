
    
var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
    }
};

Survey
    .StylesManager
    .applyTheme("default");

var fygoalJSON = {"locale":"en","title":"First Year SMART Goal","completedHtml":{"en":"Congratulations. You have created your SMART goal."},"pages":[{"name":"page1","elements":[{"type":"comment","name":"FirstDraftGoal","title":"In the space provided below, write a specific SMART goals that you would like to accomplish by the end of the academic year. Remember: Provide as much detail as needed to enable your anyone - a friend, professor or your advisor - to picture it clearly in their mind. "},{"type":"text","name":"startDate","title":"Goal Start Date: Enter the date that you will create and implement a plan to achieve your goal. ","isRequired":true,"inputType":"date"},{"type":"text","name":"endDate","title":"Goal Completion Date: Enter the date that you will complete your goal. ","inputType":"date"}]},{"name":"page2","elements":[{"type":"html","name":"question1","visibleIf":"{FirstDraftSMART}","html":{"en":"\n<!DOCTYPE html>\n<html>\n    <head>\n        <title>Smart Goal First Draft</title>\n        <script src=\"https://unpkg.com/jquery\"></script>\n        <script src=\"https://surveyjs.azureedge.net/1.0.11/survey.jquery.js\"></script>\n        <link href=\"https://surveyjs.azureedge.net/1.0.11/survey.css\" type=\"text/css\" rel=\"stylesheet\"/>\n        <link rel=\"stylesheet\" href=\"./index.css\">\n    </head>\n    <body>\n        <p></p>\n\n<script type=\"text/javascript\" src=\"./index.js\"></script>\n<script>\n\n</script>\n    </body>\n</html>\n"}},{"type":"comment","name":"specific_fy01","title":"Is your goal specific? Your goal should enable you and others to clearly understand and measure the result of your goal. \nSpecific: \"I want to achieve a 3.0 grade point average or better by the end of this academic year.\" \"\nNot specific: \"I want to improve my grade point average.\"\n","isRequired":true},{"type":"comment","name":"measurable_fy01","title":"Is your goal measurable? How will you know that you have accomplished your goal? Will you be able to demonstrate to others that you achieved it? Measurable: \"By the end of the year, I will add $1,000 to my savings account.\" Not measurable: \"I will save enough money to buy a car.\"","isRequired":true},{"type":"comment","name":"achievable_fy01","title":"Is your goal realistic? Can you realistically achieve your goal with your current knowledge, skills, and resources? If no, how will you get the knowledge and resources to achieve your goal.","isRequired":true},{"type":"comment","name":"relevant_fy01","title":"Is your goal relevant? Why is the goal important to you? In what ways will it benefit your life?","isRequired":true},{"type":"comment","name":"timely_fy01","title":"Is your goal timely? Explain why you believe that you can realistically achieve your goal by the completion date? What will you do to ensure you can meet the deadline?","isRequired":true}]},{"name":"page3","elements":[{"type":"comment","name":"finalGoal_fy01","title":"Based on your review, revise your goal as necessary to ensure that is it Specific, Measurable, Achievable, Relevant, and Timely."}]}],"sendResultOnPageNext":true,"showProgressBar":"bottom","goNextPageAutomatic":true}
    
window.survey = new Survey.Model(fygoalJSON);

survey
    .onComplete
    .add(function (result) {
        var myFyGoals = result;
        var fyJGoalsData = result.data;
        document
            .querySelector('#fygoalResult')
            .innerHTML = "result: " + JSON.stringify(result.data);
    });

$("#surveyElement").Survey({model: survey, onValueChanged: surveyValueChanged});