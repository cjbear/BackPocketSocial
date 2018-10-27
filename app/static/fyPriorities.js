

var surveyValueChanged = function (sender, options) {
    var el = document.getElementById(options.name);
    if (el) {
        el.value = options.value;
    }
};

Survey
    .StylesManager
    .applyTheme("default");

    var fyPrioritiesJSON = {
        locale: "en",
        title: "What are your priorities?",
        completedHtml: {
         en: "Nice work. Below are the things that you said were your high priorities for your first year in college. "
        },
        loadingHtml: {
         en: "Identifying your priorities is important."
        },
        pages: [
         {
          name: "page1",
          elements: [
           {
            type: "html",
            name: "FY Priorities Introduction",
            html: {
             en: "<p>For many students, the first year in college can be overwhelming. Besides your class schedule, there are many opportunities that will compete for your time. </p>\n<p>Setting your own priorities—knowing what is most important for you—will help you manage your time and reduce stress and anxiety. </p>\n<p>Below are a list of goals common to many college students. Identify your priority for each goal -- high, medium, or low. If you have priorities that are not listed below, you can add your own on the next page.</p>\n<p>No doubt that your priorities will change over time. That is okay. You can return and update your priorities when needed.</p>"
            }
           },
           {
            type: "dropdown",
            name: "Declare my major by the end of this academic year.",
            title: "Declare my major by the end of this academic year.",
            valueName: "Declare my major by the end of this academic year",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Identify the graduation requirements for the major program that I am considering.",
            title: "Identify the graduation requirements for the major program that I am considering.",
            valueName: "Identify the graduation requirements for the major program that I am considering",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Achieve or maintain my grade point average.",
            title: {
             default: "Maintain a GPA of _____.",
             en: "Achieve or maintain my grade point average."
            },
            valueName: "Achieve or maintain my grade point average",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Increase use of on campus academic support services.",
            title: "Increase use of on campus academic support services.",
            valueName: "Increase use of on campus academic support services",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Research and identify potential career options.",
            title: "Research and identify potential career options.",
            valueName: "Research and identify potential career options",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Try a new sport or activity.",
            title: "Try a new sport or activity.",
            valueName: "Try a new sport or activity",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Improve management of my personal finances.",
            title: "Improve management of my personal finances.",
            valueName: "Improve management of my personal finances",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Increase communication with, and seek advice from, faculty and advisors.",
            title: "Increase communication with, and seek advice from, faculty and advisors.",
            valueName: "Increase communication with, and seek advice from, faculty and advisors",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Improve my living situation.",
            title: "Improve my living situation.",
            valueName: "Improve my living situation",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Make more friends.",
            title: "Make more friends.",
            valueName: "Make more friends",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Participate in a social club.",
            title: "Participate in a social club.",
            valueName: "Participate in a social club",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Improve my physical fitness.",
            title: "Improve my physical fitness.",
            valueName: "Improve my physical fitness",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Manage my stress and anxiety.",
            title: "Manage my stress and anxiety.",
            valueName: "Manage my stress and anxiety",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Do volunteer work.",
            title: "Do volunteer work.",
            valueName: "Do volunteer work",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           },
           {
            type: "dropdown",
            name: "Find and apply for a study abroad program.",
            title: "Find and apply for a study abroad program.",
            valueName: "Find and apply for a study abroad program",
            choices: [
             {
              value: "High Priority",
              text: "High Priority"
             },
             {
              value: "Medium Priority",
              text: "Medium Priority"
             },
             {
              value: "Low Priority",
              text: "Low Priority"
             }
            ]
           }
          ]
         },
         {
          name: "page2",
          elements: [
           {
            type: "multipletext",
            name: "question4",
            title: {
             en: "Are there other priorities that you would like to add? Please list them below."
            },
            items: [
             {
              name: "addFyPriority01",
              title: {
               en: "Add priority"
              }
             },
             {
              name: "addFyPriority02",
              title: {
               en: "Add priority"
              }
             },
             {
              name: "addFyPriority03",
              title: "Add priority"
             },
             {
              name: "addFyPriority04",
              title: "Add priority"
             }
            ]
           },
           {
            type: "comment",
            name: "fyPrioritiesReflection",
            title: {
             en: "In the space below, write a reflection that describes the reasons for your priorities. "
            }
           }
          ]
         }
        ],
        sendResultOnPageNext: true,
        showPageNumbers: true,
        showQuestionNumbers: "off"
       }
       window.survey = new Survey.Model(fyPrioritiesJSON);

survey
    .onComplete
    .add(function (result) {
        var myFyPriorities = result;
        var fyPrioritiesData = result.data;
        document
            .querySelector('#fyPrioritiesResult')
            .innerHTML = "result: " + JSON.stringify(result.data);
    });

$("#fyPrioritiesElement").Survey({model: survey, onValueChanged: surveyValueChanged});