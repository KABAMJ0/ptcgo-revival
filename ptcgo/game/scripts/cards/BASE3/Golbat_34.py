from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import heal_self_damage_dealt

card = PokemonCardDef(
    guid="3698c10b-fe77-5951-800e-dbb63c25cb61",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    display_name="Golbat",
    searchable_by=["Golbat", "Stage 1", "Golbat"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
        Attack(
            title="Leech Life",
            game_text="Remove a number of damage counters from Golbat equal to the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance). If Golbat has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=heal_self_damage_dealt(),
        ),
    ],
)