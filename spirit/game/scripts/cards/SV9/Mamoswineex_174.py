from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="109ef57c-e235-5a4e-b59e-1430d144bf62",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswineex.Name",
    display_name="Mamoswine ex",
    searchable_by=["Mamoswine ex", "Stage 2", "ex", "Mamoswineex"],
    subtypes=["Stage 2", "ex"],
    collector_number=174,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Mammoth Hauler",
            game_text="Once during your turn, you may search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Rumbling March",
            game_text="This attack does 40 more damage for each Stage 2 Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=180,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)