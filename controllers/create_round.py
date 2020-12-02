#! /usr/bin/env python3
# coding: utf-8


from models.round import Round


def create_round(number_turn):
    name = "round " + str(number_turn + 1)
    start = "start"
    end = ""
    return Round(name, start, end)
