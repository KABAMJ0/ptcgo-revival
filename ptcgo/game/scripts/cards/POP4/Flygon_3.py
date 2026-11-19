from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    AttrID, CardType, PokemonTypes, PokemonStage, Rarities,
)
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.card_effects.passives_common import retreat_free_when


def _holds_energy(pokemon, carrier) -> bool:
    """Free retreat only while this Flygon has an Energy card on it."""
    if pokemon is None:
        return False
    return any(card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value
               for card in pokemon.children)

card = PokemonCardDef(
    guid="cdf81a41-7dbd-520f-8e67-409f7e3c88d9",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="POP4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=330,
    abilities=[
        Ability(
            title="Levitate",
            game_text="As long as Flygon has any Energy attached to it, the Retreat Cost for Flygon is 0.",
            passive=retreat_free_when(_holds_energy),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Sand Pit",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=no_retreat_attack(),
        ),
    ],
)