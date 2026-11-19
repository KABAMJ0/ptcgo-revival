from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import def_for
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import attach_from_hand


class FrenzyPassive(Passive):
    """Attacks do 40 more to the Defending Pokemon while the opponent has any of
    the named Pokemon in play."""

    NAMES = ('Groudon', 'Groudon ex', 'Rayquaza', 'Rayquaza ex')

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.attacker is None or carrier_pokemon(carrier) is not calc.attacker:
            return
        if not getattr(calc, "to_active", False):
            return
        for player_id in calc.board.player_ids:
            if player_id == calc.attacker.owning_player_id:
                continue
            for pokemon in calc.board.pokemon_in_play(player_id):
                definition = def_for(pokemon.archetype_id)
                if definition is not None and definition.display_name in self.NAMES:
                    calc.amount += 40
                    return



card = PokemonCardDef(
    guid="1c23b547-8b26-5dfe-b0c1-bb0ff749fe91",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "EX", "Kyogreex"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="As long as your opponent has Groudon, Groudon ex, Rayquaza, or Rayquaza ex in play. Kyogre ex's attacks do 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=FrenzyPassive(),
        ),
        Attack(
            title="Aqua Supply",
            game_text="You may attach a basic Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=composed(lambda ctx: ctx.deal_damage(), attach_from_hand(is_basic_energy_card, count=1, target='choice', minimum=0)),
        ),
        Attack(
            title="Tsunami",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
    ],
)