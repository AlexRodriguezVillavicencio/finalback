const WIDTH = 600;
const HEIGH = 400;

let target = {
    x: getRandomNumber(WIDTH),
    y: getRandomNumber(HEIGH)
};
 

console.log(target);
let $map = document.getElementById('map');
let $distance = document.getElementById('distance');
let clicks = 0;

$map.addEventListener('click', function(e){
    clicks++
    let distance = getDistance(e,target);
    let distanceHint = getDistanceHint(distance);
    console.log(distance);
    $distance.innerHTML = `<p>${distanceHint}</p>`;

    if(distance<100){
        Swal.fire({
                title: 'Ganaste!',
                text: 'Una Hamburguesa tradicional',
                footer: 'Vale: 12345asd',
                allowOutsideClick: false,
                imageUrl: 'http://res.cloudinary.com/equilivra/image/upload/v1634351483/rsr3qfq9t05vne30bogs.png',
                imageWidth: '100',
                imageAlt: 'hamburguesa',
                
            });

      
    }
})



