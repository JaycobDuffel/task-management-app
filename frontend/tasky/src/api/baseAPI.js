import axios from 'axios';

export const apiConfig = {
  baseUrl: process.env.REACT_APP_BASE_URL,
  auth: {
    username: process.env.REACT_APP_API_USERNAME,
    password: process.env.REACT_APP_API_PASSWORD,
  },
};

export const api = axios.create({
  baseURL: apiConfig.baseUrl,
  headers: {
    'Content-type': 'application/json',
  },
});

export default class ApiService {
  createProject(data = {}) {
    console.log(data);
    console.log(apiConfig.baseUrl);
    return api.post(`${apiConfig.baseUrl}/project/`, data);
  }
  
  createStage(data = {}) {
    return api.post(`${apiConfig.baseUrl}/stage/`, data);
  }
  
  createTask(data = {}) {
    return api.post(`${apiConfig.baseUrl}/task/`, data);
  }
}