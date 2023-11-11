var CryptoJs = require("crypto-js");

var s, u = (s = null,
        function () {
            return s || (s = function () {
                var e, t, n, r, i = null;
                return i || (t = new RegExp("\\u200c", "g"),
                    n = new RegExp("\\u200d", "g"),
                    r = new RegExp(".{8}", "g"),
                    e = "‍‌‍‍‍‌‌‌‍‍‌‍‍‌‍‍‍‍‌‍‍‌‍‍‍‌‍‌‍‍‍‌‍‌‌‍‍‍‍‌‍‌‌‌‍‌‌‌‍‌‌‍‍‍‌‌‍‌‌‍‌‍‌‌‍‌‍‍‍‌‌‌‍‌‌‍‍‌‌‍‍‌‌‍‍‍‍‌‍‌‍‍‌‌‍‍‍‌‍‍‍‍‌‍‍‍‌‌‌‍‍‌‍‍‌‌‍‌‌‌‍‌‌‌‍‍‌‍".replace(r, (function (e) {
                            return String.fromCharCode(parseInt(e.replace(t, 1).replace(n, 0), 2))
                        }
                    )),
                    i = {
                        key: CryptoJs.enc.Utf8.parse(e),
                        mode: CryptoJs.mode.CBC,
                        pad: CryptoJs.pad.Pkcs7
                    }),
                    i
            }()),
                s
        }
)


l = function (e, t) {
    void 0 === e && (e = ""),
    void 0 === t && (t = "");
    var n = u()
        , r = CryptoJs.AES.encrypt(e.toString(), n.key, {
        iv: CryptoJs.enc.Utf8.parse(t),
        mode: n.mode,
        padding: n.pad
    });
    return r = r.toString()
}
c = function (e, t) {
    void 0 === e && (e = ""),
    void 0 === t && (t = "");
    var n = u()
        , r = CryptoJs.AES.decrypt(e.toString(), n.key, {
        iv: CryptoJs.enc.Utf8.parse(t),
        mode: n.mode,
        padding: n.pad
    });
    return r = r.toString(CryptoJs.enc.Utf8)
}


m = function (e, t) {
    var n = "";
    return "string" == typeof e && e.length > 20 && (n = c(e, t.iv)),
        n
}
h = function (e, t) {
    return e ? ("string" != typeof e && (e = e.toString()),
        l(e, t.iv)) : ""
}
// var n = '{"query":"python","cityCode":1,"industryCodes":"","pageNum":1,"limit":15}'


function fn(n, t) {
    return h(n, {iv: t}).replace(/\//g, "_").replace(/\+/g, "-").replace(/=/g, "~")
    console.log(h(n, {iv: t}).replace(/\//g, "_").replace(/\+/g, "-").replace(/=/g, "~"))

}

// var s = 'vNMGPUCiqshZbvDM'
// var data = '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'
// console.log(m((data,{iv: s})))
function fn2(data,iv) {
    return m(data,{iv: iv})
}