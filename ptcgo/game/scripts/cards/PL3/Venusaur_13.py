from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9bec792-85f2-5948-98e2-b4dfd82ec907",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Green Aroma",
            game_text="Remove all Special Conditions from each of your Grass Pok\u00e9mon. Each of your Grass Pok\u00e9mon can't be affected by any Special Conditions.",
            effect=unimplemented,
        ),
        Attack(
            title="Desperate Pollen",
            game_text="If Venusaur already has 8 or more damage counters on it, the Defending Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Special Reaction",
            game_text="If the Defending Pok\u00e9mon is affected by any Special Conditions, this attack does 40 damage plus 40 more damage for each of those Special Conditions.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)