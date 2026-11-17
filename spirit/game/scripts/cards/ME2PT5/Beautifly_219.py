from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b291433f-be16-5377-96dc-7a8c300e9737",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=219,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Energy Straw",
            game_text="Your opponent reveals their hand, and this attack does 80 damage for each Energy card you find there.",
            cost={PokemonTypes.GRASS: 1},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)