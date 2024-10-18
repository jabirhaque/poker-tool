import { Chart } from "react-google-charts";

interface Props{
    win: number,
    draw: number,
    loss: number
}
export default function Probability(props: Props) {
    const {win, draw, loss} = props;
    const data = [
        ["Event", "Probability"],
        ["P(Win)", win],
        ["P(Draw)", draw],
        ["P(Loss)", loss]
    ];
    const options = {
        title: "Probability of event",
        pieHole: 0.4,
        is3D: false
    };
    return (
        <Chart
            chartType="PieChart"
            width="100%"
            height="400px"
            data={data}
            options={options}
        />
    );
}