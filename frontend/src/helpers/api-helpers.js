import axios from 'axios';

export function getApi(url) {
    return new Promise((resolve, reject) => {
        try {
            axios.get(url).then(response => {
                resolve(response && response.data);
    
            });
        } catch (error) {
            console.error(error);
            reject(error);
        }    
    });
}

export function postApi(url, data) {
    return new Promise((resolve, reject) => {
        try {
            axios.post(url, data).then(response => {
                resolve(response && response.data);
    
            });
        } catch (error) {
            console.error(error);
            reject(error);
        }    
    });
}