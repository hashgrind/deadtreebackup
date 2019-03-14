# deadtreebackup

Split a file into sequential QR codes of base64-encoded chunks for printing and storage on paper, because why not?

You can't (shouldn't?) store a ton of information this way. On the other hand, everyone knows how to base64 decode data, QR codes are ubiquitously readable and somewhat damage resistant, and paper can survive a lot of things.

Basic backup pattern: Apply to super-important-file, print out the pieces, bind into sequential order, and store somewhere physically safe.

Basic restore pattern: Scan/photograph pieces, base64 decode each, and sequentially recombine.

Even more basic restore pattern: Scan/photograph pieces, and then point the companion restore script at them.