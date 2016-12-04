(function($, win){
  "use strict";

  var Split = $.split = (function(){

    var i = 0,
      $item,
      itemLen = 0,
      rows = 2,
      setItemColumn;


    function init(){
      countTxt();
      setHeight();
    }

    function countTxt() {
      // add 3 dots text on two line
      var answers = $('.article_txt');
      var isFirefox = typeof InstallTrigger !== 'undefined';
      var initialTexts = [];
      for (var i = 0, len = answers.length; i < len; i++) {
        initialTexts.push(answers.eq(i).text());
      }
      $(window).on('load resize', function() {
        answers.each(function(index, el) {
          truncate(el, initialTexts[index], { line: 3 });
          if( $(window).width() < 767 && isFirefox ) {
            truncate(el, initialTexts[index], { line: 3 });
          } else {
            truncate(el, initialTexts[index], { line: 3 });
          }
        });
      });

    }

    // set height colum
    function setHeight() {
      var $itemList = $('#wrapper');
      $(window).on("load resize", function(){
        $itemList.each(function() {
          $item = $(this).find('.col-lg-4');
          itemLen = $item.length;
          $item.css("height","auto");
          for( var i = -1, len = Math.ceil( itemLen / rows); ++ i < len; ){
            var itemArray = [];
            for(var j = -1; ++ j < rows;){
              itemArray.push( i * rows + j );
            }
            setItemColumn(itemArray);
          }
        });
      });
    }
    setItemColumn = function(itemNum){
      var itemMaxHeight = 0;
      for( var i = 0; i < itemNum.length; i++){
        itemMaxHeight = $item.eq(itemNum[i]).height() > itemMaxHeight ? $item.eq(itemNum[i]).height() : itemMaxHeight;
      }
      for(i = 0; i < itemNum.length; i++){
        $item.eq(itemNum[i]).height(itemMaxHeight);
      }
    };

    return {
      init: init
    };

    })();

  $(Split.init);
  
})(jQuery, window);