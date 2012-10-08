$(document).ready(function() {
    var uploader = new qq.FileUploader({
        // pass the dom node (ex. $(selector)[0] for jQuery users)
        element: document.getElementById('file-uploader'),
        // path to server-side upload script
        action: FU_uploadURL,
        sizeLimit: 15000000,
        minSizeLimit: 0,
        allowedExtensions: ['xls','jpg', 'jpeg', 'pdf', 'txt','doc','htm','html','xml','xmls', 'txt','ppt','png', 'gif', 'swf'],
        // set to true to output server response to console
        debug: true,

        // events
        // you can return false to abort submit
        onSubmit: function(id, fileName){},
        onProgress: function(id, fileName, loaded, total){},
        onComplete: function(id, fileName, responseJSON){},
        onCancel: function(id, fileName){},

        messages: {
            // error messages, see qq.FileUploaderBasic for content
            typeError: FU_msgTypeError,
            sizeError: FU_msgSizeError,
            minSizeError: FU_msgMinSizeError,
            emptyError: FU_msgEmptyError,
            onLeave: FU_msgOnLeave
        },
        showMessage: function(message){ alert(message); }
    });
});
