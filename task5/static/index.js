import * as axios from './axios.min.js'
import * as jQuery from './jquery.min.js';

export default function search(text) {
    axios.post(`localhost:5000/search`, text)
        .then(response => {
            const data = response.data;
            data.forEach(result => {
                jQuery("#myULy").append('<li><a href="' + result + '">' + result + '</a></li>');
            })
        })
        .catch(err => console.warn(err));
}