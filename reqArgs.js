const required = (paramName) => {
    throw new Error(
        `${paramName} is a required parameter`
    );
}

const myFoo = (argument = required('argument')) => {
    return console.log(`${argument} is the parameter`)
};

const x = 3;
myFoo();

