from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

class SubmergePassive(Passive):
    """As long as Feebas is on your Bench, prevent all damage done to Feebas by
    attacks (both yours and your opponent's)."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        return bool(calc.is_attack and holder is not None
                    and calc.target is holder and not is_in_active_spot(holder))


card = PokemonCardDef(
    guid="5b2174dd-f0f9-575b-9d85-390663fbafad",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as Feebas is on your Bench, prevent all damage done to Feebas by attacks (both yours and your opponent's).",
            passive=SubmergePassive(),
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)