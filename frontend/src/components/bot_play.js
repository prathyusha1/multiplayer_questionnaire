import React, { Component, Fragment } from "react";
import { getApi, postApi } from '../helpers/api-helpers';

class BotPlay extends Component {
    constructor(props) {
        super(props);
        this.state = {
            questions: [],
            loaded: false,
            placeholder: "Loading",
            currentQuestion: 1,
            playAgainDisplay: false,
            askGuessResponse: false,
            score: 0
        }
        this.responses = [

        ]
    }

    loadQuestions() {
        getApi("api/animals/data").then(response => {
            const questions = response && response.questions;
            this.setState({
                ...this.state,
                questions,
                loaded: true,
                playAgainDisplay: false
            });
        });
    }
    componentDidMount() {
        var gameScore = window.top.localStorage.getItem('game-score');
        if (gameScore && !isNaN(gameScore)) {
            this.setState({
                ...this.state,
                score: +gameScore
            })
        }
        this.loadQuestions()
    }

    componentWillUnmount() {
        window.top.localStorage.setItem('game-score', this.state.score);
    }

    getCurrentQuestion() {
        return this.state.questions.find(data => data.idx == this.state.currentQuestion);
    }

    onGuessResponse(ans) {
        this.setState({
            ...this.state,
            score: (ans == 'yes') ? this.state.score - 1 : this.state.score + 1
        })
    }

    onAnswerSubmit(idx, ans) {
        this.responses = [
            ...(this.responses.filter(function (val) { return (val.idx != idx) })),
            {
                idx: idx,
                ans: ans === 'yes' ? 1 : 0
            }]
        postApi('api/animals/validate', {
            "responses": this.responses
        }).then(output => {
            var shouldIncrement = this.state.currentQuestion < this.state.questions.length
            if (shouldIncrement) {
                this.setState({
                    ...this.state,
                    currentQuestion: this.state.currentQuestion + 1
                })
            } else {
                var output_text = 'Sorry, we are unable to identify your guess !!';
                var identifiersLength = output && output.identifier && output.identifier.length;
                var shouldIncreasePoints = true;
                if (identifiersLength == 1) {
                    output_text = 'I think your animal is ' + output.identifier[0];
                    shouldIncreasePoints = false;
                    this.setState({
                        ...this.state,
                        askGuessResponse: true
                    });
                } else if (identifiersLength > 1 && identifiersLength <= 5) {
                    output_text = `Sorry, I am unable to make a perfect guess with the information I have.
                        I think your animal is one amongst -> `;
                    for (var animal of output.identifier) {
                        output_text += animal + ','
                    }
                }
                this.setState({
                    ...this.state,
                    questions: [],
                    placeholder: output_text,
                    playAgainDisplay: true,
                    score: shouldIncreasePoints ? this.state.score + 1 : this.state.score
                })
                window.top.localStorage.setItem('game-score', this.state.score);
            }
        })
    }

    render() {
        return (
            <Fragment>
                <div className="score-card">
                    <span className="score-text"> Score: {this.state.score} </span> </div>
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
                    {
                        this.state.askGuessResponse && <div>
                            <div className="buttons">
                                <button className="yes-btn" onClick={() => this.onGuessResponse("yes")}> Yes </button>
                                <button className="no-btn" onClick={() => this.onGuessResponse("no")}> No </button>
                            </div>
                        </div>

                    }
                    {
                        this.state.displayPlayAgain ? (
                            <button className="yes-btn" onClick={() => this.loadQuestions()}> Play Again </button>
                        ) : (<div> </div>)
                    }

                </div>
            </Fragment>
        )
    }
}

export default BotPlay;
