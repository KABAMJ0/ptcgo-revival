from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4f0822c3-4a53-58c2-aaaa-64126e88021b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Swing Dance",
            game_text="Once during your turn (before your attack), you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Circular Steps",
            game_text="This attack does 10 more damage for each other Pok\u00e9mon in play (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)