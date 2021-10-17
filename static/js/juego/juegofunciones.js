let getRandomNumber = size => {
    return Math.floor(Math.random()*size);
}

let getDistance = (e,target) => {
    let diffX = e.offsetX - target.x;
    let diffY = e.offsetY - target.y;
    return Math.sqrt((diffX*diffX)+(diffY*diffY));
}

let getDistanceHint = d =>{
    if(d<50){
        return "!A PUNTO DE GANAR!"
    }
    if(d<90){
        return "!ESTAS MUY CERCA!"
    }
    if(d<150){
        return "ESTAS CERCA"
    }
    if(d<250){
        return "ESTAS LEJOS"
    }
    else{
        return "ESTAS MUY LEJOS"
    }
}
