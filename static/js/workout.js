const exercise_template_id = document.getElementById('exercise-template');
const set_template_id = document.getElementById('set-template-id');
const add_exercise_btn = document.getElementById('add-exercise');
const add_sets_btn = document.getElementById('add-sets');
const exercise_count = document.querySelector('input[name="exercise-count"]');
const added_btn_div = document.getElementById("added-btn-div");
var btn2_sets;
exercise_count.value = "1";

// exercise_template
var exercise_template = _.template(exercise_template_id.innerHTML);

var set_template = _.template(set_template_id.innerHTML);

var exercise_num;
add_exercise_btn.addEventListener('click', function(){
    exercise_num = Number(exercise_count.value) + 1;
    exercise_count.value = String(exercise_num);

    exercise_compiled = exercise_template({exercise_num: exercise_num});
    var set_compiled = set_template({exercise_num: exercise_num});

    added_btn_div.insertAdjacentHTML('beforebegin', exercise_compiled);
    document.getElementById("exercise-set" + exercise_num).innerHTML += set_compiled;

    btn2_sets = document.getElementById("btn2-sets"+exercise_num);
    btn2_sets.style.display = "none";
    btn2_sets_innerHtml = btn2_sets.querySelector('#add-sets');
    btn2_sets_innerHtml.attributes.exerciseno.value = exercise_num-1;

    document.getElementById('select-label'+exercise_num).insertAdjacentElement('beforebegin', btn2_sets_innerHtml);
    added_btn_div.querySelector("#add-sets").attributes.exerciseno.value = exercise_num;
});


const addSets =  function(ele){
    exercise_num = Number(ele.attributes.exerciseno.value);
    var set_compiled = set_template({exercise_num: exercise_num});
    document.getElementById("exercise-set" + exercise_num).innerHTML += set_compiled;
};




