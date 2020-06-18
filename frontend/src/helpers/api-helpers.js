import axios from 'axios';

export async function getApi(url) {
    try {
        const response = await axios.get(url);
        console.log(response);
        return response;
    } catch (error) {
        console.error(error);
    }
}