window.onload = function(){

  var $tableElements = document.getElementsByTagName('td');
  //順番を制御するための変数
  let order = true; //trueは黒（先行）
  let othelloWhte = '◯';
  let othelloBlack = '●';
  let othelloColor = othelloBlack;

  //tableの全てにclickイベントを付与する
  for (let $i=0; $i < $tableElements.length; $i++) {
    $tableElements[$i].addEventListener('click', function(){
      //配列に変換する
      let tableElements = [].slice.call($tableElements);
      //クリックした位置の取得
      let index = tableElements.indexOf(this);
      putOthello(index);
      changeOrder();
    });
  }

  function putOthello(index) {
    $tableElements[index].innerHTML = othelloColor;
  }
  //順番の判別する
    function changeOrder() {
        if (order) {
            othelloColor = othelloWhte;
            order = false;
        } else {
            othelloColor = othelloBlack;
            order = true;
        }
    }
}

changeOthello = (index) => {
    //両隣とその隣のオセロの色（値）を取得
    let prevLeftOthello = $tableElements[index - 2].innerHTML;
    let prevOthello = $tableElements[index - 1].innerHTML;
    let nextRightOthello = $tableElements[index + 2].innerHTML;
    let nextOthello = $tableElements[index + 1].innerHTML;

    //黒
    //左隣の次のマスの色が置いたオセロと同じ色の場合隣のオセロの色を変える
    if (prevLeftOthello.match(othelloBlack) && prevOthello.match(othelloWhte)) {
        let targetIndex = index - 1;
        putOthello(targetIndex, index);
    }

    //右隣の次のマスの色が置いたオセロと同じ色の場合隣のオセロの色を変える
    if (nextRightOthello.match(othelloBlack) && nextOthello.match(othelloWhte)) {
        let targetIndex = index + 1;
        putOthello(targetIndex, index);
    }

    //白
    //左隣の次のマスの色が置いたオセロと同じ色の場合隣のオセロの色を変える
    if (prevLeftOthello.match(othelloWhte) && prevOthello.match(othelloBlack)) {
        let targetIndex = index - 1;
        putOthello(targetIndex, index);
    }

    //右隣の次のマスの色が置いたオセロと同じ色の場合隣のオセロの色を変える
    if (nextRightOthello.match(othelloWhte) && nextOthello.match(othelloBlack)) {
        let targetIndex = index + 1;
        putOthello(targetIndex, index);
    }
}