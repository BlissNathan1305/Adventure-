function spellName(name) {
    console.log(`Spelling "${name}":`);
    for (let i = 0; i < name.length; i++) {
        console.log(`${i + 1}. ${name[i]}`);
    }
}

let name = "Samuel Nathaniel";
spellName(name);
