var Individuals = {
  p1: {
    first_name: "Eugene",
    M: "H",
    last_name: "Smith",
    checks: {
      check1: 745,
      check2: 56890,
      check3: 34,
      check4: 0.7,
    },
  },
};

// var checktotal = (them) => {

// }

console.log(Individuals.p1["first_name"] + " " + Individuals.p1["last_name"]);

console.log("How much is Eugene owed ?");

console.log(Individuals.p1.checks["check1" + "check2" + "check3" + "check4"]);
