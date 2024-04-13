(function(){
    if(!window.config) {
    config_js = document.body.appendChild(document.
    createElement('script'));
    config_js.src = '//127.0.0.1:8000/static/js/config.js?r='+Math.
    floor(Math.random()*9999999999999999);
    window.config = true;
    }
    else {
    configLaunch();
    }
    })();