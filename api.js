import axios from "axios";
export const API=axios.create({baseURL:import.meta.env.VITE_API_URL||"http://localhost:5000/api"});
API.interceptors.request.use(c=>{const t=localStorage.getItem("erp_token");if(t)c.headers.Authorization=`Bearer ${t}`;return c});
export const getData=async p=>(await API.get(p)).data;
export const createData=async(p,b)=>(await API.post(p,b)).data;
export const updateData=async(p,id,b)=>(await API.put(`${p}/${id}`,b)).data;
export const deleteData=async(p,id)=>(await API.delete(`${p}/${id}`)).data;
