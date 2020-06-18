import React, { Component, Fragment } from "react";
import { getApi, postApi } from '../helpers/api-helpers';

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
        getApi("api/animals/data").then(response => {
            const questions = response && response.questions;
            this.setState(() => {
                return {
                    questions,
                    loaded: true,
                };
            });
        });
    }

    getCurrentQuestion() {
        return this.state.questions.find(data => data.idx == this.state.currentQuestion);
    }

    onAnswerSubmit(idx, ans) {
        this.responses = [
        ...(this.responses.filter(function(val) {return (val.idx != idx)})),
        {
            idx: idx,
            ans: ans === 'yes' ? 1 : 0
        }]
        postApi('api/animals/validate', {
            "responses": this.responses
        }).then(output => {
            console.log('**output', output);
            if (output && output.identifier) {
                this.setState({
                    ...this.state,
                    questions: [],
                    placeholder: output.identifier
                })
            } else {
                if (this.state.currentQuestion < this.state.questions.length) {
                    this.setState({
                        ...this.state,
                        currentQuestion: this.state.currentQuestion + 1
                    })        
                } else {
                    this.setState({
                        ...this.state,
                        questions: [],
                        placeholder: 'Sorry, we are unable to identify your guess'
                    })
                }
            }
        })
    }

    render() {
        console.log('**in render', this.state.questions.length)
        return (
            <div className="question">
                {
                this.state.questions.length > 0 ?
                        (
                            <div>
                                <div> {this.getCurrentQuestion().text} </div>
                                <div className="buttons">
                                    <button className="yes-btn" onClick={() => this.onAnswerSubmit(this.state.currentQuestion, "yes")}> Yes </button>
                                    <button className="no-btn" onClick={() => this.onAnswerSubmit(this.state.currentQuestion, "no")}> No </button>
                                </div>

                            </div>
                        )
                    :
                    <div> {this.state && this.state.placeholder} </div>
                }

            </div>
        )
    }
}

export default BotPlay;
