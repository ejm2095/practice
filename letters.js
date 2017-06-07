const word = 'mississippi';
const letters = word.split('').reduce( (prev, curr) => {
    prev[curr] = prev[curr] ? prev[curr] + 1 : 1;
    return prev;
  }, {});
let max = {letter:undefined, count:0};
Object.keys(letters).forEach( l => {
    if(letters[l] > max.count) {
        max = {letter: l, count: letters[l]};
    }else if (letters[l] == max.count) {
        max.letter += '/'+l
    }
})
console.log(max.letter)
