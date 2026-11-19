from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    AttrID, CardType, PokemonTypes, PokemonStage, Rarities,
)
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.session.passives import carrier_pokemon


def _holds_energy(target, carrier) -> bool:
    """Only this Squirtle, and only while it has an Energy card attached."""
    holder = carrier_pokemon(carrier)
    if target is None or holder is None or holder is not target:
        return False
    return any(card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value
               for card in target.children)

card = PokemonCardDef(
    guid="3610ca9e-beb5-5753-8b4b-7ed4526e4b79",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="POP4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=7,
    abilities=[
        Ability(
            title="Shell Retreat",
            game_text="As long as Squirtle has any Energy cards attached to it, damage done to Squirtle by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            passive=takes_less_passive(10, protects=_holds_energy),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)