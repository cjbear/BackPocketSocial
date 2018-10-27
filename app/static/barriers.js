

var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
        el.text = options.text;
    }
};
  
Survey
    .StylesManager
    .applyTheme("default");

var fybarriersJSON = {
    locale: "en",
    title: "First Year Barriers",
    completedHtml: "You have completed the barriers assessment.",
    pages: [
     {
      name: "page1",
      elements: [
       {
        type: "checkbox",
        name: "Potential barriers to success",
        title: {
         default: "From the list below, select the barriers that you think could make it harder for you to be successful in college this year. Please select all that apply.",
         en: "From the list below, select the barriers that you think could make it harder for you to be successful in college this year. Please select all that apply.\n\nI worry that..."
        },
        choices: [
         {
          value: "Intellectual_01",
          text: "I'm a slow reader."
         },
         {
          value: "Intellectual_02",
          text: "I don't write well enough."
         },
         {
          value: "Intellectual_03",
          text:  "because English is my second language, communication will be too difficult."
         },
         {
          value: "Emotional_01",
          text:  "I will be too stressed or anxious."
         },
         {
          value: "Financial_01",
          text: "I won't have enough money..",
         },
         {
          value: "Social_01",
          text: "my family will not understand or support me."
         },
         {
          value: "Social_02",
          text: "I worry I will party too much."
         },
         {
          value: "Social_03",
          text: "I won't make friends."
         },
         {
          value: "Emotional_02",
          text: "I feel overwhelmed, anxious, and stressed."
         },
         {
          value: "Social_04",
          text: "I don't know if I belong here."
         },
         {
          value: "Social_05",
          text:  "I will be discriminated against because of my race, ethnicity, religion, or sexual orientation. "
         }
        ],
        choicesOrder: "desc"
       }
      ]
     }
    ],
    sendResultOnPageNext: true,
    showPageNumbers: true,
    showQuestionNumbers: "off",
    showProgressBar: "bottom"
   }
   
    window.survey = new Survey.Model(fybarriersJSON);

    survey.onComplete.add(function (sender, options) {
        //Show message about "Saving..." the results
        options.showDataSaving();//you may pass a text parameter to show your own text
        var data = { surveyResult: JSON.stringify(sender.data) };
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{{ url_for('api.add_barriers', username=current_user.username) }}");
        xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
        xhr.onload = xhr.onerror = function () {
            if (xhr.status == 200) {
                options.showDataSavingSuccess(); //you may pass a text parameter to show your own text
                //Or you may clear all messages
                //options.showDataSavingClear();
            } else {
                //Error
                options.showDataSavingError(); //you may pass a text parameter to show your own text
            }
        };
        var dataStringify = JSON.stringify(data);
        xhr.send(dataStringify);
    });

    survey
        .onComplete
        .add(function (sender, result) {
            document
                .querySelector('#surveyResult')
                .innerHTML = "result: " + JSON.stringify(result.data);
        var barriers_data = result.data;
        });

    $("#surveyElement").Survey({model: survey, onValueChanged: surveyValueChanged});

