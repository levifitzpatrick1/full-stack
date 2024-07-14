import axios from "axios";
import type { UserData } from "./apiTypes";

// TODO: this also needs to be figured out 
export const apiPath = 'http://localhost:5000'

const apiClient = axios.create({
    baseURL: apiPath,
    headers: {
        'Content-Type': 'application/json'
    }
});

export const checkUsernameAvailability = async (username: string): Promise<boolean> => {
    const response = await apiClient.get('/check-username', { params: { username } });
    return !response.data.exists;
};

export const confirmUsername = async (username: string, uid: string): Promise<void> => {
    await apiClient.post('/confirm-username', { username, uid });
};

export const uploadPhoto = async (file: File, uid: string): Promise<string> => {
    const formData = new FormData();
    formData.append('photo', file);
    formData.append('uid', uid)
    const response = await apiClient.post('/upload-photo', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data.photo;
};

export const getUserData = async (uid: string): Promise<UserData> => {
    const response = await apiClient.get(`/user`, { params: { uid: uid } });
    return response.data.user;
};