

var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
    }
};

Survey
    .StylesManager
    .applyTheme("default");

var surveyJSON = {locale:"en",title:"What are your priorities?",completedHtml:"You have completed identifying your first year priorities.",pages:[{name:"page1",elements:[{type:"matrixdropdown",name:"frameworksRate",title:"Identify and rank your top five prorities for this academic year. (1 = most important.)",columns:[{name:"rate",title:"Rank your priorities for this academic year."},{name:"knowledge",title:"Please provide a brief explanation.",cellType:"text"}],choices:["Priority #1","Priority #2","Priority #3","Priority #4","Priority #5","Not a priority","Important, not a top priority."],rows:[{value:"fypriorities01",text:"Declare my major."},{value:"fypriorities02",text:"Identify the requirements for my program of study."},{value:"fypriorities03",text:"Maintain a GPA of _____."},{value:"fypriorities04",text:"Increase use of on campus academic support services."},{value:"fypriorities05",text:"Research and identify potential career options."},{value:"fypriorities06",text:"Increase my involvement in on-campus activities."},{value:"fypriorities07",text:"Improve management of my personal finances."},{value:"fypriorities08",text:"Increase connection and communication with faculty and advisors."},{value:"fypriorities09",text:"Increase my involvement in on-campus activities."},{value:"fypriorities10",text:"Improve my living situation."}]},{type:"html",name:"question1"}]}],triggers:[{type:"complete",operator:"notempty",name:"frameworksRate.fypriorities10.knowledge"}],sendResultOnPageNext:true,showProgressBar:"bottom",goNextPageAutomatic:true}

window.survey = new Survey.Model(surveyJSON);

survey
    .onComplete
    .add(function (result) {
        document
            .querySelector('#surveyResult')
            .innerHTML = "result: " + JSON.stringify(result.data);
    });

survey.data = {
    name: 'John Doe',
    email: 'johndoe@nobody.com',
    car: ['Ford']
};

$("#surveyElement").Survey({model: survey, onValueChanged: surveyValueChanged});