from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

class FeatheryPassive(Passive):
    """As long as Swablu is on your Bench, prevent all damage done to Swablu by
    your opponent's attacks."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        return bool(calc.is_attack and calc.is_opposing and holder is not None
                    and calc.target is holder and not is_in_active_spot(holder))


card = PokemonCardDef(
    guid="354243fc-44c9-558f-8b5d-d606261848be",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    display_name="Swablu",
    searchable_by=["Swablu", "Basic", "Swablu"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=333,
    abilities=[
        Ability(
            title="Feathery",
            game_text="As long as Swablu is on your Bench, prevent all damage done to Swablu by opponent's attacks.",
            passive=FeatheryPassive(),
        ),
        Attack(
            title="Razor Wind",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)