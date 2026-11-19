from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59cc9176-e3aa-5eb1-9fef-98a7e107afbe",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFlaaffy.Name",
    display_name="Dark Flaaffy",
    searchable_by=["Dark Flaaffy", "Stage 1", "DarkFlaaffy"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Thunder Slash",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, the Defending Pok\u00e9mon is now Paralyzed. Dark Flaaffy can't use Thunder Slash during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)