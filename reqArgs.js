const required = (paramName) => {
    throw: new Error(
        `${paramName} is a required parameter`
    );
}

const myFoo = (argument = required('argument')) => {
    //code and processes
}

myFoo();

