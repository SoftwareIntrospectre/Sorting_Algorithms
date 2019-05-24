//version 1
let arrayToBubbleSortV1 =  [1, 4, 7, 5, 9, 2, 3, 4, 6, 8];

const bubbleSortV1 = (arr) => {

    let sorted = false

    while(!sorted) {
      sorted = true
      for(var i=0; i < arr.length; i++) {
        if(arr[i] < arr[i-1]) {
          let temp = arr[i];
          arr[i] = arr[i-1];
          arr[i-1] = temp;
          sorted = false;
        }
      }
    }

    return arr;
}

bubbleSortV1(arrayToBubbleSortV1);


//version 2
let arrayToBubbleSortV2 = [11, 42, 79, 51, 96, 24, 37, 43, 62, 88];

const swapElementsV2 = (array, i, j) =>{
    //stores first element into the "temp" variable
    let temp = array[i];

    //moves the value of i into j's position
    array[i] = array[j];

    //stores the value of j into temp
    array[j] = temp;
}

const bubbleSortV2 = (arr) => 
{

    for (let i = 0; i < arr.length; i++){
        for(let j = 1; j < arr.length; j++){
            if(arr[j-1] > arr[j]){
                swapElementsV2(arr, j - 1, j);
            }
        }
    }

    return arr;
}

bubbleSortV2(arrayToBubbleSortV2);