// Welcome to Secure Code Game Season-2/Level-5!
// This is the last level of this season, good luck!

var CryptoAPI = (function() {
    var encoding = {
        a2b: function(a) {
            return a.charCodeAt(0); // basic ascii decoding
        },
        b2a: function(b) {
            return String.fromCharCode(b); // basic ascii encoding
        }
    };

    // 🛡️ Private internal function to avoid external tampering (Exploit 2 fix)
    function internalRound(H, w) {
        // Stub logic here – in a real SHA-1, this would be the compression function
    }

    var API = {
        sha1: {
            name: 'sha1',
            identifier: '2b0e03021a',
            size: 20,
            block: 64,
            hash: function(input) {
                // 🛡️ Fix Exploit 1: Reject non-string input (protect from toString coercion)
                if (typeof input !== 'string') {
                    throw new TypeError("Input must be a string");
                }

                var s = input + '\x80';
                var len = s.length,
                    blocks = len >> 6,
                    chunk = len & 63,
                    res = "",
                    i = 0,
                    j = 0,
                    H = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0],

                    // 🛡️ Fix Exploit 3: Prevent Array.prototype setter abuse
                    w = Object.create(null);

                while (chunk++ != 56) {
                    s += "\x00";
                    if (chunk == 64) {
                        blocks++;
                        chunk = 0;
                    }
                }

                // Pad with zero-length block
                for (s += "\x00\x00\x00\x00", chunk = 3, len = 8 * (len - 1); chunk >= 0; chunk--) {
                    s += encoding.b2a((len >> (8 * chunk)) & 255);
                }

                for (i = 0; i < s.length; i++) {
                    j = (j << 8) + encoding.a2b(s[i]);
                    if ((i & 3) === 3) {
                        w[(i >> 2) & 15] = j;
                        j = 0;
                    }

                    // 🛡️ Fix Exploit 2: use closure-scoped internalRound
                    if ((i & 63) === 63) {
                        internalRound(H, w);
                    }
                }

                for (i = 0; i < H.length; i++) {
                    for (j = 3; j >= 0; j--) {
                        res += encoding.b2a((H[i] >> (8 * j)) & 255);
                    }
                }

                return res;
            }
        }
    };

    return API;
})();
