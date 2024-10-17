import {useGetProbabilityQuery} from "./api.ts";

export default function App() {
  const { data, error, isLoading } = useGetProbabilityQuery()

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
  return(
      <>
        <h3>P(win): {data.win}</h3>
        <h3>P(draw): {data.draw}</h3>
        <h3>P(loss): {data.loss}</h3>
      </>
  )
}