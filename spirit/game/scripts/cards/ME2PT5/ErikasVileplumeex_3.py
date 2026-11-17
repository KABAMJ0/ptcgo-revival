from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df6487f0-f21f-5f8b-a63f-5e6f40974c30",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasVileplumeex.Name",
    display_name="Erika's Vileplume ex",
    searchable_by=["Erika's Vileplume ex", "Stage 2", "ex", "ErikasVileplumeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=3,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Lovely Fragrance",
            game_text="Once during your turn, you may use this Ability. Heal 30 damage from each of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Bloom Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)