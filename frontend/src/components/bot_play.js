import React, { Component, Fragment } from "react";
import getApi from '../helpers/api-helpers';

class BotPlay extends Component {
    constructor(props) {
        super(props);
        this.state = {
            questions: [],
            loaded: false,
            placeholder: "Loading",
            currentQuestion: 1
        }
        this.responses = [

        ]
    }
    componentDidMount() {
        getApi().then(response => {
            const questions = response && response.questions;
            this.setState(() => {
                return {
                    questions,
                    loaded: true
                };
            });
        })
        fetch("api/animals/data")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return { placeholder: "Something went wrong!" };
                    });
                }
                console.log('**resp', response);
                return response.json();
            })
            .then(response => {
                console.log('**questions', response)
                const questions = response && response.questions;
                this.setState(() => {
                    return {
                        questions,
                        loaded: true
                    };
                });
            });
    }

    getCurrentQuestion() {
        return this.state.questions.find(data => data.idx == this.state.currentQuestion);
    }

    async onAnswerSubmit(idx, ans) {
        this.responses = [
        ...this.responses,
        {
            idx: idx,
            ans: ans === 'yes' ? 1 : 0
        }]
        this.setState({
            ...this.state,
            currentQuestion: currentQuestion + 1
        })

    }

    render() {
        console.log('**in render', this.state.questions.length)
        return (
            <Fragment>
                <div> afjkdjfdljkf </div>
                {
                this.state.questions.length > 0 ?
                        (
                            <div>
                                <div> {this.getCurrentQuestion().text} </div>
                                <div>
                                    <button> Yes </button>
                                    <button> No </button>
                                </div>

                            </div>
                        )
                    :
                    <div> {this.state && this.state.placeholder} </div>
                }

            </Fragment>
        )
    }
}

export default BotPlay;
