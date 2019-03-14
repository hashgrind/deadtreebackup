# deadtreebackup

Split a file into sequential QR codes of base64-encoded chunks for printing and storage on paper, because why not?

You can't store a ton of information this way easily. On the other hand, everyone knows how to base64 decode data, QR codes are ubiquitously readable and somewhat damage resistant, and paper can survive a lot of things.

Basic pattern: Apply to super-important-file, print out the pieces, bind into sequential order, and store somewhere physically safe. When needed: Scan pieces, base64 decode each, and sequentially recombine.