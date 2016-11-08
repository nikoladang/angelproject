(function($, win){
  "use strict";

  var Split = $.split = (function(){

    function init(){
      countTxt();
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

    return {
      init: init
    };

    })();

  $(Split.init);
  
})(jQuery, window);