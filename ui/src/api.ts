import {createApi, fetchBaseQuery} from "@reduxjs/toolkit/query/react";

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000' }),
  endpoints: (builder) => ({
    getMessage: builder.query<{ message: string }, void>({
      query: () => ``,
    }),
    getProbability: builder.query<{ win: number, draw: number, loss: number }, void>({
      query: () => `/get_probability_test`,
    }),
  }),
})

export const {
  useGetMessageQuery,
  useGetProbabilityQuery
} = api