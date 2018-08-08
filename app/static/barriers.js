

var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
    }
};
  
Survey
    .StylesManager
    .applyTheme("default");

var surveyJSON = {"pages":[{"name":"page1","elements":[{"type":"checkbox","name":"Potential barriers to success","title":"From the list below, select the barriers that you think could make it harder for you to be successful in college this year. Please select all that apply.","isRequired":true,"choices":[{"value":"Reading","text":"I'm a slow reader."},{"value":"Writing","text":"I don't write well enough."},{"value":"Language","text":"English is my second language."},{"value":"Emotional_1","text":"College life is stressful."},{"value":"Financial_1","text":"I don't have enough money."},{"value":"Social_1","text":"I'm in a serious relationship."},{"value":"Social_2","text":"I worry I will party too much."},{"value":"Social_3","text":"It's hard for me to make friends."},{"value":"Financial_2","text":"I'm worried about my financial aid."},{"value":"Emotional_2","text":"I feel overwhelmed."},{"value":"Social_4","text":"I don't know if I belong here."},{"value":"Race","text":"Descrimination because of my race\\ethnicity."}],"choicesOrder":"asc","colCount":2}]}]}

window.survey = new Survey.Model(surveyJSON);

survey
    .onComplete
    .add(function (result) {
        document
            .querySelector('#surveyResult')
            .innerHTML = "result: " + JSON.stringify(result.data);
    });

$("#surveyElement").Survey({model: survey, onValueChanged: surveyValueChanged});