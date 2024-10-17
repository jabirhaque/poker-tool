import {useGetMessageQuery} from "./api.ts";

export default function App() {
  const { data, error, isLoading } = useGetMessageQuery()

  if (isLoading){
    return(
        <h1>Loading...</h1>
    )
  }
  if (error){
    return(
        <h1>ERROR</h1>
    )
  }
  return <h1>{data.message}</h1>
}