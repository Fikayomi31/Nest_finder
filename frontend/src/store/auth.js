import {create} from 'zustand';
import {mountStoreDevtool} from 'simple-zustand-devtools';

const useAuthStore = create((set, get) => ({
    allUserDate: null,
    loading: false,

    use: () => ({
        user_id: get().allUserDate?.user_id || null,
        username: get().allUserDate?.username || null,
    }),

    setUser: (user) => ({
        allUserDate: user
    }),
    setLoading: (loading) => set({ loading }),
    isLoggedIn: () => get.allUserDate != null,
}));

if (import.meta.env.Dev) {
    mountStoreDevtool("store", useAuthStore);
}


export { useAuthStore }
