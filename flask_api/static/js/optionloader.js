
$('#task').change(function() {

loadsubtasks($(this).val())
    .then(subtasks => $("#subtask")
        .empty()
        .append(subtasks.reduce((acc, cur) => acc + `<option>${cur}</option>`, "")));
});

$('#task').change();
function loadsubtasks(task) {
    return new Promise((resolve, reject) => {
        var subtasks = [];
        for(var k in model[task]) subtasks.push(k);
        resolve(subtasks);
    });
}

function myFunc(vars) {
    return vars
}

