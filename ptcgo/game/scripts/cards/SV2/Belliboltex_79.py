from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5eb7e7a5-3353-5bc2-8042-f5b40c24168f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Belliboltex.Name",
    display_name="Bellibolt ex",
    searchable_by=["Bellibolt ex", "Stage 1", "ex", "Belliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=79,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Attack(
            title="Jumping Press",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Paralyzing Ball",
            game_text="You may discard 2 Lightning Energy from this Pok\u00e9mon to make your opponent's Active Pok\u00e9mon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)