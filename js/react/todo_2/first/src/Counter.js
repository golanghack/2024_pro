import React, { Component } from "react";

class CounterClass extends Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0,
        };
    }

    increment = () => {
        this.setState((prevState) => ({
            count: prevState.count + 1,
        }));
    };

    decrement = () => {
        this.setState((prevState) => ({
            count: prevState.count - 1,
        }));
    };

    render() {
        return (
            <div>
                <h2>Count: {this.state.count}</h2>
                <button onClick={this.increment}>Increment</button>
                <button onClick={this.decrement}>Decrement</button>
            </div>
        );
    }
}

export default CounterClass;