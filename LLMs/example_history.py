match_history = {
    "board" : {
        "blue" : ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi"],
        "red" : ["africa", "antarctica", "asia", "australia", "europe", "north america", "south america", "mexico"],
        "neutral" : ["almond", "apricot", "avocado", "blackberry", "blueberry", "coconut", "cranberry"],
        "bomb": ["canada"]
    },
    "starting_team" : "red",
    "history" : [
        {
            "team" : "red",
            "spymaster_clue" : "fruit",
            "number" : 2,
            "guesser_turns" : [
                {
                    "actions" : [
                        {
                            "teammember" : "red1",
                            "tool_call" : "codenames_discuss_tool",
                            "tool_args" : "",
                            "tool_return" : ""
                        },
                        {
                            "teammember" : "red2",
                            "tool_call" : "codenames_discuss_tool",
                            "tool_args" : "",
                            "tool_return" : ""
                        },
                        {
                            "teammember" : "red1",
                            "tool_call" : "codenames_guess_tool",
                            "tool_args" : "apple",
                            "tool_return" : "RED"
                        }
                    ],
                    "decision" : "guess",
                    "outcome" : "correct"
                },
                {
                    "actions" : [
                        {
                            "teammember" : "red1",
                            "tool_call" : "codenames_discuss_tool",
                            "tool_args" : "",
                            "tool_return" : ""
                        },
                        {
                            "teammember" : "red2",
                            "tool_call" : "codenames_end_turn_tool",
                            "tool_args" : "",
                            "tool_return" : ""
                        }
                    ],
                    "decision" : "end turn",
                    "outcome" : ""
                }
            ]
        },
        {
            "team" : "blue",
            "clue" : "location",
            "number" : 2,
            "turns" : [
                {
                    "actions" : [
                        {
                            "teammember" : "blue1",
                            "tool_call" : "codenames_guess_tool",
                            "tool_args" : "canada",
                            "tool_return" : "BLACK"
                        }
                    ],
                    "decision" : "guess",
                    "outcome" : "wrong - bomb"
                }
            ]
        }
    ],
    "winner" : "red",
}