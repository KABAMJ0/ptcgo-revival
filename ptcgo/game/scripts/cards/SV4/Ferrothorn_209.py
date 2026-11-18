from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.passives_common import (
    boost_own_next_turn, takes_less_passive,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d290c3b9-f17d-514d-8140-1a1046accdca",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=209,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Spinning Needles",
            game_text="During your next turn, this Pok\u00e9mon's Spinning Needles attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=boost_own_next_turn(100, attack_title="Spinning Needles"),
        ),
    ],
)