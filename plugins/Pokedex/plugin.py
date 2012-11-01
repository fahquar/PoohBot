# encoding: utf8
###
# Copyright (c) 2010, Alex Munroe
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import pokedex.db
import pokedex.db.tables as tables
import pokedex.lookup

import urllib


def get_stat_color(stat):
    if stat < 41:
        return 4  # red
    elif stat < 52:
        return 7  # orange
    elif stat < 61:
        return 8  # yellow
    elif stat < 71:
        return 9  # green
    elif stat < 85:
        return 11  # cyan
    elif stat < 100:
        return 12  # blue
    else:
        return 13  # purple


class Pokedex(callbacks.Plugin):
    """Add the help for "@plugin help Pokedex" here
    This should describe *how* to use this plugin."""
    def __init__(self, irc):
        self.__parent = super(Pokedex, self)
        self.__parent.__init__(irc)
        self.db = pokedex.db.connect(self.registryValue('databaseURL'))
        self.lookup = pokedex.lookup.PokedexLookup(
            directory=conf.supybot.directories.data.dirize('pokedex-index'),
            session=self.db,
        )

    def pokedex(self, irc, msg, args, thing):
        """<thing...>

        Looks up <thing> in the veekun Pokédex."""

        # Fix encoding.  Sigh.
        if not isinstance(thing, unicode):
            ascii_thing = thing
            try:
                thing = ascii_thing.decode('utf8')
            except UnicodeDecodeError:
                thing = ascii_thing.decode('latin1')

        # Similar logic to the site, here.
        results = self.lookup.lookup(thing)

        # Nothing found
        if len(results) == 0:
            self._reply(irc, "I don't know what that is.")
            return

        # Multiple matches; propose them all
        if len(results) > 1:
            if results[0].exact:
                reply = "Are you looking for"
            else:
                reply = "Did you mean"

            # For exact name matches with multiple results, use type prefixes
            # (item:Metronome).  For anything else, omit them
            use_prefixes = (results[0].exact
                            and '*' not in thing
                            and '?' not in thing)

            result_strings = []
            for result in results:
                result_string = result.object.name

                # Prepend, e.g., pokemon: if necessary
                if use_prefixes:
                    # Table classes know their singular names
                    prefix = result.object.__singlename__
                    result_string = prefix + ':' + result_string

                # Identify foreign language names
                if result.language:
                    result_string += u""" ({0}: {1})""".format(
                        result.iso3166, result.name)

                result_strings.append(result_string)

            self._reply(irc, u"{0}: {1}?".format(reply, '; '.join(result_strings)))
            return

        # If we got here, there's an exact match; hurrah!
        result = results[0]
        obj = result.object

        # Deal with Pokémon shenanigans
        if isinstance(obj, tables.PokemonForm):
            obj = obj.pokemon
        elif isinstance(obj, tables.PokemonSpecies):
            obj = obj.default_pokemon

        if isinstance(obj, tables.Pokemon):
            reply_template = \
                u"""#{id} {name}, {type}-type Pokémon.  Has {abilities}.  """ \
                """{stats}.  """ \
                """http://veekun.com/dex/pokemon/{link_name}"""

            if not obj.is_default:
                # Can't use urllib.quote() on the whole thing or it'll
                # catch "?" and "=" where it shouldn't.
                # XXX Also we need to pass urllib.quote() things explicitly
                #     encoded as utf8 or else we get a UnicodeEncodeError.
                link_name = '{name}?form={form}'.format(
                    name=urllib.quote(obj.species.name.lower().encode('utf8')),
                    form=urllib.quote(obj.default_form.form_identifier.lower().encode('utf8')),
                )
            else:
                link_name = urllib.quote(obj.species.name.lower().encode('utf8'))

            # a/b/c/d/e/f sucks.  Put stats in a more readable format.
            # Also, color-code them by good-osity.
            colored_stats = []
            stat_total = 0
            for pokemon_stat in obj.stats:
                base_stat = pokemon_stat.base_stat
                stat_total += base_stat
                color = get_stat_color(base_stat)

                colored_stats.append(
                    "\x03{0:02d}{1}\x0f".format(color, base_stat)
                )

            colored_stat_total = "\x03{0:02d}{1}\x0f".format(
                get_stat_color(stat_total / 6),
                stat_total,
            )
            stats = """{0} HP, {1}/{2} phys, {3}/{4} spec, {5} speed; {total} total""" \
                .format(*colored_stats, total=colored_stat_total)
            self._reply(irc, reply_template.format(
                id=obj.species.id,
                name=obj.name,
                type='/'.join(_.name for _ in obj.types),
                abilities=' or '.join(_.name for _ in obj.abilities),
                stats=stats,
                link_name=link_name,
                )
            )

        elif isinstance(obj, tables.Move):
            reply_template = \
                u"""{name}, {type}-type {damage_class} move.  """ \
                """{power} power; {accuracy}% accuracy; {pp} PP.  """ \
                """{effect}  """ \
                """http://veekun.com/dex/moves/{link_name}"""
            self._reply(irc, reply_template.format(
                name=obj.name,
                type=obj.type.name,
                damage_class=obj.damage_class.name,
                power=obj.power,
                accuracy=obj.accuracy,
                pp=obj.pp,
                effect=unicode(obj.short_effect.as_text()),
                link_name=urllib.quote(obj.name.lower().encode('utf8')),
                )
            )

        elif isinstance(obj, tables.Type):
            reply_template = u"""{name}, a type.  """

            offensive_reply_factors = {
                200: u'\x03092×\x0f',
                50:  u'\x0304½×\x0f',
                0:   u'\x03140×\x0f',
            }

            offensive_modifiers = {}
            for matchup in obj.damage_efficacies:
                if matchup.damage_factor != 100:
                    offensive_modifiers.setdefault(matchup.damage_factor, []) \
                        .append(matchup.target_type.name)
            if offensive_modifiers:
                reply_template += u"""{offensive_modifiers}.  """
                for factor in offensive_modifiers:
                    offensive_modifiers[factor] = u'{factor} against {types}'.format(
                        factor=offensive_reply_factors[factor],
                        types=', '.join(sorted(offensive_modifiers[factor]))
                    )

            defensive_reply_factors = {
                200: u'\x03042×\x0f',
                50:  u'\x0309½×\x0f',
                0:   u'\x03110×\x0f',
            }

            defensive_modifiers = {}
            for matchup in obj.target_efficacies:
                if matchup.damage_factor != 100:
                    defensive_modifiers.setdefault(matchup.damage_factor, []) \
                        .append(matchup.damage_type.name)
            if defensive_modifiers:
                reply_template += u"""{defensive_modifiers}.  """
                for factor in defensive_modifiers:
                    defensive_modifiers[factor] = u'{factor} from {types}'.format(
                        factor=defensive_reply_factors[factor],
                        types=', '.join(sorted(defensive_modifiers[factor]))
                    )

            reply_template += u"""http://veekun.com/dex/types/{link_name}"""

            self._reply(irc, reply_template.format(
                name=obj.name.capitalize(),
                offensive_modifiers='; '.join(offensive_modifiers[_]
                                              for _ in sorted(offensive_modifiers)),
                defensive_modifiers='; '.join(defensive_modifiers[_]
                                              for _ in sorted(defensive_modifiers)),
                link_name=urllib.quote(obj.name.lower().encode('utf8')),
                )
            )

        elif isinstance(obj, tables.Item):
            reply_template = \
                u"""{name}, an item.  {effect}  """ \
                """http://veekun.com/dex/items/{link_pocket}/{link_name}"""

            effect = obj.short_effect
            if effect is None:
                effect = 'No short effect, sorry.  :('
            else:
                effect = unicode(effect.as_text())

            self._reply(irc, reply_template.format(
                name=obj.name,
                effect=effect,
                link_pocket=urllib.quote(obj.pocket.name.lower().encode('utf8')),
                link_name=urllib.quote(obj.name.lower().encode('utf8')),
                )
            )

        elif isinstance(obj, tables.Ability):
            reply_template = \
                u"""{name}, an ability.  {effect}  """ \
                """http://veekun.com/dex/abilities/{link_name}"""
            self._reply(irc, reply_template.format(
                name=obj.name,
                effect=obj.short_effect.as_text(),
                link_name=urllib.quote(obj.name.lower().encode('utf8')),
                )
            )

        elif isinstance(obj, tables.Nature):
            reply_template = \
                u"""{name}, a nature.  """ \
                u"""Raises \x0303{up}\x0f, lowers \x0304{down}\x0f.  """ \
                u"""http://veekun.com/dex/natures/{link_name}"""
            self._reply(irc, reply_template.format(
                name=obj.name,
                up=obj.increased_stat.name,
                down=obj.decreased_stat.name,
                link_name=urllib.quote(obj.name.lower().encode('utf8')),
                )
            )

        else:
            # This can only happen if lookup.py is upgraded and we are not
            self._reply(irc, "Uhh..  I found that, but I don't know what it is.  :(")

    pokedex = wrap(pokedex, [rest('something')])

    def _reply(self, irc, response):
        """Wraps irc.reply() to do some Unicode decoding."""
        if isinstance(response, str):
            irc.reply(response)
        else:
            irc.reply(response.encode('utf8'))


Class = Pokedex


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
