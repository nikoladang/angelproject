(function webpackUniversalModuleDefinition(root, factory) {
  if(typeof exports === 'object' && typeof module === 'object')
    module.exports = factory();
  else if(typeof define === 'function' && define.amd)
    define([], factory);
  else {
    var a = factory();
    for(var i in a) (typeof exports === 'object' ? exports : root)[i] = a[i];
  }
})(this, function() {
return /******/ (function(modules) { // webpackBootstrap
/******/  // The module cache
/******/  var installedModules = {};

/******/  // The require function
/******/  function __webpack_require__(moduleId) {

/******/    // Check if module is in cache
/******/    if(installedModules[moduleId])
/******/      return installedModules[moduleId].exports;

/******/    // Create a new module (and put it into the cache)
/******/    var module = installedModules[moduleId] = {
/******/      exports: {},
/******/      id: moduleId,
/******/      loaded: false
/******/    };

/******/    // Execute the module function
/******/    modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/    // Flag the module as loaded
/******/    module.loaded = true;

/******/    // Return the exports of the module
/******/    return module.exports;
/******/  }


/******/  // expose the modules object (__webpack_modules__)
/******/  __webpack_require__.m = modules;

/******/  // expose the module cache
/******/  __webpack_require__.c = installedModules;

/******/  // __webpack_public_path__
/******/  __webpack_require__.p = "";

/******/  // Load entry module and return exports
/******/  return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  var _truncator = __webpack_require__(1);

  Object.keys(_truncator).forEach(function (key) {
    if (key === "default") return;
    Object.defineProperty(exports, key, {
      enumerable: true,
      get: function get() {
        return _truncator[key];
      }
    });
  });

/***/ },
/* 1 */
/***/ function(module, exports, __webpack_require__) {

  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol ? "symbol" : typeof obj; };

  exports.truncate = truncate;

  var _object = __webpack_require__(2);

  var _dom = __webpack_require__(3);

  var _dom2 = _interopRequireDefault(_dom);

  function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

  var DEFAULT_OPTIONS = {
    ellipsis: '...'
  };

  function truncate(el, text, options) {
    if (options === null || (typeof options === 'undefined' ? 'undefined' : _typeof(options)) !== 'object') {
      throw new Error('options must be an object');
    }

    execWithUnfixHeight(el, function () {
      var domEl = (0, _dom2.default)(el);
      var opts = normalizeOptions(options);

      if (typeof opts.height === 'number') {
        return truncateByHeight(domEl, text, opts.height, opts);
      }

      if (typeof opts.line === 'number') {
        return truncateByLine(domEl, text, Math.floor(opts.line), opts);
      }

      if (typeof opts.count === 'number') {
        return truncateByCount(domEl, text, Math.floor(opts.count), opts);
      }

      throw new Error('options must have height, line or count as number');
    });
  }

  function normalizeOptions(options) {
    var opts = (0, _object.extend)({}, DEFAULT_OPTIONS, options);

    if (opts.ellipsis === null) opts.ellipsis = '';

    return opts;
  }

  // set the element height to auto
  // and unlock constraints of min-, max-height during given function is executed
  function execWithUnfixHeight(el, fn) {
    var _el$style = el.style;
    var height = _el$style.height;
    var maxHeight = _el$style.maxHeight;
    var minHeight = _el$style.minHeight;


    try {
      el.style.height = 'auto';
      el.style.maxHeight = 'none';
      el.style.minHeight = '0';

      fn();
    } finally {
      // ensure the styles are restored
      el.style.height = height;
      el.style.maxHeight = maxHeight;
      el.style.minHeight = minHeight;
    }
  }

  function truncateByLine(el, text, line, options) {
    truncateByHeight(el, text, el.lineHeight * line, options);
  }

  function truncateByHeight(el, text, height, options) {
    el.text = text;

    if (el.height <= height) {
      return;
    }

    truncateImpl(el, text, height, options, 0, text.length);
  }

  function truncateByCount(el, text, count, options) {
    if (text.length <= count) {
      el.text = text;
      return;
    }

    el.text = text.substring(0, count) + options.ellipsis;
  }

  function truncateImpl(el, text, maxHeight, options, left, right) {
    var center = Math.floor((left + right) / 2);
    var truncated = text.substring(0, center) + options.ellipsis;
    el.text = truncated;

    if (left >= right - 1) {
      return;
    }

    var height = el.height;

    if (height > maxHeight) {
      truncateImpl(el, text, maxHeight, options, left, center);
    } else {
      // left index should always be included in search space
      // because it might be boundary point of truncation
      truncateImpl(el, text, maxHeight, options, center, right);
    }
  }

/***/ },
/* 2 */
/***/ function(module, exports) {

  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.extend = extend;
  function extend(target) {
    for (var _len = arguments.length, objs = Array(_len > 1 ? _len - 1 : 0), _key = 1; _key < _len; _key++) {
      objs[_key - 1] = arguments[_key];
    }

    objs.forEach(function (obj) {
      Object.keys(obj).forEach(function (key) {
        if (obj[key] !== undefined) target[key] = obj[key];
      });
    });
    return target;
  }

/***/ },
/* 3 */
/***/ function(module, exports) {

  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

  exports.default = dom;

  function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

  var Dom = function () {
    function Dom(el) {
      _classCallCheck(this, Dom);

      this.el = el;
      this.style = window.getComputedStyle(el, '');
    }

    _createClass(Dom, [{
      key: 'text',
      set: function set(val) {
        if ('textContent' in this.el) {
          this.el.textContent = val;
        } else if ('innerText' in this.el) {
          this.el.innerText = val;
        } else {
          throw new Error('The browser does not support text insertion for DOM');
        }
      }
    }, {
      key: 'height',
      get: function get() {
        return parseFloat(this.style.getPropertyValue('height')) || 0;
      }
    }, {
      key: 'lineHeight',
      get: function get() {
        var origHTML = this.el.innerHTML;

        this.el.innerHTML = 'X';
        var height = this.height;
        this.el.innerHTML = origHTML;

        return height;
      }
    }]);

    return Dom;
  }();

  function dom(el) {
    return new Dom(el);
  }

/***/ }
/******/ ])
});
;