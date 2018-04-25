/*
 *  Copyright (c) 2015 The WebRTC project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree.
 */

'use strict';

// Put variables in global scope to make them available to the browser console.

var video = document.querySelector('video');
var canvas = window.canvas = document.querySelector('canvas');
canvas.width = 480;
canvas.height = 360;

var button = document.querySelector('button');
button.onclick = function() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').
    drawImage(video, 0, 0, canvas.width, canvas.height);
};

var constraints = {
    audio: false,
    video: true
};

function handleSuccess(stream) {
    window.stream = stream; // make stream available to browser console
    video.srcObject = stream;
}

function handleError(error) {
    console.log('navigator.getUserMedia error: ', error);
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// for 403 error
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function uploadPhoto()
{
    // Generate the image data
    var Pic = document.getElementById("myCanvas").toDataURL("image/png");
    Pic = Pic.replace(/^data:image\/(png|jpg);base64,/, "");
    var photo = {
        img: Pic
    }
    //var csrftoken = getCookie('csrftoken');
    // Sending the image data to Server
    $.ajaxSetup({
        data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
    });
    $.ajax({
        url: "/uploadPhoto/",
        type: 'POST',
        data: photo,
        async: true,
        cache: false,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (response) {
            $('.upload-progress').hide();
            if (response.status == 200) {
                   alert("ajax received success !");
                }
        },
        error: function(response) {
            console.log("error", response);
            // $('.upload-progress').hide();
        }
    });
    return false;
}

navigator.mediaDevices.getUserMedia(constraints).
then(handleSuccess).catch(handleError);

